from random import choice
from grid import Grid
from constant import *
from tkinter import *
from case import *


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

    def ant_movement(self):

        directions = []

        if self.coordX - 1 > 0:
            directions.append('l')
        if self.coordY - 1 > 0:
            directions.append('u')
        if self.coordX + 1 < GRID_WIDTH:
            directions.append('r')
        if self.coordY + 1 < GRID_HEIGHT:
            directions.append('d')










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

    def leave_odour(self, grid):
        '''Leave odour at the ant's current position.'''
        current_case = grid.grid[self.coordX - 1][self.coordY - 1]
        if self.isHungry:
            current_case.odour_home += 5
        else:
            current_case.odour_food += 5

    def check_interaction_point(self, grid):
        to_check = grid.grid[self.coordX][self.coordY]
        if self.isHungry:
            if isinstance(to_check, InteractionPoint) and to_check.isFood:
                self.isHungry = False
        else:
            if isinstance(to_check, InteractionPoint) and not to_check.isFood:
                self.isHungry = True






