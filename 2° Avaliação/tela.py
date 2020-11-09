from tkinter import *
import tkinter


class Application:
    def __init__(self, master=None):

        self.fontePadrao = ("Arial", "10")

        # Container do Titul #
        self.Cont1 = Frame(master)
        self.Cont1["pady"] = 10
        self.Cont1.pack()

        self.titulo = Label(self.Cont1, text="Monitoramento de dados")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        # Container do Disco #
        self.Cont2 = Frame(master)
        self.Cont2["pady"] = 10
        self.Cont2.pack()

        self.discoIdLabel = Label(
            self.Cont2, text="Id Disco", font=self.fontePadrao)
        self.discoIdLabel.pack(side=LEFT)

        self.discoIdTxt = Entry(self.Cont2)
        self.discoIdTxt["width"] = 10
        self.discoIdTxt["font"] = self.fontePadrao
        self.discoIdTxt.pack(side=LEFT)

        # Container de botões

        self.botao = Frame(master)
        self.botao["pady"] = 10
        self.botao.pack()

        self.sair = Button(self.botao)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "10")
        self.sair["width"] = 5
        self.sair["command"] = self.botao.quit
        self.sair.pack()

        self.maiorRam = Button(self.botao)
        self.maiorRam["text"] = "Maior RAM"
        self.maiorRam["font"] = ("Calibri", "10")
        self.maiorRam["width"] = 15
        self.maiorRam.pack(side=RIGHT)

        self.menorRam = Button(self.botao)
        self.menorRam["text"] = "Menor RAM" 
        self.menorRam["font"] = ("Calibri", "10")
        self.menorRam["width"] = 15
        self.menorRam.pack(side=RIGHT)

root = Tk()


Application(root)
root.mainloop()
