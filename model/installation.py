from model.tile import Tile
from model.room import Room
from model.plan import Plan
import math
import copy


class Installation:

    def __init__(self, room, tile, border, init):
        self.room = room
        self.tile = tile
        self.border = border
        self.init_tiles = init

    def print(self):
        print("## Installation ##")
        print("* Room: " + str(self.room))
        print("* Tile: " + str(self.tile))
        print("* Border: " + str(self.border))
        print("* Init tiles: " + str(self.init_tiles))
        print("##")

        result = self.process()
        for i, r in enumerate(result.rows):
            print(str(i) + " : ", end='')
            print(*r)

        print("##")

    def process(self):
        actual_room = Room(self.room.l1 - 2 * self.border, self.room.l2 - 2 * self.border)

        rows = math.ceil(actual_room.l2 / self.tile.width)
        rest = 0
        result = []
        for r in range(rows):
            row, rest = self.create_row(actual_room, rest, self.init_tiles, r, (r + 1) == rows)
            result.append(row)

        return Plan(actual_room, result)

    def create_row(self, actual_room, rest, first_tiles, index, is_last):

        f_tile = copy.deepcopy(self.tile)
        if first_tiles.get(index) is not None:
            f_tile.length = first_tiles.get(index)
        elif rest != 0:
            f_tile.length = rest

        m_tile = copy.deepcopy(self.tile)
        last_row_width = actual_room.l2 % self.tile.width
        if is_last and last_row_width > 0:
            m_tile.width = last_row_width
            f_tile.width = last_row_width

        row = [f_tile]
        whole_tiles = math.floor((actual_room.l1 - f_tile.length) / self.tile.length)
        for t in range(whole_tiles):
            row.append(copy.deepcopy(m_tile))
        last = actual_room.l1 - f_tile.length - whole_tiles * m_tile.length
        if last != 0:
            row.append(Tile(last, m_tile.width))
        r = m_tile.length - last

        return row, r
