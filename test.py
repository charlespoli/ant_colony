from tkinter import * 
from grid import Grid
from constant import *

fenetre = Tk()
fenetre.geometry("1200x800")
fenetre.resizable(0, 0)

width = CANVAS_WIDTH
height = CANVAS_HEIGHT
canvas = Canvas(fenetre, width=width, height=height, background='#D3D3D3')


test = Grid()

test.set_interaction_points()
test.
test.print_grid()



canvas.pack()

fenetre.mainloop()







# while True:

    # grid.update_odour()
    # ant.update_position()
    # grid.check_interaction_point()