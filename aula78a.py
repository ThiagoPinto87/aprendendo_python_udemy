# Sets - Conjuntos em Python (tipo set)

# 'Set' são eficientes para remover valores duplicados
# de iteráveis.
# - Seus valores serão sempre únicos;
# - Não aceitam valores mutáveis;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

#l1 = {1, 2, 3, 3, 3, 3, 3, 1}
#print(l1, type(l1))

# l1 = [1, 2, 3, 3, 3, 3, 3, 1]
# print(l1, type(l1))
# s1 = set(l1)
# print(s1, type(s1))
# l2 = list(s1)
# print(l2, type(l2))

s1 = {1, 2, 3}
print(3 not in s1)
for numero in s1:
    print(numero)

# Métodos úteis:
# add, update, clear, discard

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos