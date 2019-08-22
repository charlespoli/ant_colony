from random import choice
from grid import Grid
from constant import *
from tkinter import *


class Ant(object):

    List = []

    def __init__(self, coordX, coordY, canvas, isHungry = True):

        self.coordX = coordX
        self.coordY = coordY
        x = self.coordX * CELL_SIZE
        y = self.coordY * CELL_SIZE
        self.canvas = canvas
        self.rectangle = self.canvas.create_rectangle(x, y, x + CELL_SIZE - 1,
                                         y + CELL_SIZE - 1, fill=COLOR_ANT)

        self.isHungry = isHungry

        Ant.List.append(self)


    def update_position(self):
        # Update ant's position and leave odour on previous

        #self.leave_odour()
        self.ant_movement()



    def ant_movement(self):

        directions = []

        if self.coordX - 1 > 0:
            directions.append('L')
        if self.coordY - 1 > 0:
            directions.append('U')
        if self.coordX + 1 < GRID_WIDTH:
            directions.append('R')
        if self.coordY + 1 < GRID_HEIGHT:
            directions.append('D')

        dir = choice(directions)

        if dir == 'R':
            self.canvas.move(self.rectangle, CELL_SIZE, 0)
            self.coordX += 1
        elif dir == 'L':
            self.canvas.move(self.rectangle, - CELL_SIZE, 0)
            self.coordX -= 1
        elif dir == 'D':
            self.canvas.move(self.rectangle, 0, CELL_SIZE)
            self.coordY += 1
        elif dir == 'U':
            self.canvas.move(self.rectangle, 0, - CELL_SIZE)
            self.coordY -= 1


    def leave_odour(self):
        pass



    def draw_ant(self):
        pass



