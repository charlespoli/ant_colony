from tkinter import * 

fenetre = Tk()
fenetre.geometry("1200x800")
fenetre.resizable(0, 0)

width = 1200
height = 800
canvas = Canvas(fenetre, width=width, height=height, background='#D3D3D3')
ligne1 = canvas.create_line(width/2, 0, width/2, height)
ligne2 = canvas.create_line(0, height/2, width, height/2)
txt = canvas.create_text(width/2, height/2, text="Cible", font="Arial 16 "
    "italic", fill="blue")
canvas.pack()

fenetre.mainloop()
