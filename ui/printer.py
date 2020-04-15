import copy
from ui.graphics import *
from model.plan import Plan


def scale(plan: Plan):
    scaled = copy.deepcopy(plan)

    if scaled.room.l1 > Printer.WIDTH:
        factor = Printer.WIDTH / scaled.room.l1

        scaled.room.l1 = round(scaled.room.l1 * factor)
        scaled.room.l2 = round(scaled.room.l2 * factor)

        for r in scaled.rows:
            for t in r:
                t.length = round(t.length * factor)
                t.width = round(t.width * factor)

    return scaled


def draw_row(win, y, r, original_row_index, original_plan):
    tile_point = Point(0, y)
    draw_row_index(original_row_index, tile_point, win)
    for tile_index, t in enumerate(r):
        if tile_index == 0 or tile_index == (len(r) - 1):
            draw_tile_size(t, original_plan.rows[original_row_index][tile_index], tile_point, win)
        tile = Rectangle(tile_point, Point(tile_point.getX() + t.length, tile_point.getY() + t.width))
        tile_point = Point(tile_point.getX() + t.length, y)
        tile.draw(win)


def draw_row_index(row_index, tile_point, win):
    text_point = tile_point.clone()
    text_point.move(11, 10)
    text = Text(text_point, str(row_index))
    text.setSize(10)
    text.draw(win)


def draw_tile_size(scaled_tile, original_plan_tile, tile_point, win):
    text_point = tile_point.clone()
    text_point.move(scaled_tile.length / 2, scaled_tile.width / 2)
    text = Text(text_point, original_plan_tile.length)
    text.setFill("blue")
    text.draw(win)


class Printer:
    WIDTH = 1000

    @staticmethod
    def print(plan: Plan):
        scaled = scale(plan)

        room = scaled.room
        win = GraphWin(title="laminate", width=room.l1, height=room.l2)
        win.setCoords(0, 0, room.l1, room.l2)

        p = Point(0, 0)
        for i, r in enumerate(reversed(scaled.rows)):
            draw_row(win, p.getY(), r, len(scaled.rows) - i - 1, plan)
            p = Point(0, p.getY() + r[0].width)

        win.getMouse()
        win.close()
