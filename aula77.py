# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

# for pergunta in perguntas:
#     for chave, valor in pergunta.items():
#         print(chave, valor)

acertos = 0
for questao in perguntas:
    try:
        print(f'Pergunta: {questao['Pergunta']}')
        
        for n, opcao in enumerate(questao['Opções']):
            print(f'{n}) {opcao}')
        
        print()
        resposta_usuario = input('Escolha uma opção: ')
        resposta_usuario = int(resposta_usuario)

        if questao['Opções'][resposta_usuario] == questao['Resposta']:
            print('>>> ACERTOU <<<')
            acertos += 1
            print()
        else:
            print('ERROU!!!')
            print()
    
    except:
        print('ERROU!!!')
        print()

print('##### RESULTADO #####')
print(f'Você acertou {acertos} de {len(perguntas)}')