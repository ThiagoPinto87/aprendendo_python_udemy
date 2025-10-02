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
            '(nome, idade, peso) VALUES (%s, %s, %s) ' #Os %s são placeholders para os valores
        )
        # Inserindo dados na tabela.
        data = ("João", 30, 80.5)
        result = cursor.execute(sql, data)
        print(f'{result} linha afetada.')
    connection.commit()


