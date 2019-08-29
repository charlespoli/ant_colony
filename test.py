from random import randint
from time import sleep
from ant import *
from grid import *
from constant import *

window = Tk()
# window.geometry()
# window.resizable(0, 0)

canvas = Canvas(window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, background='#D3D3D3')
canvas.pack()

test_grid = Grid(canvas)

test_grid.set_interaction_points()
test_grid.print_grid()


for i in range(1):
    Ant(randint(0, GRID_WIDTH - 1), randint(0, GRID_HEIGHT - 1),
        test_grid, canvas)

test_grid.draw_grid(canvas)

for i in range(2000):
    test_grid.draw_odours(canvas)
    test_grid.update_odour()
    for ant in Ant.List:
        ant.leave_odour()
        ant.ant_movement()
    canvas.update()
    print('tick')
    sleep(0.1)

window.mainloop()

