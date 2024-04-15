# Calculadora com while

while True:     # O True está sendo redundante, visto que o while já é True internamente.
    sair = input('Quer sair [s]im: ')
    sair = sair.lower()
    if sair == 's':
        break

    try:
        prim_numero = input('Digite um número: ')
        prim_numero = float(prim_numero)
        
        seg_numero = input('Digite outro número: ')
        seg_numero = float(seg_numero)
        
        operacao = input('Digite a operação [a], [s], [m] ou [d]: ')

        while not operacao == 'a' or not operacao == 's' or not operacao == 'm' or not operacao == 'd':
            print(f'Você digitou "{operacao}", não é um operador válido.')
            operacao = input('Digite a operação [a], [s], [m] ou [d]: ')
        
        try:
                if operacao == 'a':
                    resultado = prim_numero + seg_numero
                    print(f'A soma de {prim_numero} + {seg_numero} é {resultado:5f}')

                elif operacao == 's':
                    resultado = prim_numero - seg_numero
                    print(f'A subtração de {prim_numero} - {seg_numero} é {resultado:5f}')

                elif operacao == 'm':
                    resultado = prim_numero * seg_numero
                    print(f'A multiplicação de {prim_numero} * {seg_numero} é {resultado:5f}')

                elif operacao == 'd':
                    resultado = prim_numero / seg_numero
                    print(f'A divisão de {prim_numero} / {seg_numero} é {resultado:5f}')
        except:
            print('Você fez uma operação inválida, a calculadora será reiniciada.')
            break

    except:
        print('Você não digitou um número válido.')