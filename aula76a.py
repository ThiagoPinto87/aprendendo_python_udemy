# Manipulando chaves e valores em dicionários
pessoa = {}

##
##

chave = 'nome'

# pessoa[chave] = 'Luiz Otávio'
pessoa[chave] = 'Skilo'
pessoa['sobrenome'] = 'Cba'

print(pessoa)
print(pessoa[chave])

pessoa['nome'] = 'Maria'

print(pessoa)
del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

print(pessoa.get('sobrenome')) #print(pessoa.get('sobrenome', 'não existe'))
if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])

# print('ISSO Não vai')