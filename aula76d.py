# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave e retorna um valor da chave ou None.
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda',
}
# print(p1['nome'])
# print(p1.get('nome', 'Não existe'))

# nome = p1.pop('nome')
# print(nome)
# print(p1)

# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)

# print(p1)
# p1.update({
#     'nome': 'novo valor',   #Aqui está alterando o valor da chave 'nome'
#     'idade': 30,            #Aqui está incluindo a chave 'idade' e passando o valor 30.
# })
print(p1)
# p1.update(nome='novo valor', idade=30)
# tupla = (('nome', 'novo valor2'), ('idade', 35))
# p1.update(tupla)
lista = [['nome', 'novo valor3'], ['idade', 38]]
p1.update(lista)
print(p1)