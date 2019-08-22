from constant import *


class Case(object):

    def __init__(self):
        self.odour_home = 0
        self.odour_food = 0


class InteractionPoint(object):

    def __init__(self, isFood):

        self.isFood = isFood

    def draw_point(self, canvas, coordX, coordY):

        x = coordX * CELL_SIZE
        y = coordY * CELL_SIZE
        if self.isFood:
            color = COLOR_RED

        else:
            color = COLOR_BLUE

        canvas.create_rectangle(x, y, x + CELL_SIZE - 1, y + CELL_SIZE -
                                1, fill=color)
