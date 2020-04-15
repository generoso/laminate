class Room:

    def __init__(self, l1, l2):
        """Longer side of a tile will be parallel to l1"""
        self.l1 = l1
        self.l2 = l2

    def __str__(self):
        return "[" + str(self.l1) + ", " + str(self.l2) + "]"
