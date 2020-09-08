import mysql.connector
import time
import psutil
import datetime
import platform
import os 
from mysql.connector import Error


try:
    connection = mysql.connector.connect(host='localhost', database='python2', user='root', password='30252115')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:

    plat = platform
    discoG = psutil.disk_usage('G://')
    discoC = psutil.disk_usage('C://')
    discoE = psutil.disk_usage('E://')

    cursor = connection.cursor(prepared=True)

    insertDisco = """insert into disco (nome,espaco_total)
        values (%s,%s);"""
    valor_usadoG = round(discoG.used / (1024.0 ** 3),2)
    valor_livreG = round(discoG.free / (1024.0 ** 3),2)
    valor_usadoC = round(discoC.used / (1024.0 ** 3),2)
    valor_livreC = round(discoC.free / (1024.0 ** 3),2)
    valor_usadoE = round(discoE.used / (1024.0 ** 3),2)
    valor_livreE = round(discoE.free / (1024.0 ** 3),2)
    
    cursor.execute(insertDisco, ("G://",(valor_livreG + valor_usadoG)))
    cursor.execute(insertDisco, ("C://",(valor_livreC + valor_usadoC)))
    cursor.execute(insertDisco, ("E://",(valor_livreE + valor_usadoE)))

    insertPython = """insert into python (versao,instalado)
        values (%s,%s);"""
    if (plat.python_version() is None):
        instalado = False
    else:
        instalado = True 
    versao = plat.python_version()
    cursor.execute(insertPython, (versao,instalado))   

    insertSistema = """insert into sistema (nome)
        values (%s);"""
    sistema = plat.system()
    cursor.execute(insertSistema,("teste"))

    insertMaquina = """insert into maquina (nome,processador)
        values (%s,%s);"""
    nome = plat.node()
    processador = plat.processor()
    cursor.execute(insertMaquina,(nome,processador))