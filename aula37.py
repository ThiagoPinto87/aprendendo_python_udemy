"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

contador = 0

while contador <= 100:
    contador += 1
    
    if contador == 6:
        print('Não vou mostrar o 6.')
        continue    #Pula o laço não segue com a string abaixo.

    if contador >= 10 and contador<= 27:
        print(f'Não vou mostrar o {contador}')
        continue    #Pula o laço não segue com a string abaixo.

    print(contador)

    if contador == 40:
        break   #Quebra o laço.

print('Acabou')


