"""
Higher Order Functions ou First-Class Functions
Funções de primeira classe

Academicamente, os termos Higher Order Functions e First-Class Functions têm significados diferentes.

Higher Order Functions - Funções que podem receber e/ou retornar outras funções

First-Class Functions - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)


"""


def saudacao(msg, nome):
    return f'{msg}, {nome}!'


def executa(funcao, *args): #Empacotou os argumentos
    return funcao(*args)    #Desempacotou os argumentos.


print(
    executa(saudacao, 'Bom dia', 'Luiz')
)
print(
    executa(saudacao, 'Boa noite', 'Maria')
)