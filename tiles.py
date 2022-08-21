from model.tile import Tile
from model.room import Room
from model.grid_installation import GridInstallation
from ui.printer import Printer


def main():
    room = Room(1810, 1210)
    # room = Room(1950, 1210)
    tile = Tile(601, 301)
    border = 0
    init = {
         0: (551, 201),
         1: (551, 301),
         2: (551, 301),
         3: (551, 301),
         4: (551, 301), # last

    }

    installation = GridInstallation(room, tile, border, init)

    plan = installation.process()
    installation.print()
    Printer.print(plan)


if __name__ == '__main__':
    main()
