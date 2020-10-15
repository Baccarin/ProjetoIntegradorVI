import mysql.connector
import time
import psutil
import datetime
from mysql.connector import Error

try:
    # Iniciada tentativa de conexão com o banco
    connection = mysql.connector.connect(
        # Informações da base de dados
        host='localhost', database='python', user='root', password='30252115')
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

    discoG = psutil.disk_usage('G://')
    discoC = psutil.disk_usage('C://')
    discoE = psutil.disk_usage('E://')
    swap = psutil.swap_memory()
    ram = psutil.virtual_memory()

    cursor = connection.cursor(prepared=True)
    # Texto base do insert na base de dados
    insert = """insert into leitura (id_disco,valor_usado,valor_livre,valor_livre_percentual,
                                        swap_percentual,ram_livre,ram_livre_percentual)
        values (%s,%s,%s,%s,%s,%s,%s);"""

    valor_usadoG = round(discoG.used / (1024.0 ** 3), 2)
    valor_livreG = round(discoG.free / (1024.0 ** 3), 2)
    valor_livre_percentualG = discoG.percent

    valor_usadoC = round(discoC.used / (1024.0 ** 3), 2)
    valor_livreC = round(discoC.free / (1024.0 ** 3), 2)
    valor_livre_percentualC = discoC.percent

    valor_usadoE = round(discoE.used / (1024.0 ** 3), 2)
    valor_livreE = round(discoE.free / (1024.0 ** 3), 2)
    valor_livre_percentualE = discoE.percent

    swap_percentual = round(swap.percent, 2)
    ram_livre = round(ram.percent, 2)
    ram_livre_percentual = round(ram.available * 100 / ram.total, 2)

    # Executando os inserts na base de dados
    cursor.execute(insert, (1, valor_usadoG, valor_livreG,
                            valor_livre_percentualG, swap_percentual, ram_livre, ram_livre_percentual))
    cursor.execute(insert, (2, valor_usadoC, valor_livreC,
                            valor_livre_percentualC, swap_percentual, ram_livre, ram_livre_percentual))
    cursor.execute(insert, (3, valor_usadoE, valor_livreE,
                            valor_livre_percentualE, swap_percentual, ram_livre, ram_livre_percentual))

    cursor.execute("select nome,espaco_total from disco")

    for (nome, espaco_total) in cursor.fetchall():
        print(nome, espaco_total)
