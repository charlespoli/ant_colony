from random import choice
from grid import Grid


class Ant(object):

    def __init__(self, coordX, coordY, isHungry = True):

        self.coordX = coordX
        self.coordY = coordY
        self.isHungry = isHungry
        self.grid = Grid()


    def update_position(self):
        # Update ant's position and leave odour on previous

        #self.leave_odour()
        self.ant_movement()



    def ant_movement(self):

        directions = []

        if self.coordX > 0:
            directions.append('L')
        if self.coordY > 0:
            directions.append('U')
        if self.coordX < self.grid.width:
            directions.append('R')
        if self.coordY < self.grid.height:
            directions.append('D')

        dir = choice(directions)

        if dir == 'R':
            self.coordX += 1
        elif dir == 'L':
            self.coordX -= 1
        elif dir == 'D':
            self.coordY += 1
        elif dir == 'U':
            self.coordY -= 1


    def leave_odour(self):
        pass



    def draw_ant(self):
        pass



