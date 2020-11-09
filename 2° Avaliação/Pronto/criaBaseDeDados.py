import mysql.connector
import psutil
from mysql.connector import Error


def insertDados(base, senha):
    try:
        # Iniciada tentativa de conexão com o banco
        connection = mysql.connector.connect(
            # Informações da base de dados
            host='localhost', database=base, user='root', password=senha)
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
        insert = """
            insert into disco (nome, espaco_total)
            values('C://', 223.00),('D://', 111.00),('E://', 931.00);"""
        cursor.execute(insert)
        print('Insert do disco')

        connection.commit()
        connection.close()


def createTables(base, senha):
    try:
        # Iniciada tentativa de conexão com o banco
        connection = mysql.connector.connect(
            # Informações da base de dados
            host='localhost', database=base, user='user', password=senha)
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
        createTable = """
			create table if not exists disco (
				id int auto_increment primary key,
				nome varchar (200) not null,
				espaco_total float not null,
                CONSTRAINT u_nome UNIQUE (nome)
            );"""
        cursor.execute(createTable)
        print('Insert disco')

        createLeitura = """
		    create table if not exists leitura(
				id int auto_increment primary key,
				id_disco int not null,
				valor_usado float not null,
				valor_livre_percentual float not null,
				ram_livre float not null,
				ram_livre_percentual float not null,
				dta_leitura TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
				FOREIGN KEY(id_disco) REFERENCES disco(id)
		); """
        cursor.execute(createLeitura)
        print('Criada tabela leitura')

        connection.commit()
        connection.close()
