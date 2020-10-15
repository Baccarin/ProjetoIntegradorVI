from tkinter import *
import tkinter


class Application:
    def __init__(self, master=None):

        self.fontePadrao = ("Arial", "10")

        # Container do Titul #
        self.Cont1 = Frame(master)
        self.Cont1["pady"] = 10
        self.Cont1.pack()

        self.titulo = Label(self.Cont1,
                            text="Monitoramento de dados")
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

        # Container do Usuário #
        self.Cont3 = Frame(master)
        self.Cont3["pady"] = 10
        self.Cont3.pack()

        self.userNomeLabel = Label(
            self.Cont3, text="Nome Usuário", font=self.fontePadrao)
        self.userNomeLabel.pack(side=LEFT)

        self.userNomeTxt = Entry(self.Cont3)
        self.userNomeTxt["width"] = 10
        self.userNomeTxt["font"] = self.fontePadrao
        self.userNomeTxt.pack(side=LEFT)

        self.userIdLabel = Label(
            self.Cont3, text="Id Usuário", font=self.fontePadrao)
        self.userIdLabel.pack(side=LEFT)

        self.userIdTxt = Entry(self.Cont3)
        self.userIdTxt["width"] = 10
        self.userIdTxt["font"] = self.fontePadrao
        self.userIdTxt.pack(side=RIGHT)

        # Container da Pasta #
        self.Cont4 = Frame(master)
        self.Cont4["pady"] = 10
        self.Cont4.pack()

        self.pastaNomeLabel = Label(
            self.Cont4, text="Nome da Pasta", font=self.fontePadrao)
        self.pastaNomeLabel.pack(side=LEFT)

        self.pastaNomeTxt = Entry(self.Cont4)
        self.pastaNomeTxt["width"] = 10
        self.pastaNomeTxt["font"] = self.fontePadrao
        self.pastaNomeTxt.pack(side=LEFT)

        self.pastaIdLabel = Label(
            self.Cont4, text="Id da Pasta", font=self.fontePadrao)
        self.pastaIdLabel.pack(side=LEFT)

        self.pastaIdTxt = Entry(self.Cont4)
        self.pastaIdTxt["width"] = 10
        self.pastaIdTxt["font"] = self.fontePadrao
        self.pastaIdTxt.pack(side=RIGHT)


root = Tk()
Application(root)
root.mainloop()
