class Grid(object):

    def __init__(self, width, height):

        self.width = width
        self.height = height

        self.grid = [[[] for x in range(self.width)]for y in range(
            self.height)]



