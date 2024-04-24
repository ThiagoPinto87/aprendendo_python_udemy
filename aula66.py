"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

# def soma(x, y):
#     print(x + y)

# soma(1, 2) #Definição de argumento posicional.



def soma(x, y, z):
    # Definição
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)


soma(1, 2, 3)
soma(1, z=2, y=5) #Exemplo de argumento nomeado.

# print(1, 2, 3, sep='-')