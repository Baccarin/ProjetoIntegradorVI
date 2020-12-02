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
        self.discoNomeLabel.pack(side=LEFT, padx=14)
        
        self.discoNomeTxt = Entry(self.contDisco ,width = 10, font=self.fontePadrao)
        self.discoNomeTxt.pack(side=LEFT, padx=10)
        

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

        self.contAviso = Frame(master,pady=10)
        self.contAviso.pack()

        self.aviso = Label(self.contAviso, text="  ",width = 100, font=self.fontePadrao)
        self.aviso.pack(side=BOTTOM)

    def plot_botoes(self, master=None):
        #Função que define o estilo, posição e ações referente aos botôes de plot (gráficos)
        self.botao = Frame(master)
        self.botao["pady"] = 10
        self.botao.pack()

        self.plot_E = Button(self.botao,bg='blue') #bg >> define a cor do elemento
        self.plot_E["text"] = "HD (E:)" #define o conteudo do elemento na tela
        self.plot_E["font"] = ("Calibri", "10") #define a fonte e o tamanho da mesma
        self.plot_E["width"] = 15 #tamanho do elemento
        self.plot_E["command"] = leitura.bt_plot_HD_E #define uma ação ao botão ser clicado
        self.plot_E.pack(side=RIGHT) #posição do componente

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

        self.plot_botoes() #chama a função que define e inicia os botões referente aos gráficos

        self.botao = Frame(master,pady=10)
        self.botao.pack()

        self.leitura = Button(self.botao,text="Leitura",
         font=self.fontePadrao,width=15,command=leitura.bt_iniciarLeitura) #define nome, conteudo, fonte ,tamanho e ação do botão
        self.leitura.pack(side=RIGHT)

        self.leituraUnica = Button(self.botao,text="Leitura Unica",
         font=self.fontePadrao,width=15,command=self.leituraUnicaTela) #define nome, conteudo, fonte ,tamanho e ação do botão
        self.leituraUnica.pack(side=RIGHT)

        self.teste = Button(self.botao,text="Print pelo Id", 
         font=self.fontePadrao,width=15, command = self.print_discoId) #
        self.teste.pack(side=RIGHT)

        self.teste = Button(self.botao,text="Print pelo nome",
         font=self.fontePadrao,width=15,command = self.print_discoNome) #printa com relação ao nome dado
        self.teste.pack(side=RIGHT)

        self.Data = Button(self.botao,bg='red',text = "Print pela data",
         font=self.fontePadrao,width = 15,command = self.print_Data) #print com delimitação de data
        self.Data.pack(side=RIGHT)

        self.sair = Button(self.botao,bg='red',text="Sair",
         font=self.fontePadrao,width=5,command=self.botao.quit) #botão que fecha a aplicação
        self.sair.pack(side = BOTTOM)

    def print_discoId(self):
        try:
        # Iniciada tentativa de conexão com o banco
            connection = mysql.connector.connect(
            # Informações da base de dados
            host='localhost', database='projetovi', user='user', password='123456',buffered = True)
            if connection.is_connected():
                cursor = connection.cursor()

        except Error as e:
            # Caso ocorra erro
            print("Não conectado", e)
        finally:
            try:
                self.aviso['text'] = ""
                discoId = int (self.discoIdTxt.get())
                print(discoId)
                if (discoId == 1):
                    select = "select nome,espaco_total from disco where id = 1  "
                    cursor.execute(select)
                    records = cursor.fetchall()
                    print(records)
                    self.aviso['text'] = records
                elif (discoId == 2):
                    select = "select nome,espaco_total from disco where id = 2  "    
                    cursor.execute(select)
                    records = cursor.fetchall()
                    print(records)
                    self.aviso['text'] = records
                elif (discoId == 3 ):
                    select = "select nome,espaco_total from disco where id = 3  " 
                    cursor.execute(select)
                    records = cursor.fetchall()
                    print(records)
                    self.aviso['text'] = records
                else:
                    if (discoId == ''):
                        self.aviso['text'] = "Preencha o campo do nome do disco. Tente novamente." 
                    else:
                        self.aviso['text'] = "Nenhum registro encontrado. Tente novamente."                                                       

            except ValueError:
                self.aviso['text'] = "Somente numeros sao aceitos. Tente novamente."

    def print_discoNome(self,master = None):
        try:
        # Iniciada tentativa de conexão com o banco
            connection = mysql.connector.connect(
            # Informações da base de dados
            host='localhost', database='projetovi', user='user', password='123456',buffered = True)
            if connection.is_connected():
                cursor = connection.cursor()
                cursor.execute("select database();")

        except Error as e:
            # Caso ocorra erro
            print("Não conectado", e)
        finally:
            self.aviso['text'] = ""
            discoNome = self.discoNomeTxt.get()
            print(discoNome)
            if (discoNome == 'E://'):
                select = "select id,nome,espaco_total from disco where nome like  'E://' "
                cursor.execute(select,discoNome)
                records = cursor.fetchall()
                print(records)
                self.aviso['text'] = records
            elif (discoNome == 'D://'):
                select = "select id,nome,espaco_total from disco where nome like  'D://' "
                cursor.execute(select,discoNome)
                records = cursor.fetchall()
                print(records)
                self.aviso['text'] = records
            elif (discoNome == 'C://'):
                select = "select id,nome,espaco_total from disco where nome like  'C://' "
                cursor.execute(select,discoNome)
                records = cursor.fetchall()
                print(records)
                self.aviso['text'] = records
            else:
                if (discoNome == ''):
                    self.aviso['text'] = "Preencha o campo do nome do disco. Tente novamente." 
                else:
                    self.aviso['text'] = "Nenhum registro encontrado. Tente novamente."  

    def __init__(self, master=None):

        self.init_label() #inicia labels
        self.init_botoes() #inicia botoes

    def print_Data(self):
        dtInicio = self.dtaInicioTxt.get()
        dtFim = self.dtaFimTxt.get()
        if (dtFim == '' or dtInicio == ''):
            self.aviso['text'] = "Preencha as duas datas. Tente novamente."
        else:
            try:
                # Iniciada tentativa de conexão com o banco
                connection = mysql.connector.connect(
                    # Informações da base de dados
                host='localhost', database='projetovi', user='user', password='123456',buffered = True)
                if connection.is_connected():
                    cursor = connection.cursor()
                    cursor.execute("select database();")

            except Error as e:
                    # Caso ocorra erro
                print("Não conectado", e)
            finally:
                select = "select # from leitura where dta_leitura between %s and %s"
                cursor.execute(select,(dtInicio,dtFim))
                records = cursor.fetchall()
                print(records)
                self.aviso['text'] = records
            
    def leituraUnicaTela (self):
        leitura.bt_iniciarLeituraUnica()
        self.aviso['text'] = "Finalizada leitura única." 

root = Tk()
root.geometry('700x400')


Application(root)
root.mainloop()
