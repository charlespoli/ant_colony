from tkinter import *
from grid import Grid
from constant import *
from drawing_manager import *
from ant import *
from random import randint
from time import sleep

fenetre = Tk()
fenetre.geometry("1200x800")
# fenetre.resizable(0, 0)

DM = Drawer(fenetre)

test_grid = Grid()

test_grid.set_interaction_points()

test_grid.print_grid()

for i in range(20):
    Ant(randint(0, GRID_WIDTH - 1), randint(0, GRID_HEIGHT - 1))

DM.draw_grid(test_grid.grid)
DM.draw_ants(Ant.List)
fenetre.mainloop()

for i in range(20):
    for ant in Ant.List:
        ant.update_position()
    DM.update_ants(Ant.List)

    sleep(0.5)



# while True:

# grid.update_odour()
# ant.update_position()
# grid.check_interaction_point()
