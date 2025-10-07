import os
import pymysql
import dotenv

# Carrega as variáveis de ambiente do arquivo .env
dotenv.load_dotenv()


TABLE_NAME = 'cusomers'

# Conexão com o banco de dados MySQL.
connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
)


# Conexão com o banco de dados MySQL e garante que será fechada após o uso.
with connection:
    # Abre um cursor para executar comandos SQL e fecha automaticamente após o bloco.
    with connection.cursor() as cursor:   
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ( '                       
                       'id INT NOT NULL AUTO_INCREMENT, '
                       'nome VARCHAR(50) NOT NULL, '
                       'idade INT NOT NULL, ' 
                       'peso DECIMAL(5,2) NOT NULL, '
                       'PRIMARY KEY (id))'
        )
        #CUIDADO, ESTE COMANDO APAGA TODOS OS DADOS DA TABELA
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')
    connection.commit()
    print("Conexão bem sucedida!")
    
    # Começamos a manipular dados na tabela.

    with connection.cursor() as cursor:   
        sql = (
            f'INSERT INTO {TABLE_NAME} '                       
            '(nome, idade, peso) VALUES (%s, %s, %s) ' #Os %s são placeholders para os valores e previnem o SQL Injection.
        )
        # Inserindo dados na tabela.
        data = ("João", 30, 80.5)
        result = cursor.execute(sql, data)
        # print(f'{result} linha afetada.')
    connection.commit()



    # Inserindo dados na tabela usando um dicionário.
    with connection.cursor() as cursor:   
        sql = (
            f'INSERT INTO {TABLE_NAME} '                       
            '(nome, idade, peso) VALUES '
            '(%(name)s, %(idade)s, %(peso)s) ' #Os valores constantes nos parenteses, tem que ser iguais aos nomes das chaves do dicionário.
        )
        # Inserindo dados na tabela.
        data2 = {
            "peso": 55.0,
            "name": "Maria",
            "idade": 25,
        }
        result = cursor.execute(sql, data2)
        # print(f'{result} linha afetada.') 
        # print(sql)
        # print(data2)  
    connection.commit()


    # Inserindo múltiplos dados na tabela usando uma lista de dicionários.
    with connection.cursor() as cursor:   
        sql = (
            f'INSERT INTO {TABLE_NAME} '                       
            '(nome, idade, peso) VALUES '
            '(%(name)s, %(idade)s, %(peso)s) ' #Os valores constantes nos parenteses, tem que ser iguais aos nomes das chaves do dicionário.
        )
        # Inserindo dados na tabela.
        data3 = (
            {"peso": 25.0,"name": "João","idade": 12,},
            {"peso": 30.0,"name": "Maria","idade": 22,},
            {"peso": 35.0,"name": "Ana","idade": 32,},
            {"peso": 40.0,"name": "Pedro","idade": 42,},
        )
        result = cursor.executemany(sql, data3)
        # print(f'{result} linha afetada.') 
        # print(sql)
        # print(data3)  
    connection.commit()


    # Inserindo múltiplos dados na tabela usando uma lista de tuplas.
    with connection.cursor() as cursor:   
        sql = (
            f'INSERT INTO {TABLE_NAME} '                       
            '(nome, idade, peso) VALUES '
            '(%s, %s, %s) ' #Os valores constantes nos parenteses, tem que ser iguais aos nomes das chaves do dicionário.
        )
        # Inserindo dados na tabela.
        data4 = (
            ("Karina",38,28.0),
            ("Karolina",32,30.0),
        )
        result = cursor.executemany(sql, data4)
        # print(f'{result} linha afetada.') 
        # print(sql)
        # print(data4)  
    connection.commit()


    #LENDO os valores com SELECT
    # with connection.cursor() as cursor:   
    #     sql = (
    #         f'SELECT * FROM {TABLE_NAME}'
    #     )

    #     cursor.execute(sql)
        
        # print('-' * 50)
        # print('Lendo uma linha com fetchone()')
        # data5 = cursor.fetchone()
        # print(data5)
        # print()
        # print('-' * 50)
        # print('Lendo todas as linhas com fetchall()')
        # data6 = cursor.fetchall()
        
        # for row in data:
        #     print(row)
        # print('-' * 50)

    
    #LENDO os valores com SELECT
    with connection.cursor() as cursor:   
        sql = (
            f'SELECT * FROM {TABLE_NAME} '
            'WHERE id > 5 '
        )

        cursor.execute(sql)
        
        print('-' * 50)
        print('Lendo todas as linhas com fetchall()')
        data6 = cursor.fetchall()
        print('-' * 50)
        
        for row in data6:
            print(row)
        print('-' * 50)


