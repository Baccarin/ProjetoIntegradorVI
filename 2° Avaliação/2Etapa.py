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
    
    while True:
        cursor = connection.cursor(prepared=True)

        # Busca e retorna o id do disco
        #cursor.execute("select id from disco where nome like 'G://' ")
        #discoGid = cursor.fetchone()

        #cursor.execute("select id from disco where nome like 'C://' ")
        #discoCid = cursor.fetchone()

        #cursor.execute("select id from disco where nome like 'E://' ")
        #discoEid = cursor.fetchone()


        print(p.username())
        print(p.cwd())

        #print(discoGid,discoCid,discoEid)
        #connection.commit()
        time.sleep(50)
