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
            left_case = self.grid.grid[self.coordX - 1][self.coordY]
            if not isinstance(left_case, InteractionPoint):
                directions.append('L')

        if self.coordY - 1 > 0:
            up_case = self.grid.grid[self.coordX][self.coordY - 1]
            if not isinstance(up_case, InteractionPoint):
                directions.append('U')

        if self.coordX + 1 < GRID_WIDTH:
            right_case = self.grid.grid[self.coordX + 1][self.coordY]
            if not isinstance(right_case, InteractionPoint):
                directions.append('R')

        if self.coordY + 1 < GRID_HEIGHT:
            down_case = self.grid.grid[self.coordX][self.coordY + 1]
            if not isinstance(down_case, InteractionPoint):
                directions.append('D')

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
        elif dir == None:
            pass

    def odour_movement(self, coeff, index, weight):
        # Adjust the weight values accordingly to odour coefficients.
        # TODO update function with for loop.
        new_value = weight[index] + (coeff * ODOUR_FACTOR * (len(weight) - 1))

        new = [weight[x] - coeff * ODOUR_FACTOR for x in range(len(weight)) if
               x != index]
        new.insert(index, new_value)
        return new

    def check_interaction_point(self, case):
        if self.isHungry:
            if isinstance(case, InteractionPoint) and case.isFood:
                self.isHungry = False
                return True
            else:
                return False
        else:
            if isinstance(case, InteractionPoint) and not case.isFood:
                self.isHungry = True
                return True
            else:
                return False

    def leave_odour(self):
        """Leave odour at the ant's current position."""
        current_case = self.grid.grid[self.coordX - 1][self.coordY - 1]

        if self.isHungry:
            current_case.odour_home += 5
            if current_case.odour_home > 50:
                current_case.odour_home = 50
        else:
            current_case.odour_food += 5
            if current_case.odour_food > 50:
                current_case.odour_food = 50

    def adjust_weight(self, case, weight, current_index):
        if self.isHungry:
            reading = case.odour_food
        else:
            reading = case.odour_home

        if reading > 0:
            new_weight = self.odour_movement(reading, current_index,
                            weight)
            return new_weight




