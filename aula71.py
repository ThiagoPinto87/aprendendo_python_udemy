"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembre-te de desempacotamento
# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)


# def soma(x, y):
#     return x + y

def soma(*args): #o parametro descrito como 'args' é uma convenção dos devs Pythonistas para argumentos não nomeados.
    print(args)
    total = 0
    for n in args:
        total += n
    return total

# soma_1_2_3 = soma(1,2,3)
# print(soma_1_2_3)

numeros = 1,2,3,8,9,12,456
soma_cabulosa = soma(*numeros)  #O '*' está desempacotando a tupla 'numeros', caso isso não seja feito, a função soma, não ocorrerá.
print(soma_cabulosa)

print(sum(numeros))