from constant import *


class AbstractCase(object):

    def __init__(self, coordX, coordY):

        self.coordX = coordX
        self.coordY = coordY


class Case(AbstractCase):

    def __init__(self, coordX, coordY):

        super().__init__(coordX, coordY)
        self.odour_home = 0
        self.odour_food = 0


class InteractionPoint(AbstractCase):

    def __init__(self, coordX, coordY, isFood):

        super().__init__(coordX, coordY)
        self.isFood = isFood

    def draw_point(self, canvas):

        x = self.coordX * CELL_SIZE
        y = self.coordY * CELL_SIZE
        if self.isFood:
            color = COLOR_RED

        else:
            color = COLOR_BLUE

        canvas.create_rectangle(x, y, x + CELL_SIZE - 1, y + CELL_SIZE -
                                1, fill=color)
