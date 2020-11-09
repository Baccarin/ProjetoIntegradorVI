from tkinter import *
import tkinter
import mysql.connector
from mysql.connector import Error
import leitura as leitura


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
                leitura.iniciar()


        def maiorUsoRam(self):
            maiorUsoRAM = "select * from leitura order by ram_livre_percentual limit 1;"
            cursor.execute(maiorUsoRAM)
            return maiorUsoRAM

        def menorUsoRam(self):
            menorUsoRAM = "select * from leitura order by ram_livre_percentual desc limit 1;"
            cursor.execute(menorUsoRAM)
            return menorUsoRAM

        def __init__(self, master=None):

            self.fontePadrao = ("Arial", "10")

            # Container do Titulo #
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

            self.discoIdLabel = Label(self.Cont2, text="Id Disco", font=self.fontePadrao)
            self.discoIdLabel.pack(side=LEFT, padx= 14)

            self.discoIdTxt = Entry(self.Cont2)
            self.discoIdTxt["width"] = 10
            self.discoIdTxt["font"] = self.fontePadrao
            self.discoIdTxt.pack(side=LEFT, padx= 10)

            self.discoNomeLabel = Label(self.Cont2, text="Nome Disco", font=self.fontePadrao)
            self.discoNomeLabel.pack(side=LEFT)

            self.discoNomeTxt = Entry(self.Cont2)
            self.discoNomeTxt["width"] = 10
            self.discoNomeTxt["font"] = self.fontePadrao
            self.discoNomeTxt.pack(side=LEFT)

            # Container do Disco #
            self.Cont3 = Frame(master)
            self.Cont3["pady"] = 10

            self.Cont3.pack()

            self.dtaInicio = Label(self.Cont3, text="Data Inicio", font=self.fontePadrao)
            self.dtaInicio.pack(side=LEFT, padx= 10)

            self.dtaInicioTxt = Entry(self.Cont3)
            self.dtaInicioTxt["width"] = 10
            self.dtaInicioTxt["font"] = self.fontePadrao
            self.dtaInicioTxt.pack(side=LEFT)

            self.dtaFimLabel = Label(self.Cont3, text="Data Fim", font=self.fontePadrao)
            self.dtaFimLabel.pack(side=LEFT, padx= 14)

            self.dtaFimTxt = Entry(self.Cont3)
            self.dtaFimTxt["width"] = 10
            self.dtaFimTxt["font"] = self.fontePadrao
            self.dtaFimTxt.pack(side=LEFT)

            # Container de botões

            self.botao = Frame(master)
            self.botao["pady"] = 10
            self.botao.pack()

            self.maiorRam = Button(self.botao)
            self.maiorRam["text"] = "Maior RAM"
            self.maiorRam["font"] = ("Calibri", "10")
            self.maiorRam["width"] = 15
            self.maiorRam.pack()

            self.menorRam = Button(self.botao)
            self.menorRam["text"] = "Menor RAM"
            self.menorRam["font"] = ("Calibri", "10")
            self.menorRam["width"] = 15
            self.menorRam.pack()

            self.leitura = Button(self.botao,command = )
            self.leitura["text"] = "Leitura"
            self.leitura["font"] = ("Calibri", "10")
            self.leitura["width"] = 15
            self.sair["command"] = self.botao.quit
            self.leitura.pack()

            self.excluir = Button(self.botao)
            self.excluir["text"] = "Excluir"
            self.excluir["font"] = ("Calibri", "10")
            self.excluir["width"] = 15
            self.excluir.pack()

            self.sair = Button(self.botao)
            self.sair["text"] = "Sair"
            self.sair["font"] = ("Calibri", "10")
            self.sair["width"] = 5
            self.sair["command"] = self.botao.quit
            self.sair.pack(side=BOTTOM)
            self.sair.pack()


root = Tk()


Application(root)
root.mainloop()
