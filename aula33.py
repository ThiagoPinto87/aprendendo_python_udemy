"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""
#string = '1000'
# outra_variavel = f'{string[:3]}ABC{string[4:]}'
# print(string)
# print(outra_variavel)
#print(string.zfill(10))


nome = 'Skilo_Cba'
nome_alterado = f'{nome[:4]}0{nome[5:]}'    #Substitui o 'o' pelo '0' e coloca na variável 'nome_alterado' usando o fatiamento de string.
#print(nome_alterado)
print(nome_alterado.zfill(20))              #Coloca '0' à esquerda até completar a quantidade de caracteres que você pediu. Muito bom para controlar tamanho de string's.
