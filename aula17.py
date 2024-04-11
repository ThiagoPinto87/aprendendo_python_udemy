# if / elif / else

condicao = 10 == 10

if condicao:
    print('Esse código é do "if"')

elif condicao:
    ... #a reticencias é a mesma coisa que pass. Essa reticencia chama-se elypise

elif condicao == False:
    print('Esse código é do elif')


#elif e else depende do if. O else tem que ser a ultima condição do bloco.


print('Terminou, fora do "if"')