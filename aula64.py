"""
Criando CPF.
"""
import random

for _ in range(10):
    cpf = ''

    for i in range(9):
        cpf += str(random.randint(0,9))

    #print(cpf)

    #PRIMEIRO DÍGITO
    nove_digitos = cpf[:9]
    #print(nove_digitos)

    res_multipl = []
    coeficiente_1 = 10
    soma = 0
    for n in nove_digitos:
        soma += int(n) * coeficiente_1
        coeficiente_1 -= 1

    prep_prim_digito = (soma * 10) % 11

    prim_digito = prep_prim_digito if prep_prim_digito <= 9 else 0

    #print(prim_digito)


    #SEGUNDO DÍGITO
    dez_digitos = cpf[:10] + str(prim_digito)
    #print(dez_digitos)

    res_multipl = []
    coeficiente_2 = 11
    soma = 0
    for n in dez_digitos:
        soma += int(n) * coeficiente_2
        coeficiente_2 -= 1

    prep_seg_digito = (soma * 10) % 11

    seg_digito = prep_seg_digito if prep_seg_digito <= 9 else 0

    #print(seg_digito)


    #VALIDAÇÃO
    cpf_limpo = cpf

    cpf_gerado_pelo_calculo = nove_digitos + str(prim_digito) + str(seg_digito)

    print(cpf_gerado_pelo_calculo)