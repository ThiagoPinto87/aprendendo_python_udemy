import sqlite3
from main import DB_FILE, TABLE_NAME

# Abrindo conexão
connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(
    f'SELECT * FROM {TABLE_NAME}'
)


# Mostrando somente um dado
row = cursor.fetchone()
print(row)


# Mostrando os dados
# for row in cursor.fetchall():
#     _id, name, weight = row # Desempacotamento
#     print(_id, name, weight)

# Fechando a conexão
cursor.close()
connection.close()