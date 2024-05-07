# Dictionary Comprehension e Set Comprehension

#### Dictionary Comprehension ####
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

# print(produto.items())

# dc = {
#     chave: valor.upper()
#     if isinstance(valor, str) else valor    # se o valor for do tipo str...
#     for chave, valor
#     in produto.items()
#     if chave != 'categoria'
# }
# print(dc)


# lista = [
#     ('a', 'valor a'),
#     ('b', 'valor a'),
#     ('b', 'valor a'),
# ]
# dc = {
#     chave: valor
#     for chave, valor in lista
# }

# print(dc)



# lista = [
#     ('a', 'valor a'),
#     ('b', 'valor a'),
#     ('b', 'valor a'),
# ]

# print(dict(lista))


####Set comprehension####

s1 = {2 ** i for i in range(10)}
print(s1)