from tkinter import *
from constant import *
from grid import *
from case import *


class Drawer(object):

    def __init__(self, fenetre):

        self.canvas = Canvas(fenetre, width=CANVAS_WIDTH, height=CANVAS_HEIGHT,
                             background='#D3D3D3')
        self.canvas.pack()

    def draw_grid(self, grid):

        for row in grid:
            for element in row:
                if isinstance(element, Case):
                    pass

                elif isinstance(element, InteractionPoint):
                    x = element.coordX * CELL_SIZE
                    y = element.coordY * CELL_SIZE
                    if element.isFood:
                        color = COLOR_RED

                    else:
                        color = COLOR_BLUE

                    self.canvas.create_rectangle(x, y, x + CELL_SIZE - 1,
                                                 y + CELL_SIZE - 1, fill=color)
                    print(x, y)
