from tkinter import * 
from grid import Grid
from constant import *

fenetre = Tk()
fenetre.geometry("1200x800")
fenetre.resizable(0, 0)

width = CANVAS_WIDTH
height = CANVAS_HEIGHT
canvas = Canvas(fenetre, width=width, height=height, background='#D3D3D3')

canvas.create_rectangle(230, 10, 290, 60,
    outline="#f11", fill="#1f1", width=2)

canvas.pack()

fenetre.mainloop()

test = Grid()

test.set_interaction_points()
test.print_grid()








# while True:

    # grid.update_odour()
    # ant.update_position()
    # grid.check_interaction_point()