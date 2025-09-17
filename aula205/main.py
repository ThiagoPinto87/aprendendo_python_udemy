import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME    # Caminho completo do arquivo
TABLE_NAME = 'customers'        # Tabela de clientes que será criada

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()


# # Cria a tabela caso não exista
# cursor.execute(
#     f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
#     '('
#     'id INTEGER PRIMARY KEY AUTOINCREMENT,'
#     'name TEXT,'
#     'weight REAL'
#     ')'
# )
# connection.commit()


# CRUD - Create, Read, Update, Delete
# SQL - INSERT, SELECT, UPDATE, DELETE


#CUIDADO: fazendo delete sem where
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)



# DELETE com WHERE




connection.commit()


# Registrar valores nas colunas da tabela.
# Esta é a forma mais segura de inserir valores, evitando SQL Injection usando ? como placeholder (binding)

# sql = (
# f'INSERT INTO {TABLE_NAME} (name, weight) '
# 'VALUES '
# '(?, ?)'
# )

# cursor.execute(sql, ['Luiz', 84.5])
# connection.commit()



# # Inserindo múltiplos valores de uma vez
# sql = (
# f'INSERT INTO {TABLE_NAME} (name, weight) '
# 'VALUES '
# '(?, ?)'
# )

# cursor.executemany(sql, [
#     ['Luiz', 84.5], ['Maria', 65.1], ['João', 70.2]
#     ])
# connection.commit()



# # Inserindo valores com dicionário.
# sql = (
# f'INSERT INTO {TABLE_NAME} (name, weight) '
# 'VALUES '
# '(:name, :weight)'
# )

# cursor.execute(sql, {'name': 'Julio', 'weight': 88.5})
# connection.commit()




# Inserindo múltiplos valores com dicionário.
sql = (
f'INSERT INTO {TABLE_NAME} (name, weight) '
'VALUES '
'(:name, :weight)'
)


cursor.executemany(sql, (
{'name': 'Luiz', 'weight': 84.5},
{'name': 'Maria', 'weight': 65.1},
{'name': 'João', 'weight': 70.2}
))
connection.commit()


if __name__ == '__main__':
    print(sql)


    # # DELETE com WHERE
    # cursor.execute(
    #     f'DELETE FROM {TABLE_NAME} '
    #     'WHERE id = 52'
    # )
    # connection.commit()

    # cursor.execute(
    #     f'SELECT * FROM {TABLE_NAME}'
    # )

    # for row in cursor.fetchall():
    #     _id, name, weight = row # Desempacotamento
    #     print(_id, name, weight)



    # UPDATE com WHERE
    # No update, precisa colocar quais as colunas que serão alteradas. Lembrando de não esquecer de colocar o WHERE.
    cursor.execute(
        f'UPDATE {TABLE_NAME} '
        'SET name = "QUALQUER VALOR", weight = 99.9 '
        'WHERE id = 58'
    )
    connection.commit()

    cursor.execute(
        f'SELECT * FROM {TABLE_NAME}'
    )

    for row in cursor.fetchall():
        _id, name, weight = row # Desempacotamento
        print(_id, name, weight)


    

    # Fechando a conexão
    cursor.close()
    connection.close()