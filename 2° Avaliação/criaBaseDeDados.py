import mysql.connector
from mysql.connector import Error


def createTables(base,senha):
    try:
        # Iniciada tentativa de conexão com o banco
        connection = mysql.connector.connect(
            # Informações da base de dados
            host='localhost', database=base, user='root', password=senha)
        if connection.is_connected():
            db_Info = connection.get_server_info()
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()

    except Error as e:
        # Caso ocorra erro
        print("Não conectado", e)

    finally:

        createTable = """
			create table if not exists disco (
				id int auto_increment primary key,
				nome varchar (200) not null,
				espaco_total float not null
			);"""
        cursor.execute(createTable)
        print('Criada tabela disco')

        createTable = """
		create table if not exists usuario (
				id int auto_increment primary key,
				nome varchar (200) not null unique,
				dta_primeiro_acesso TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
		);"""
        cursor.execute(createTable)
        print('Criada tabela usuario')

        createTable = """
		create table if not exists pasta(
				id int auto_increment primary key,
				diretorio varchar (500) not null,
				quantidadeLeituras int check(quantidadeLeituras > 0)
		);"""
        cursor.execute(createTable)
        print('Criada tabela pasta')

        createTable = """
		create table if not exists leitura(
				id int auto_increment primary key,
				id_disco int not null,
				id_usuario int not null,
				id_pasta int not null,
				valor_usado float not null,
				valor_livre_percentual float not null,
				ram_livre float not null,
				ram_livre_percentual float not null,
				dta_leitura TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
				FOREIGN KEY(id_disco) REFERENCES disco(id),
				FOREIGN KEY(id_usuario) REFERENCES usuario(id),
				FOREIGN KEY(id_pasta) REFERENCES pasta(id)
		); """
        cursor.execute(createTable)
        print('Criada tabela leitura')

        connection.commit()
        connection.close()


def insertDados(base, senha):
    try:
        # Iniciada tentativa de conexão com o banco
        connection = mysql.connector.connect(
            #Informações da base de dados
            host='localhost', database=base, user='root', password=senha)
        if connection.is_connected():
            db_Info = connection.get_server_info()
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()

    except Error as e:
        # Caso ocorra erro
        print("Não conectado", e)

    finally:

        insert = """
            insert into disco (nome, espaco_total)
            values('G://', 931.00),('C://', 111.00),('E://', 223.00);"""
        cursor.execute(insert)
        print('Insert do disco')

        insert = """
            insert into pasta(diretorio,quantidadeLeituras)
            values('Teste de insert 2',1);"""
        cursor.execute(insert)
        print('Insert da pasta')

        insert = """
            insert into usuario(nome)
            values ('Teste de 2° usuário');"""
        cursor.execute(insert)
        print('Insert do usuario')

        connection.commit()
        connection.close()
