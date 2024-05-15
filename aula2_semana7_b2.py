# evento = eventos são ações que são tomadas para determinar ações
# showinfo = mostra uma mensagem de aviso na tela
# button = adiciona um botão a janela
# command = funcao que o button terá
# strftime = converte % com suas respectivas letras em data e hora
# localtime = converse os valores da strftime no horario atual
# Entry = recebe um valor
# bind = tratar eventos de teclas apertadas para determinadas funcoes

from tkinter import Tk, Button, Label, Entry
from tkinter.messagebox import showinfo
from time import strftime, localtime, strptime

# Mostra data e hora atual ao clicar no botão
#
# def clicked():
#     time = strftime('Day: %d %b %y\nTime: %H:%M:%S%p\n', localtime())
#     showinfo(message=time)

    
# button = Button(root, text='Clique', command=clicked)
# button.pack()
# root.mainloop()

# def clicked():
#     global entry
#     date = entry.get()
#     weekday = strftime('%A', strptime(date, '%b %d, %Y'))
#     showinfo(message='{} foi um {}'.format(date, weekday))


# root = Tk()
# label = Label(root, text='Digite uma data:')
# label.grid(row=0, column=0) # row = linha // column = coluna
# entry = Entry(root)
# entry.grid(row=0, column=1)
# button = Button(root, text='Clique', command=clicked)
# button.grid(row=1, column=0, columnspan=2)
# root.mainloop()

# Mostra eventos(teclas/mouse) que pressionou
#
from tkinter import Tk, Text, BOTH

def key_pressed(event):
    print('char: {}'.format(event.keysym))

def mouse_clicked_left(event):
    print('mouse left clicked')

def mouse_clicked_right(event):
    print('mouse right clicked')

root = Tk()
text = Text(root, width=20, height='5')
text.bind('<KeyPress>', key_pressed)
text.bind('<Button-1>', mouse_clicked_left)
text.bind('<Button-3>', mouse_clicked_right)
text.pack(expand=True, fill=BOTH)
root.mainloop()