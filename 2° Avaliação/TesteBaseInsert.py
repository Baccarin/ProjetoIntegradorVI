import mysql.connector
from mysql.connector import Error
import criaBaseDeDados as base


try:
    #Iniciada tentativa de conexão com o banco
    connection = mysql.connector.connect(
        #Informações da base de dados
        host='localhost', database='projetovi', user='user', password='123456')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Conectado a MySQL Server versão ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Base conectada: ", record)

except Error as e:
    #Caso ocorra erro
    print("Não conectado", e)

finally:
    #Cria as tabelas, e rebece como parâmetro o nome da base e a senha do user 
    base.createTables('projetovi','123456')

    #Faz um insert de dados para verficicar se a base está criada
    base.insertDados('projetovi','123456')