# Sets - Conjuntos em Python (tipo set)


# Operadores úteis:

# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos


s1 = {1, 2, 3}
s2 = {2, 3, 4}

s3 = s1 | s2    # Une os dois sets
s3 = s1 & s2    # Interceção nos dois sets
s3 = s1 - s2    # Itens presentes somente no primeiro set (na esquerda). Result. 1
s3 = s2 - s1    # Itens presentes somente no primeiro set (na esquerda). Result. 4
s3 = s1 ^ s2    # Itens exclusivos em cada set (retira a interseção entre os sets)
print(s3)