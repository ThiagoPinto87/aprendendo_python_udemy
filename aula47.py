"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
    - Se a letra digitada estiver na palavra secreta; exiba a letra;
    - Se a letra digitada não estiver na palavra secreta; exiba "*".
Faça a contagem de tentativas do seu usuário.
"""


# verificar aulas 27 e 29 para a solução do exercício e verificar também o método replace conforme sugerido pelo "Predador_Vegano".


palavra_secreta = 'perfume'
palavra_formada = ''

while True:
    usuario = input('Digite uma letra: ').lower()

    if len(usuario) > 1:
        print('Digite apenas 1 (uma) letra.')
        continue        # Sai do if voltando ao while.

    if usuario in palavra_secreta:
        for letra in palavra_secreta:
            if usuario == letra:
                palavra_formada += usuario
            else:
                palavra_formada += '*'
        print(palavra_formada)
    else:
        for letra in palavra_secreta:
            palavra_formada += '*'
        print(palavra_formada)