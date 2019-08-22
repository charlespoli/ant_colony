from tkinter import *
from constant import *
from grid import *
from case import *

class Drawer(object):

    def __init__(self, fenetre):

        self.canvas = Canvas(fenetre, width=CANVAS_WIDTH, height=CANVAS_HEIGHT,
                        background='#D3D3D3')


    def draw_grid(self, grid):

        for row in grid:
            buffer = ""
            for element in row:
                if (isinstance(element, Case)):
                    buffer += 'C'

                elif (isinstance(element, InteractionPoint)):
                    x = coordX * CELL_SIZE
                    y = coordY * CELL_SIZE
                    if self.isFood:
                        color = COLOR_RED

                    else:
                        color = COLOR_BLUE

                    self.canvas.create_rectangle(x, y, x + CELL_SIZE - 1,
                        y + CELL_SIZE - 1, fill=color)
