"""
Melhorando o código.
"""

import re
import sys

entrada = input('CPF: ')

#746.824.890-70

cpf = re.sub(r'[^0-9]','', entrada)
entrada_e_sequencial = entrada == entrada[0] * len(entrada)

if entrada_e_sequencial:
    print('Você enviou dados sequenciais')
    sys.exit()
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
dez_digitos = cpf[:10]
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

if nove_digitos + str(prim_digito) + str(seg_digito) == cpf_limpo:
    print('CPF Validado')
else:
    print('CPF INCORRETO')