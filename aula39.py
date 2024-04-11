"""
Iterando strings com while.
"""

#       012345678
nome = 'Skilo_Cba'

tamanho_nome = len(nome)
# print(tamanho_nome)
# print(nome[4])


#nova_string = '*S*k*i*l*o*_*C*b*a'

nova_string = ' '
contador = 0
while contador < tamanho_nome:
    string = f'*{nome[contador]}'
    nova_string += string
    contador += 1
    #nome[contador] = f'*{nova_string[nome[contador]]}'

print(f'{nova_string}*')