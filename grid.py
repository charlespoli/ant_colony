from interaction_point import InteractionPoint

class Grid(object):

    def __init__(self, width, height):

        self.width = width
        self.height = height

        self.grid = [[[] for x in range(self.width)]for y in range(
            self.height)]


    def set_interaction_points(self):

        home = InteractionPoint(0, 0, False)
        food = InteractionPoint(self.width - 1, self.height - 1, True)

        self.grid[home.coordX][home.coordY].append(home)
        self.grid[food.coordX][food.coordY].append(food)

    def update_odour(self):
        # Odour decays

    def check_interaction_point(self):
        # Checks if ant reaches interaction_point





