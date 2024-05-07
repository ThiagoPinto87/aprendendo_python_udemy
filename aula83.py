# Empacotamento e desempacotamento de dicionários
# a, b = 1, 2
# a, b = b, a
# # print(a, b)


# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

# a, b = pessoa.values()
# print(a, b)

# a, b = pessoa.items()
# print(a, b)

# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

# print(pessoa, dados_pessoa)

#PARA EXTRAIR DADOS DE UM DICIONÁRIO BASTA COLOCAR '**'
pessoas_completa = {**pessoa, **dados_pessoa}

# print(pessoas_completa)

# # args e kwargs
# # args (já vimos) - são argumentos não nomeados.
# # kwargs - keyword arguments (argumentos nomeados)


def mostro_argumentos_nomeados(*args, **kwargs):
    print('não nomeados', args)
    for chave, valor in kwargs.items():
        print(chave, valor)



# mostro_argumentos_nomeados(1, 2, nome='Joana', qlq=123)

# mostro_argumentos_nomeados(**pessoas_completa)

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}
mostro_argumentos_nomeados(**configuracoes)