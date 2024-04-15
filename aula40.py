# Calculadora com while

while True:     # O True está sendo redundante, visto que o while já é True internamente.
   
    print('#### Calculadora ####')
    
    try:
        prim_numero = input('Digite um número: ')
        prim_numero = float(prim_numero)
        
        seg_numero = input('Digite outro número: ')
        seg_numero = float(seg_numero)

        operacao = input('Digite a operação [+], [-], [*] ou [/]: ')
        
        while len(operacao) > 1:
            print('Digite apenas um operador.')
            operacao = input('Digite a operação [+], [-], [*] ou [/]: ')
            
        while True:
            
            try:
                if operacao == '+':
                    resultado = prim_numero + seg_numero
                    print(f'A soma de {prim_numero} + {seg_numero} é {resultado:5f}')
                    break

                elif operacao == '-':
                    resultado = prim_numero - seg_numero
                    print(f'A subtração de {prim_numero} - {seg_numero} é {resultado:5f}')
                    break

                elif operacao == '*':
                    resultado = prim_numero * seg_numero
                    print(f'A multiplicação de {prim_numero} * {seg_numero} é {resultado:5f}')
                    break

                elif operacao == '/':
                    resultado = prim_numero / seg_numero
                    print(f'A divisão de {prim_numero} / {seg_numero} é {resultado:5f}')
                    break

                else:
                    print(f'Você digitou "{operacao}", não é um operador válido.')
                    operacao = input('Digite a operação [+], [-], [*] ou [/]: ')
        
            except:
                print('Você fez uma operação inválida, a calculadora será reiniciada.')
                break
    
        sair = input('Quer sair [s]im: ').lower().startswith('s')
        if sair is True:
            break

    except:
        print('Você não digitou um número válido.')
