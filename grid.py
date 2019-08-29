from case import *


class Grid(object):

    def __init__(self, canvas):

        self.grid = []
        for y in range(GRID_HEIGHT):
            self.grid.append([])
            for x in range(GRID_WIDTH):
                self.grid[y].append(Case(x, y, canvas))

    def set_interaction_points(self):
        """Places the interaction points on the grid."""
        home = InteractionPoint(0, 0, False)
        food = InteractionPoint(GRID_WIDTH - 1, GRID_HEIGHT - 1, True)

        self.grid[0][0] = home
        self.grid[GRID_HEIGHT - 1][GRID_WIDTH - 1] = food

    def print_grid(self):
        """Prints grid with cases and interaction points."""
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
        """Draws the grid on the canvas."""
        for row in self.grid:
            for element in row:
                if isinstance(element, InteractionPoint):
                    element.draw_point(canvas)

    def update_odour(self):
        # Odour decays by 1 unit.
        for row in self.grid:
            for element in row:
                if isinstance(element, Case):
                    if element.odour_home > 0:
                        element.odour_home -= 0.5
                    elif element.odour_food > 0:
                        element.odour_food -= 0.5

    def draw_odours(self, canvas):
        for row in self.grid:
            for element in row:
                if isinstance(element, Case):
                    element.draw_odour(canvas)

