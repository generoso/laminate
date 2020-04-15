class Plan:

    def __init__(self, room, rows):
        self.room = room
        self.rows = rows

    def __str__(self):
        str_list = []
        for i, r in enumerate(self.rows):
            str_list.append(str(i) + " : ")
            for t in r:
                str_list.append(str(t))
            str_list.append('\n')
        return ''.join(str_list)
