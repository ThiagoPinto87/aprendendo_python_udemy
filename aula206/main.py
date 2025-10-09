import os
import pymysql
import pymysql.cursors
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
    cursorclass=pymysql.cursors.DictCursor, # Define o cursor para retornar resultados como dicionários.
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
    # with connection.cursor() as cursor:
    #     menor_id = 2
    #     maior_id = 5

    #     sql = (
    #         f'SELECT * FROM {TABLE_NAME} '
    #         'WHERE id BETWEEN %s AND %s'
    #     )

    #     cursor.execute(sql, (menor_id, maior_id)) #Os valores são passados como uma tupla para substituir os placeholders %s na consulta SQL.
    #     print(cursor.mogrify(sql, (menor_id, maior_id))) #Demonstra o comando SQL que será executado com os valores inseridos.

    #     print('-' * 50)
    #     print('Lendo todas as linhas com fetchall()')
    #     data6 = cursor.fetchall()
    #     print('-' * 50)
        
        # for row in data6:
        #     print(row)
        # print('-' * 50)



    #DELETANDO um registro
    # with connection.cursor() as cursor:

    #     sql = (
    #         f'DELETE FROM {TABLE_NAME} '
    #         'WHERE id = %s'
    #     )

    #     print(cursor.execute(sql, (3,))) #Os valores são passados como uma tupla para substituir os placeholders %s na consulta SQL.
    #     connection.commit()

    #     cursor.execute(f'SELECT * FROM {TABLE_NAME}') #Os valores são passados como uma tupla para substituir os placeholders %s na consulta SQL.

    #     for row in cursor.fetchall():
    #         print(row)

    
    #ATUALIZANDO um registro
    with connection.cursor() as cursor:

        sql = (
            f'UPDATE {TABLE_NAME} '
            'SET nome = %s, idade = %s, peso = %s '
            'WHERE id = %s'
        )

        cursor.execute(sql, ('Thiago', 37, 89.5, 4)) #Os valores são passados como uma tupla para substituir os placeholders %s na consulta SQL.
        connection.commit()

        result_from_select = cursor.execute(f'SELECT * FROM {TABLE_NAME}') #Os valores são passados como uma tupla para substituir os placeholders %s na consulta SQL.

        # for row in cursor.fetchall():
        #     _id, nome, idade, peso = row
        #     print(f'ID: {_id}, Nome: {nome}, Idade: {idade}, Peso: {peso:.2f}kg')
       
        # for row in cursor.fetchall():
        #     _id, nome, idade, peso = row.values()
        #     print(f'ID: {_id}, Nome: {nome}, Idade: {idade}, Peso: {peso}kg')


        # #Testando o scroll do cursor com o modo padrão (absoluto)
        # print('For 1: ')
        # for row in cursor.fetchall():
        #     print(row)

        # # #Movendo o cursor para testar o scroll
        # # print('-' * 50)
        # # print('For 2: ')
        # # cursor.scroll(-3) #Retorna o cursor para o início dos resultados.

        # #Movendo o cursor para testar o scroll com modo absoluto
        # print('-' * 50)
        # print('For 2: ')
        # cursor.scroll(3, mode='absolute') #Retorna o cursor para o início dos resultados.

        # for row in cursor.fetchall():
        #     print(row)

    
    #Testando outras coisas com o cursor
        for row in cursor.fetchall():
            print(row)


        # cursor.execute(
        #     f'SELECT id fom {TABLE_NAME} ORDER BY id DESC LIMIT 1'
        # )
        # lastID = cursor.fetchone()
        

        print('Result from select:', result_from_select)
        print('rowcount:', cursor.rowcount) #Número de linhas afetadas pela última operação.
        print('lastrowid:', cursor.lastrowid) #ID da última linha inserida
        # print('lastrowid na mão:', lastID['id']) #ID da última linha inserida
        print('rownumber:', cursor.rownumber) #Número da linha atual no conjunto de resultados.
