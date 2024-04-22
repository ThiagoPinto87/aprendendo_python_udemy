"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3   4   5
lista = [10, 20, 30, 40]#... Adicionar itens no final utiliza menos processamento.
# lista[2] = 300
# del lista[2]
lista.append(50)
lista.pop() #Remove o ultimo valor.
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(3) # Retirou o valor 70 e colocou na variável 'ultimo_valor'.
print(lista, 'Removido,', ultimo_valor)
print(lista)
print(lista[2])