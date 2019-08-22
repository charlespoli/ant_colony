from random import randint
from time import sleep
from ant import *
from grid import *

window = Tk()
# window.geometry()
# window.resizable(0, 0)

test_grid = Grid()

test_grid.set_interaction_points()
test_grid.print_grid()

canvas = Canvas(window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, background='#D3D3D3')
canvas.pack()

for i in range(20):
    Ant(randint(0, GRID_WIDTH - 1), randint(0, GRID_HEIGHT - 1), canvas)

test_grid.draw_grid(canvas)

for i in range(200):
    for ant in Ant.List:
        ant.update_position()
        canvas.update()
    sleep(0.1)

window.mainloop()
# while True:

# grid.update_odour()
# ant.update_position()
# grid.check_interaction_point()
