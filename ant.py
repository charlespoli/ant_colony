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
            directions.append('l')
        if self.coordY - 1 > 0:
            directions.append('u')
        if self.coordX + 1 < GRID_WIDTH:
            directions.append('r')
        if self.coordY + 1 < GRID_HEIGHT:
            directions.append('d')

        weight = [1/len(directions) for i in range(len(directions))]
        current_index = 0

        if 'l' in directions:
            left_case = self.grid.grid[self.coordX - 1][self.coordY]
            food = left_case.odour_food
            home = left_case.odour_home

            if self.check_interaction_point(left_case):
                return None
            else:
                if self.isHungry:
                    if food > 0:
                        weight = self.odour_movement(food, current_index,
                            weight)
                        current_index += 1
                else:
                    if home > 0:
                        weight = self.odour_movement(home, current_index,
                            weight)
                        current_index += 1


        if 'u' in directions:
            up_case = self.grid.grid[self.coordX][self.coordY - 1]
            food = up_case.odour_food
            home = up_case.odour_home

            if self.check_interaction_point(up_case):
                return None
            else:
                if self.isHungry:
                    if food > 0:
                        weight = self.odour_movement(food, current_index,
                            weight)
                        current_index += 1
                else:
                    if home > 0:
                        weight = self.odour_movement(up_case.odour_food,
                            current_index, weight)
                        current_index += 1

        if 'r' in directions:
            right_case = self.grid.grid[self.coordX + 1][self.coordY]
            food = right_case.odour_food
            home = right_case.odour_home

            if self.check_interaction_point(right_case):
                return None
            else:
                if self.isHungry:
                    if food > 0:
                        weight = self.odour_movement(food, current_index,
                                                     weight)
                        current_index += 1
                else:
                    if home > 0:
                        weight = self.odour_movement(up_case.odour_food,
                                                     current_index, weight)
                        current_index += 1

        if 'd' in directions:
            down_case = self.grid.grid[self.coordX][self.coordY + 1]
            food = down_case.odour_food
            home = down_case.odour_home

            if self.check_interaction_point(down_case):
                return None
            else:
                if self.isHungry:
                    if food > 0:
                        weight = self.odour_movement(food, current_index,
                            weight)
                        current_index += 1
                else:
                    if home > 0:
                        weight = self.odour_movement(up_case.odour_food,
                            current_index, weight)
                        current_index += 1

        dir = choices(directions, weight, k=1)

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
            if isinstance(to_check, InteractionPoint) and not to_check.isFood:
                self.isHungry = True
                return True
            else:
                return False

    def leave_odour(self):
        """Leave odour at the ant's current position."""
        current_case = self.grid.grid[self.coordX - 1][self.coordY - 1]
        if self.isHungry:
            current_case.odour_home += 5
        else:
            current_case.odour_food += 5






