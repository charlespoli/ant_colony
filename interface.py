from tkinter import * 
from grid import Grid


fenetre = Tk()
fenetre.geometry("1200x800")
fenetre.resizable(0, 0)

width = 1200
height = 800
canvas = Canvas(fenetre, width=width, height=height, background='#D3D3D3')
ligne1 = canvas.create_line(width/2, 0, width/2, height)
ligne2 = canvas.create_line(0, height/2, width, height/2)


image = PhotoImage(file="ant.png")

canvas.create_image(0, 0, anchor=NW, image=image)
canvas.pack()

fenetre.mainloop()

grid = Grid(3,3)

grid.set_interaction_points()

print(grid.grid)




while True:

    grid.update_odour()
    ant.update_position()
    grid.check_interaction_point()