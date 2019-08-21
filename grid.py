class Grid(object):

    def __init__(self, width, height):

        self.width = width
        self.height = height

        self.Matrix = [[0 for x in range(self.width)] for y in range(
            self.height)]
