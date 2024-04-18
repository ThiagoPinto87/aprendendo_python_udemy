"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::] - i-> início | f-> fim | p-> passo
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[::-1])
print(variavel[4:7])    #Começará a partir do caracter 4 e vai até o 6º caracter.
print(variavel[4:])     #Começará a partir do caracter 4 e vai até o final da string.
print(variavel[0:5])    #Começará a partir do caracter 0 e vai até o 4º caracter.
print(variavel[:6])     #Começará a partir do início da string e vai até o 5º caracter.
print(len(variavel))    #conta a quantidade de caractéres do string.
print(variavel[0:9:2])  #Começará a partir do caracter 0 e vai até o caracter 8 pulando de 2 em 2.
print(variavel[-10:-1]) #Começará a partir do caracter -1 e vai até o caracter -9.