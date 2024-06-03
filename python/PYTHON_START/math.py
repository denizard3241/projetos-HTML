from tkinter import *


def funcClicar():
    print("TE AMO TE AMO")


janelaPrincipal = Tk()
texto = Label(master=janelaPrincipal, text="Te amo laryssa!")
texto.pack()

# Nota: Para usar PhotoImage, você precisa especificar o caminho de um arquivo de imagem válido
# Substitua "caminho/para/o/arquivo.png" pelo caminho real do arquivo de imagem
pic = PhotoImage(file="D:/python/download.png")

logo = Label(master=janelaPrincipal, image=pic)
logo.pack()

botao = Button(master=janelaPrincipal,
               text='Clique para ganhar corações <3', command=funcClicar)
botao.pack()

janelaPrincipal.mainloop()
