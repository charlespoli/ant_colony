from tkinter import *
from grid import *
from constant import *
from ant import *
from random import randint
from time import sleep

fenetre = Tk()
fenetre.geometry("1200x800")
# fenetre.resizable(0, 0)

canvas = Canvas(fenetre, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, background='#D3D3D3')
canvas.pack()

test_grid = Grid()

test_grid.set_interaction_points()

test_grid.print_grid()

for i in range(20):
    Ant(randint(0, GRID_WIDTH - 1), randint(0, GRID_HEIGHT - 1), canvas)

test_grid.draw_grid(canvas)

for i in range(100):
    for ant in Ant.List:
        ant.update_position()
        canvas.update()
    sleep(1)

fenetre.mainloop()
# while True:

# grid.update_odour()
# ant.update_position()
# grid.check_interaction_point()
