import mysql.connector
import time
import psutil
import datetime
from mysql.connector import Error
import matplotlib.pyplot as plt


def bt_plot_RAM():
    try:
        # Iniciada tentativa de conexão com o banco
        connection = mysql.connector.connect(
            # Informações da base de dados
            host='localhost', database='projetovi', user='user', password='123456')
        if connection.is_connected():
            cursor = connection.cursor()

    except Error as e:
        # Caso ocorra erro
        print("Não conectado", e)
    finally:
        cursor.execute("select ram_livre from leitura ")
        maiorRam = cursor.fetchall()
        plt.plot(maiorRam)
        plt.ylabel('Uso da memória RAM (%)')
        plt.xlabel('Número da leitura')
        plt.show()

def bt_plot_HD_D():
    try:
        # Iniciada tentativa de conexão com o banco
        connection = mysql.connector.connect(
            # Informações da base de dados
            host='localhost', database='projetovi', user='user', password='123456')
        if connection.is_connected():
            cursor = connection.cursor()


    except Error as e:
        # Caso ocorra erro
        print("Não conectado", e)
    finally:
        cursor.execute("select l.valor_usado from disco d left join leitura l on l.id_disco = d.id  where d.nome like 'D://' ")
        valorHdD = cursor.fetchall()
        plt.plot(valorHdD,'y--')
        plt.ylabel('Ocupação do disco D') 
        plt.xlabel('Número da leitura')
        plt.title("Gráfico Disco D:")
        
        plt.show()

def bt_plot_HD_C():
    try:
        # Iniciada tentativa de conexão com o banco
        connection = mysql.connector.connect(
            # Informações da base de dados
            host='localhost', database='projetovi', user='user', password='123456')
        if connection.is_connected():
            cursor = connection.cursor()


    except Error as e:
        # Caso ocorra erro
        print("Não conectado", e)
    finally:
        cursor.execute("select l.valor_usado from disco d left join leitura l on l.id_disco = d.id  where d.nome like 'C://' ")
        valorHdC = cursor.fetchall()
        plt.plot(valorHdC,'g--')
        plt.ylabel('Ocupação do disco C') 
        plt.xlabel('Número da leitura')
        plt.title("Gráfico Disco C:")
        plt.show()

def bt_plot_HD_E():
    try:
        # Iniciada tentativa de conexão com o banco
        connection = mysql.connector.connect(
            # Informações da base de dados
            host='localhost', database='projetovi', user='user', password='123456')
        if connection.is_connected():
            cursor = connection.cursor()


    except Error as e:
        # Caso ocorra erro
        print("Não conectado", e)
    finally:
        cursor.execute("select l.valor_usado from disco d left join leitura l on l.id_disco = d.id  where d.nome like 'E://' ")
        valorHdE = cursor.fetchall()
        plt.plot(valorHdE,'b--')
        plt.ylabel('Ocupação do disco E') 
        plt.xlabel('Número da leitura')
        plt.title("Gráfico Disco E:")
        plt.show()

def iniciarLeitura():
    try:
        # Iniciada tentativa de conexão com o banco
        connection = mysql.connector.connect(
            # Informações da base de dados
            host='localhost', database='projetovi', user='user', password='123456')
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

        # Busca e retorna o id do disco
        cursor.execute("select id from disco where nome like 'D://' ")
        discoGid = cursor.fetchone()
        print('Id do disco D:// :', discoGid[0])

        cursor.execute("select id from disco where nome like 'C://' ")
        discoCid = cursor.fetchone()
        print('Id do disco C:// :',discoCid[0])

        cursor.execute("select id from disco where nome like 'E://' ")
        discoEid = cursor.fetchone()
        print('Id do disco E:// :',discoEid[0])

        quantidade = 1
        while True:
            cursor = connection.cursor(prepared=True)

            discoD = psutil.disk_usage('D://')
            discoC = psutil.disk_usage('C://')
            discoE = psutil.disk_usage('E://')
            ram = psutil.virtual_memory()

            cursor = connection.cursor(prepared=True)
            # Texto base do insert na base de dados
            insert = """insert into leitura (id_disco,valor_usado,valor_livre_percentual,ram_livre,ram_livre_percentual)
                values (%s,%s,%s,%s,%s);"""

            valor_usadoD = round(discoD.used / (1024.0 ** 3), 2)
            valor_livre_percentualD = discoD.percent

            valor_usadoC = round(discoC.used / (1024.0 ** 3), 2)
            valor_livre_percentualC = discoC.percent

            valor_usadoE = round(discoE.used / (1024.0 ** 3), 2)
            valor_livre_percentualE = discoE.percent

            ram_livre = round(ram.percent, 2)
            ram_livre_percentual = round(ram.available * 100 / ram.total, 2)

            # Executando os inserts na base de dados
            cursor.execute(insert, (discoGid[0], valor_usadoD,
                                    valor_livre_percentualD, ram_livre, ram_livre_percentual))
            cursor.execute(insert, (discoCid[0], valor_usadoC,
                                    valor_livre_percentualC, ram_livre, ram_livre_percentual))
            cursor.execute(insert, (discoEid[0], valor_usadoE,
                                    valor_livre_percentualE, ram_livre, ram_livre_percentual))

            connection.commit()
            print('Leitura número: ' ,quantidade)
            quantidade = quantidade + 1

            time.sleep(5)

def bt_iniciarLeitura():
    try:
        # Iniciada tentativa de conexão com o banco
        connection = mysql.connector.connect(
            # Informações da base de dados
            host='localhost', database='projetovi', user='user', password='123456')
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

        # Busca e retorna o id do disco
        cursor.execute("select id from disco where nome like 'D://' ")
        discoGid = cursor.fetchone()

        cursor.execute("select id from disco where nome like 'C://' ")
        discoCid = cursor.fetchone()

        cursor.execute("select id from disco where nome like 'E://' ")
        discoEid = cursor.fetchone()

        quantidade = 1
        while quantidade < 2:
            cursor = connection.cursor(prepared=True)

            discoD = psutil.disk_usage('D://')
            discoC = psutil.disk_usage('C://')
            discoE = psutil.disk_usage('E://')
            ram = psutil.virtual_memory()

            cursor = connection.cursor(prepared=True)
            # Texto base do insert na base de dados
            insert = """insert into leitura (id_disco,valor_usado,valor_livre_percentual,ram_livre,ram_livre_percentual)
                values (%s,%s,%s,%s,%s);"""

            valor_usadoD = round(discoD.used / (1024.0 ** 3), 2)
            valor_livre_percentualD = discoD.percent

            valor_usadoC = round(discoC.used / (1024.0 ** 3), 2)
            valor_livre_percentualC = discoC.percent

            valor_usadoE = round(discoE.used / (1024.0 ** 3), 2)
            valor_livre_percentualE = discoE.percent

            ram_livre = round(ram.percent, 2)
            ram_livre_percentual = round(ram.available * 100 / ram.total, 2)

            # Executando os inserts na base de dados
            cursor.execute(insert, (discoGid[0], valor_usadoD,
                                    valor_livre_percentualD, ram_livre, ram_livre_percentual))
            cursor.execute(insert, (discoCid[0], valor_usadoC,
                                    valor_livre_percentualC, ram_livre, ram_livre_percentual))
            cursor.execute(insert, (discoEid[0], valor_usadoE,
                                    valor_livre_percentualE, ram_livre, ram_livre_percentual))

            connection.commit()
            quantidade = quantidade + 1

            time.sleep(5)

def bt_iniciarLeituraUnica():
    try:
        # Iniciada tentativa de conexão com o banco
        connection = mysql.connector.connect(
            # Informações da base de dados
            host='localhost', database='projetovi', user='user', password='123456')
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

        # Busca e retorna o id do disco
        cursor.execute("select id from disco where nome like 'D://' ")
        discoGid = cursor.fetchone()

        cursor.execute("select id from disco where nome like 'C://' ")
        discoCid = cursor.fetchone()

        cursor.execute("select id from disco where nome like 'E://' ")
        discoEid = cursor.fetchone()

        cursor = connection.cursor(prepared=True)

        discoD = psutil.disk_usage('D://')
        discoC = psutil.disk_usage('C://')
        discoE = psutil.disk_usage('E://')
        ram = psutil.virtual_memory()

        cursor = connection.cursor(prepared=True)
        # Texto base do insert na base de dados
        insert = """insert into leitura (id_disco,valor_usado,valor_livre_percentual,ram_livre,ram_livre_percentual)
                values (%s,%s,%s,%s,%s);"""

        valor_usadoD = round(discoD.used / (1024.0 ** 3), 2)
        valor_livre_percentualD = discoD.percent

        valor_usadoC = round(discoC.used / (1024.0 ** 3), 2)
        valor_livre_percentualC = discoC.percent

        valor_usadoE = round(discoE.used / (1024.0 ** 3), 2)
        valor_livre_percentualE = discoE.percent

        ram_livre = round(ram.percent, 2)
        ram_livre_percentual = round(ram.available * 100 / ram.total, 2)

        # Executando os inserts na base de dados
        cursor.execute(insert, (discoGid[0], valor_usadoD,
                                    valor_livre_percentualD, ram_livre, ram_livre_percentual))
        cursor.execute(insert, (discoCid[0], valor_usadoC,
                                    valor_livre_percentualC, ram_livre, ram_livre_percentual))
        cursor.execute(insert, (discoEid[0], valor_usadoE,
                                    valor_livre_percentualE, ram_livre, ram_livre_percentual))

        connection.commit()




            
