"""
Faça uma lista de compras com listas.
O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista.
Não permita que o programa quebre com erros de índices inexistentes na lista.

"""

###- Colocar na lista a quantidade
###- Sair do sistema

lista_compras = []

while True:
    print('Digite a opção desejada:')
    opcao = input('[i]Inserir | [a]Apagar | [l]Listar: ').lower()

    try:
        if len(opcao) > 1:
            print('Digite apenas uma das opções abaixo:')
            opcao = input('[i]Inserir | [a]Apagar | [l]Listar: ').lower()

        elif opcao == 'i':
            produto = input('Qual produto deseja inserir? \n')
            lista_compras.append(produto)
            print('Produto inserido com sucesso!')

        elif opcao == 'a':
            del_produto = input('Qual produto deseja tirar da lista? \nDigite o índice dele: ')
            del_produto = int(del_produto)
            del lista_compras[del_produto]
            print('Produto retirado da lista com sucesso!')

        elif opcao == 'l':
            if not lista_compras: #lista_compras == []:
                print('Não há produtos a serem listados.')
                continue

            else:
                print('-'*20)
                print(f'Índice\t|Produto')
                print('-'*20)
                for i, produto in enumerate(lista_compras):
                    print(f'{i}\t|{produto}')

        else:
            print(f'Você digitou {opcao}. Esta opção é inválida. \nDigite uma das três opções sugeridas.')

    except:
        print(f'Você digitou {opcao}. Esta opção é inválida. \n O sistema será reiniciado')
        continue