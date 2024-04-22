"""
Introdução ao empacotamento e desempacotamento
"""
nome1, *resto = ['Maria', 'Helena', 'Luiz'] # O '*' empacota o restante da lista na variável definda com o nome 'resto'. Caso não queira usar a variável, por convenção da comunidade python, utiliza-se o '_'


# A
nome1, *_ = ['Maria', 'Helena', 'Luiz']

# B
_, nome2, *_ = ['Maria', 'Helena', 'Luiz']

# C
_, _, nome, *_ = ['Maria', 'Helena', 'Luiz']

# D
_, _, nome, *resto = ['Maria', 'Helena', 'Luiz']

# _, _, nome, *resto = ['Maria', 'Helena', 'Luiz']
print('----A---')
print(nome1)
print('----B----')
print(nome2)
print('----C----')
print(nome)
print('----D----')
print(nome, resto) #Como não há mais valores dentro da lista, ele traz uma lista vazia caso isso seja útil em algum momento.