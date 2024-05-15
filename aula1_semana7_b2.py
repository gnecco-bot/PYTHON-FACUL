# Necessario criar um objeto para iterar
# Metodos do tkinter:
# Tk = cria uma janela
# Label = cria um texto na janela
# Pack = forma diretiva de posicionar elementos na janela
# Photoimage = adiciona uma imagem a janela
# subsample compacta a imagem a um tamanho desejado
# side = local que deve ser inserido na janela
# TOP = parte de cima da janela
# BOTTOM = parte de baixo da janela
# mainloop = chama o loop da janela para inicializar
# grid = divide a janela em grade para locação de determinados locais

from tkinter import Tk, Label, PhotoImage, TOP, BOTTOM, RAISED

root = Tk()
photo = PhotoImage(file='5eeea355389655.59822ff824b72.gif').subsample(1)
imagem = Label(master=root, image=photo)
hello = Label(master=root, text='Olá classe!', font=("courier", 18))
imagem.pack(side=TOP)
hello.pack(side=BOTTOM)
root.mainloop()

# JANEAL CALCULADORA (apenas interface)
#
# root = Tk()
# labels = [['1','2','3'],
#           ['4','5','6'],
#           ['7','8','9'],
#           ['*','0','#']]

# for r in range(4):
#     for c in range(3):
#         label = Label(root, relief=RAISED, padx=20, text=labels[r][c])
#         label.grid(row=r, column=c)
# root.mainloop()