"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input('Digite um número inteiro: ')

try:
    numero_int = int(numero)
    par_impar = numero_int % 2

    if par_impar == 0:
        print(f'Você digitou {numero_int} que é PAR.')
    else:
        print(f'Você digitou {numero_int} que é IMPAR.')
except:
    print('Você não digitou um número inteiro.')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

print('#' * 25)

hora = input('Digite uma hora [inteiro]: ')

try:
    hora_int = int(hora)

    if hora_int >= 0 and hora_int <= 11:
        print('Bom dia!')
    elif hora_int >= 12 and hora_int <= 17:
        print('Boa tarde')
    elif hora_int >= 18 and hora_int <= 23:
        print('Boa noite')
    elif hora_int > 23:
        print('Número de hora inválido. Por favor, digite outro número inteiro.')
except:
    print('Você não digitou um número inteiro.')



"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

print('#' * 25)

nome = input('Digite seu nome: ')

try:
    tamanho = len(int(nome))

    if type(nome) != str:
        print('Você não digitou um nome válido.')    
    elif tamanho <= 4:
        print(f'Seu nome {nome} é CURTO.')
    elif tamanho > 4 and tamanho <= 6:
        print(f'Seu nome {nome} é NORMAL.')
    else:
        print(f'Seu nome {nome} é MUITO GRANDE.')
except:
    print('Você não digitou um nome válido')