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

    # def draw_ants(self, antList):
    #
    #     for ant in antList:
    #         x = ant.coordX * CELL_SIZE
    #         y = ant.coordY * CELL_SIZE
    #         rec = self.canvas.create_rectangle(x, y, x + CELL_SIZE - 1,
    #                                      y + CELL_SIZE - 1, fill=COLOR_ANT)
    #         self.AntSpriteList.append(rec)
    #
    # def update_ants(self, antList):
    #
    #     for i in range(len(self.AntSpriteList)):
    #         #dx = self.canvas.coords(self.AntSpriteList[i])[0] - antList[i].coordX
    #         #dy = self.canvas.coords(self.AntSpriteList[i])[1] - antList[i].coordY
    #         x = antList[i].coordX
    #         y = antList[i].coordY
    #         self.canvas.move(self.AntSpriteList[i], x, y)
    #         self.canvas.after(100, self.update_ants)

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
