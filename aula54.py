"""
Faça uma lista de compras com listas.
O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista.
Não permita que o programa quebre com erros de índices inexistentes na lista.

"""
import os

lista_compras = []

while True:
    print('Digite a opção desejada:')
    opcao = input('[i]Inserir | [a]Apagar | [l]Listar | [s]Sair: ').lower()
   
        
    try:
        if len(opcao) > 1:
            os.system('cls')
            print('Digite apenas uma das opções abaixo:')
            opcao = input('[i]Inserir | [a]Apagar | [l]Listar | [s]Sair: ').lower()

        elif opcao == 'i':
            os.system('cls')
            produto = input('Qual produto deseja inserir? \n')
            lista_compras.append(produto)
            print('Produto inserido com sucesso!')

        elif opcao == 'a':
            os.system('cls')
            del_produto = input('Qual produto deseja tirar da lista? \nDigite o índice dele: ')
            del_produto = int(del_produto)
            del lista_compras[del_produto]
            print('Produto retirado da lista com sucesso!')

        elif opcao == 'l':
            os.system('cls')
            if not lista_compras: #lista_compras == []:
                print('Não há produtos a serem listados.')
                continue

            else:
                print('-'*20)
                print(f'Índice\t|Produto')
                print('-'*20)
                for i, produto in enumerate(lista_compras):
                    print(f'{i}\t|{produto}')
        
        elif opcao == 's':
            os.system('cls')
            saida = input('Você selecionou sair, deseja confirmar a saída? [s]Sim [n]Não: ').lower()

            if saida == 's':
                break
            else:
                continue

        else:
            os.system('cls')
            print(f'Esta opção é inválida.\n')
        

    except ValueError:
        os.system('cls')
        print(f'Por favor digite um número inteiro.')
        continue
    except IndexError:
        print('Este índice é inválido.')
    except Exception:
        print('Erro não identificado.')