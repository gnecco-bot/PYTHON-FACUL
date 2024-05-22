from tkinter import Tk, Label, PhotoImage, RIDGE, GROOVE, Canvas

root = Tk()
gatoimagem = PhotoImage(file='5eeea355389655.59822ff824b72.gif')
objgato = Label(root, relief=RIDGE, image=gatoimagem)
objgato.pack(side='left')
text = Label(root, text='steam poweredby')
text.pack(side='top')
pixelimagem = PhotoImage(file='5eeea355389655.59822ff824b72.gif')
objpixel = Label(root, relief=GROOVE, image=pixelimagem)
objpixel.pack(side='right')
root.mainloop()

### DENHOS CANVAS ###
#
# def begin(event):
#     global oldx, oldy
#     oldx, oldy = event.x, event.y

# def draw(event):
#     global oldx, oldy, canvas
#     newx, newy = event.x, event.y
#     canvas.create_line(oldx, oldy, newx, newy)
#     oldx, oldy = newx, newy

# raiz = Tk()
# oldx, oldy = 0, 0
# canvas = Canvas(raiz, height=720, width=1280)
# canvas.bind("<Button-1>", begin)
# canvas.bind("<Button1-Motion>", draw)
# canvas.pack()
# raiz.mainloop()
