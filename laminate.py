from model.tile import Tile
from model.room import Room
from model.installation import Installation
from ui.printer import Printer


def main():
    room = Room(3330, 2700)
    tile = Tile(1286, 194)
    border = 8
    init = {
        5: 1286,
        10: 1286
    }

    installation = Installation(room, tile, border, init)

    plan = installation.process()
    installation.print()
    Printer.print(plan)


if __name__ == '__main__':
    main()
