"""
Interpolação básica de strings
s - para interpolar string's
d e i - para interpolar int's
f - para interpolar float's
x e X - para interpolar Hexadecimais (ABCDEF0123456789)
"""
nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco) # Isso é interpolação colocar o "%"
print(variavel)
print('O hexadecimal de %d é %08X' % (1500, 1500))