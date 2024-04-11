nome = input('Qual o seu nome? ')   #O resultado que o input trás é somente string, ou seja, se quiser fazer conta, tem que usar a coerção de dados.

print(f"O seu nome é {nome=}") #o '=' após a variável é utilizada para identificar qual o nome da váriável no output pois ela repete qual a variável.

print('--------------')

n1 = input("digite um número: ")
n2 = input("digite outro número: ")

int_n1 = int(n1)
int_n2 = int(n2)


print(f'A soma dos números é: {int_n1 + int_n2}')