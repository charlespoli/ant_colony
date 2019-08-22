from tkinter import *
from constant import *
from grid import *
from case import *


class Drawer(object):



    def __init__(self, fenetre):

        self.canvas = Canvas(fenetre, width=CANVAS_WIDTH, height=CANVAS_HEIGHT,
                             background='#D3D3D3')
        self.canvas.pack()
        self.AntSpriteList = []

    def draw_ants(self, antList):

        for ant in antList:
            x = ant.coordX * CELL_SIZE
            y = ant.coordY * CELL_SIZE
            self.AntSpriteList.append(self.canvas.create_rectangle(x, y, x + CELL_SIZE - 1,
                                         y + CELL_SIZE - 1, fill=COLOR_ANT))

    def update_ants(self, antList):

        for i in range(len(self.AntSpriteList)):
            x = antList[i].coordX * CELL_SIZE
            y = antList[i].coordY * CELL_SIZE
            self.canvas.coords(self.AntSpriteList[i], [x, y, x + CELL_SIZE - 1,
                                         y + CELL_SIZE - 1])



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
