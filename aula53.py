"""
enumerate - enumera iteráveis (índices) (Cria uma lista enumerada)
"""
# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')


# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)


for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])

# for tupla_enumerada in enumerate(lista):
#     print('FOR da tupla:')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')


# lista_enumerada = enumerate(lista)
# #print(next(lista_enumerada))

# for item in lista_enumerada:
#     print(item)