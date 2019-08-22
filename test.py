from tkinter import *
from grid import Grid
from constant import *
from drawing_manager import *

fenetre = Tk()
fenetre.geometry("1200x800")
# fenetre.resizable(0, 0)

DM = Drawer(fenetre)

test_grid = Grid()

test_grid.set_interaction_points()

test_grid.print_grid()

DM.draw_grid(test_grid.grid)

fenetre.mainloop()

# while True:

# grid.update_odour()
# ant.update_position()
# grid.check_interaction_point()
