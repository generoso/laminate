from model.tile import Tile
from model.room import Room
from model.plan import Plan
import math
import copy


class GridInstallation:
    """ Quick and dirty adaptation of the installation class for simple tiles, organized as a grid.
    
    In this context the border should be set to 0, and (half of) the grout line width should be included in the tile size.
    """

    def __init__(self, room, tile, border, init):
        self.room = room
        self.tile = tile
        self.border = border
        self.init_tiles = init

    def print(self):
        print("## Grid Installation ##")
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
        result = []
        rows, last_row_width = self.compute_rows_and_last_row_width()

        print(f'Rows {rows}, last {last_row_width}')

        for r in range(rows):
            row = self.create_row(self.room, self.init_tiles, r, (r + 1) == rows, last_row_width)
            result.append(row)

        return Plan(self.room, result)

    def compute_rows_and_last_row_width(self):
        tot_width = 0
        r = 0
        while(True):
            new_tot_width = tot_width
            if self.init_tiles.get(r):
                new_tot_width += self.init_tiles.get(r)[1]
            else:
                new_tot_width += self.tile.width

            if new_tot_width > self.room.l2:
                return (r+1, self.room.l2 - tot_width)
            if new_tot_width == self.room.l2:
                if self.init_tiles.get(r) is not None:            
                    return (r+1, self.init_tiles.get(r)[1])
                else:
                    return (r+1, self.tile.width)
            r = r+1
            tot_width = new_tot_width

    def create_row(self, room, first_tiles, index, is_last, last_row_width):

        f_tile = copy.deepcopy(self.tile)
        if first_tiles.get(index) is not None:
            f_tile = Tile(first_tiles.get(index)[0], first_tiles.get(index)[1])

        m_tile = copy.deepcopy(self.tile)
        m_tile.width = f_tile.width
        if is_last and last_row_width > 0:
            m_tile.width = last_row_width
            f_tile.width = last_row_width

        row = [f_tile]
        whole_tiles = math.floor((room.l1 - f_tile.length) / self.tile.length)
        for t in range(whole_tiles):
            row.append(copy.deepcopy(m_tile))
        last = room.l1 - f_tile.length - whole_tiles * m_tile.length
        if last != 0:
            row.append(Tile(last, m_tile.width))

        return row
