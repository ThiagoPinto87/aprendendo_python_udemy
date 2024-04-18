"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
    - Se a letra digitada estiver na palavra secreta; exiba a letra;
    - Se a letra digitada não estiver na palavra secreta; exiba "*".
Faça a contagem de tentativas do seu usuário.
"""
import os

palavra_secreta = 'perfume'
letras_acertadas =''
cont = 0

while True:
    usuario = input('Digite uma letra: ').lower()
    cont += 1

    #Verifica se o usuário tentou digitar várias letras.
    if len(usuario) > 1 or usuario.isnumeric():
        print('Digite apenas 1 (uma) letra.')
        continue        # Sai do if voltando ao while.
        
    if usuario in palavra_secreta:
        letras_acertadas += usuario

    palavra_formada =''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    
    print(f'Palavra formada: {palavra_formada}')
    
    if palavra_formada == palavra_secreta:
        print('VOCÊ ACERTOU')
        print(f'A palavra era: {palavra_secreta}')
        print(f'Você tentou {cont} vezes.')
        letras_acertadas =''
        cont = 0
