class Tile:
    def __init__(self, length, width):
        """Longer side should be the length parameter"""
        self.length = length
        self.width = width

    def __str__(self):
        return "[" + str(self.length) + ", " + str(self.width) + "]"