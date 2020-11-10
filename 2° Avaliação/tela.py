from tkinter import *
import tkinter
import mysql.connector
from mysql.connector import Error
import Leitura as leitura
#import BotoesAcoes as acoes


class Application:

    def iniciarLeitura(self):
        try:
            # Iniciada tentativa de conexão com o banco
            connection = mysql.connector.connect(
                # Informações da base de dados
                host='localhost', database='projetovi', user='root', password='123456')
            if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Conectado a MySQL Server versão ", db_Info)
                cursor = connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                print("Base conectada: ", record)

        except Error as e:
            # Caso ocorra erro
            print("Não conectado", e)

        finally:
            print("")

    def plot_botoes(self, master=None):

        self.botao = Frame(master)
        self.botao["pady"] = 10
        self.botao.pack()

        self.plot_E = Button(self.botao,bg='blue')
        self.plot_E["text"] = "HD (E:)"
        self.plot_E["font"] = ("Calibri", "10")
        self.plot_E["width"] = 15
        self.plot_E["command"] = leitura.bt_plot_HD_E
        self.plot_E.pack(side=RIGHT)

        self.plot_D = Button(self.botao,bg='yellow')
        self.plot_D["text"] = "HD (D:)"
        self.plot_D["font"] = ("Calibri", "10")
        self.plot_D["width"] = 15
        self.plot_D["command"] = leitura.bt_plot_HD_D
        self.plot_D.pack(side=RIGHT)

        self.plot_C = Button(self.botao,bg='green')
        self.plot_C["text"] = "HD (C:)"
        self.plot_C["font"] = ("Calibri", "10")
        self.plot_C["width"] = 15
        self.plot_C["command"] = leitura.bt_plot_HD_C
        self.plot_C.pack(side=RIGHT)

        self.RAM = Button(self.botao,bg='pink')
        self.RAM["text"] = "RAM"
        self.RAM["font"] = ("Calibri", "10")
        self.RAM["width"] = 15
        self.RAM["command"] = leitura.bt_plot_RAM
        self.RAM.pack(side=RIGHT)

    def init_botoes(self, master=None):

        self.plot_botoes()

        self.botao = Frame(master,pady=10)
        self.botao.pack()

        self.leitura = Button(self.botao,text="Leitura",
         font=self.fontePadrao,width=15,command=leitura.bt_iniciarLeitura)
        self.leitura.pack(side=RIGHT)

        self.teste = Button(self.botao,text="Teste",
         font=self.fontePadrao,width=15)
        self.teste["command"] = leitura.bt_iniciarLeitura
        self.teste.pack(side=RIGHT)

        self.sair = Button(self.botao,bg='red',text="Sair",
         font=self.fontePadrao,width=5,command=self.botao.quit)
        self.sair.pack()

    def init_label(self, master=None):

        self.fontePadrao = ("Arial", "10")

        # Container do Titulo #
        self.contTitulo = Frame(master,pady=10)
        self.contTitulo.pack()

        self.titulo = Label(self.contTitulo, text="Monitoramento de dados", font=self.fontePadrao)
        self.titulo.pack()

        # Container do Disco #
        self.contDisco = Frame(master,pady=10)
        self.contDisco.pack()

        self.discoIdLabel = Label(self.contDisco, text="Id Disco", font=self.fontePadrao)
        self.discoIdLabel.pack(side=LEFT, padx=14)

        self.discoIdTxt = Entry(self.contDisco ,width = 10, font=self.fontePadrao)
        self.discoIdTxt.pack(side=LEFT, padx=10)

        self.discoNomeLabel = Label(self.contDisco, text="Nome Disco", font=self.fontePadrao)
        self.discoNomeLabel.pack(side=LEFT)

        self.discoNomeTxt = Entry(self.contDisco,width = 10, font=self.fontePadrao)
        self.discoNomeTxt.pack(side=LEFT)

        # Container do Data #
        self.contData = Frame(master,pady=10)
        self.contData.pack()

        self.dtaInicio = Label(self.contData, text="Data Inicio", font=self.fontePadrao)
        self.dtaInicio.pack(side=LEFT, padx=10)

        self.dtaInicioTxt = Entry(self.contData,width = 10, font=self.fontePadrao)
        self.dtaInicioTxt.pack(side=LEFT)

        self.dtaFimLabel = Label(self.contData, text="Data Fim", font=self.fontePadrao)
        self.dtaFimLabel.pack(side=LEFT, padx=14)

        self.dtaFimTxt = Entry(self.contData,width = 10, font=self.fontePadrao)
        self.dtaFimTxt.pack(side=LEFT)

    def __init__(self, master=None):

        self.init_label()
        self.init_botoes()




root = Tk()
root.geometry('600x400')


Application(root)
root.mainloop()
