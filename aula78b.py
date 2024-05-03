# Sets - Conjuntos em Python (tipo set)

# Métodos úteis:
# add, update, clear, discard
s1 = set()
s1.add('Luiz')
s1.add(1) # Não aceita inserir mais de um valor como por exemplo: 's1.add(1,2)'
s1.update(('Olá mundo', 1, 2, 3, 4))
# s1.clear()
s1.discard('Olá mundo') #Elimina um determinado valor imutável.
s1.discard('Luiz') #Elimina um determinado valor imutável.
print(s1)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos