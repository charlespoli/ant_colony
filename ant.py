from random import choice
from grid import Grid
from constant import *
from tkinter import *
from case import *
from random import choices


class Ant(object):

    List = []

    def __init__(self, coordX, coordY, grid, canvas, isHungry = True):

        self.coordX = coordX
        self.coordY = coordY
        x = self.coordX * CELL_SIZE
        y = self.coordY * CELL_SIZE
        self.canvas = canvas
        self.rectangle = self.canvas.create_rectangle(x, y, x + CELL_SIZE - 1,
            y + CELL_SIZE - 1, fill=COLOR_ANT)

        self.isHungry = isHungry
        self.grid = grid

        Ant.List.append(self)

    def ant_movement(self):

        directions = []

        if self.coordX - 1 > 0:
            left_case = self.grid.grid[self.coordY][self.coordX - 1]
            if not isinstance(left_case, InteractionPoint):
                directions.append('L')
            else:
                self.change_target(left_case)

        if self.coordY - 1 > 0:
            up_case = self.grid.grid[self.coordY - 1][self.coordX]
            if not isinstance(up_case, InteractionPoint):
                directions.append('U')
            else:
                self.change_target(up_case)

        if self.coordX + 1 < GRID_WIDTH:
            right_case = self.grid.grid[self.coordY][self.coordX + 1]
            if not isinstance(right_case, InteractionPoint):
                directions.append('R')
            else:
                self.change_target(right_case)

        if self.coordY + 1 < GRID_HEIGHT:
            down_case = self.grid.grid[self.coordY + 1][self.coordX]
            if not isinstance(down_case, InteractionPoint):
                directions.append('D')
            else:
                self.change_target(down_case)

        weight = [1/len(directions) for i in range(len(directions))]
        current_index = 0

        if 'L' in directions:
            weight = self.adjust_weight(left_case, weight, current_index)
            current_index += 1

        if 'U' in directions:
            weight = self.adjust_weight(up_case, weight, current_index)
            current_index += 1

        if 'R' in directions:
            weight = self.adjust_weight(right_case, weight, current_index)
            current_index += 1

        if 'D' in directions:
            weight = self.adjust_weight(down_case, weight, current_index)
            current_index += 1

        dir = choices(directions, weight)[0]

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
        elif dir is None:
            pass

    def adjust_weight(self, case, weight, current_index):
        # Adjust the weight values accordingly to odour coefficients.
        if self.isHungry:
            reading = case.odour_food
        else:
            reading = case.odour_home

        if reading > 0:

            for el in weight:
                el -= reading * ODOUR_FACTOR
            weight[current_index] += (reading * ODOUR_FACTOR * len(weight))
            return weight

    def change_target(self, point):
        if self.isHungry and point.isFood:
            self.isHungry = False
        elif not self.isHungry and not point.isFood:
            self.isHungry = True
        else:
            return

    def leave_odour(self):
        """Leave odour at the ant's current position."""
        current_case = self.grid.grid[self.coordY][self.coordX]

        if self.isHungry:
            current_case.odour_home += 5
            if current_case.odour_home > 50:
                current_case.odour_home = 50
        else:
            current_case.odour_food += 5
            if current_case.odour_food > 50:
                current_case.odour_food = 50





