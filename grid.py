from constant import *
from case import *


class Grid(object):

    def __init__(self):

        self.width = GRID_WIDTH
        self.height = GRID_HEIGHT

        self.grid = [[ Case() for x in range(self.width)]for y in range(
            self.height)]


    def set_interaction_points(self):

        home = InteractionPoint(False)
        food = InteractionPoint(True)

        self.grid[0][0] = home
        self.grid[self.height - 1][self.width - 1] = food

    def print_grid(self):

        for row in self.grid:
            buffer = ""
            for element in row:
                if (isinstance(element, Case)):
                    buffer += 'C'

                elif (isinstance(element, InteractionPoint)):
                    if element.isFood:
                        buffer += 'F'
                    else:
                        buffer += 'H'
            print(buffer)


    def update_odour(self):
        # Odour decays
        pass

    def check_interaction_point(self):
        pass
        # Checks if ant reaches interaction_point





