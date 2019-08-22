from case import *


class Grid(object):

    def __init__(self):
        self.grid = []
        for y in range(GRID_HEIGHT):
            self.grid.append([])
            for x in range(GRID_WIDTH):
                self.grid[y].append(Case(x, y))

    def set_interaction_points(self):
        home = InteractionPoint(0, 0, False)
        food = InteractionPoint(GRID_WIDTH - 1, GRID_HEIGHT - 1, True)

        self.grid[0][0] = home
        self.grid[GRID_HEIGHT - 1][GRID_WIDTH - 1] = food

    def print_grid(self):
        for row in self.grid:
            buffer = ""
            for element in row:
                if isinstance(element, Case):
                    buffer += 'C'

                elif isinstance(element, InteractionPoint):
                    if element.isFood:
                        buffer += 'F'
                    else:
                        buffer += 'H'
            print(buffer)

    def draw_grid(self, canvas):
        for row in self.grid:
            for element in row:
                if isinstance(element, Case):
                    pass

                elif isinstance(element, InteractionPoint):
                    element.draw_point(canvas)

    def update_odour(self):
        # Odour decays
        pass

    def check_interaction_point(self):
        pass
        # Checks if ant reaches interaction_point
