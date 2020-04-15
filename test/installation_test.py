import unittest
from model.tile import Tile
from model.room import Room
from model.installation import Installation


class TestInstallation(unittest.TestCase):

    def test_a(self):
        room = Room(3330, 2700)
        tile = Tile(1286, 194)
        border = 8
        init = {
            0: 1286,
            12: 1286
        }

        installation = Installation(room, tile, border, init)
        plan = installation.process()
        installation.print()
        self.sanity_checks(init, plan, room, border)

    def test_b(self):
        room = Room(100, 50)
        tile = Tile(60, 20)
        border = 0
        init = {}

        installation = Installation(room, tile, border, init)
        plan = installation.process()
        installation.print()
        self.sanity_checks(init, plan, room, border)

    def sanity_checks(self, init, plan, room, border):
        tot_l2 = 0
        for i, r in enumerate(plan.rows):
            tot_l2 = tot_l2 + r[0].width
            if init.get(i) is not None:
                self.assertEqual(r[0].length, init.get(i), "Line {} is wrong".format(i))

            tot_l1 = 0
            for t in r:
                self.assertTrue(t.length != 0)
                self.assertTrue(t.width != 0)
                tot_l1 = tot_l1 + t.length
            self.assertEqual(room.l1 - 2 * border, tot_l1, "Line {} is wrong".format(i))

        self.assertEqual(tot_l2, room.l2 - 2 * border, "Line {} is wrong".format(i))


if __name__ == '__main__':
    unittest.main()
