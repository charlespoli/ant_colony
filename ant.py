class Ant(object):

    def __init__(self, coordX, coordY, isHungry = True):

        self.coordX = coordX
        self.coordY = coordY
        self.isHungry = isHungry


    def update_position(self):
        # Update ant's position and leave odour on previous location

        ant_movement()
        leave_odour()


    def ant_movement(self):
        pass


    def leave_odour(self):
        pass

