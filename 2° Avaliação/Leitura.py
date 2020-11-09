import mysql.connector
import time
import psutil
import datetime
from mysql.connector import Error

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

    p = psutil.Process()
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

        time.sleep(50)
