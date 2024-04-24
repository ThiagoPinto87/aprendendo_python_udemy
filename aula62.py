"""
Calculo do Segundo dígito do CPF
CPF: 746.824.890-70

Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11  10  9  8  7  6  5  4  3  2
*  7   4   6  8  2  4  8  9  0  7
   77  40 ...

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0+14 = 315
Multiplicar o resultado anterior por 10
315 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf = '746.824.890-70'

#PRIMEIRO DÍGITO
nove_digitos = cpf[:11].replace('.','')
#print(nove_digitos)

res_multipl = []
coeficiente_1 = 10
soma = 0
for n in nove_digitos:
    soma += int(n) * coeficiente_1
    coeficiente_1 -= 1

prep_prim_digito = (soma * 10) % 11

prim_digito = prep_prim_digito if prep_prim_digito <= 9 else 0

print(prim_digito)


#SEGUNDO DÍGITO
dez_digitos = cpf[:13].replace('.','')
dez_digitos = dez_digitos.replace('-','')
#print(dez_digitos)

res_multipl = []
coeficiente_2 = 11
soma = 0
for n in dez_digitos:
    soma += int(n) * coeficiente_2
    coeficiente_2 -= 1

prep_seg_digito = (soma * 10) % 11

seg_digito = prep_seg_digito if prep_seg_digito <= 9 else 0

print(seg_digito)



#VALIDAÇÃO
cpf_limpo = cpf.replace('-', '')
cpf_limpo = cpf_limpo.replace('.','')

if nove_digitos + str(prim_digito) + str(seg_digito) == cpf_limpo:
    print('CPF Validado')
else:
    print('CPF INCORRETO')