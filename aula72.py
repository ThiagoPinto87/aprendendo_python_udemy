"""
Exercício com funções

# Crie uma função que multiplica todos os argumentos não nomeados recebidos. Retorne o total para uma variável e mostre o valor da variável.

# Crie uma função que fala se um número é par ou ímpar. Retorne se o número é par ou ímpar.
"""

def multiplacador(*args):
    total = 1
    for n in args:
        total *= n
    return total

multiplacacao = multiplacador(1,2,3,4,5)
print(1*2*3*4*5)
print(multiplacacao)

print('\n#################\n')

def par_impar(x):
    numero = x
    if numero % 2 == 0:
        print('Par')
    else:
        print('Ímpar')

par_impar(5)

#Resolução do professor.

def par(x):
    return x % 2 == 0

print(par(2))
print(par(5))
print(par(17))
print(par(22))

#resolução 2

print('##### Resolução 2 #####')
def par_ou_impar(x):
    valor = x % 2 == 0
    if valor:
        return f'{x} é par.'
    return f'{x} é ímpar.'

print(par_ou_impar(2))
print(par_ou_impar(7))
print(par_ou_impar(8))
print(par_ou_impar(9))