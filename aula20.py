primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor=} é maior que {segundo_valor=}')

elif primeiro_valor == segundo_valor:
    print(f' O {primeiro_valor=} e o {segundo_valor=} são iguais')

else:
    print(f'{segundo_valor=} é maior que {primeiro_valor=}')