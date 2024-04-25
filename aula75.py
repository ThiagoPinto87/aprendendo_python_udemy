'''
Exercício
Crie funções que duplicam, triplicam e quadruplicam o número recebido como parâmetro.
'''

def criar_mutiplicador(numero_multiplicador):
    def multiplicar(numero):
        return numero * numero_multiplicador
    return multiplicar

duplicar = criar_mutiplicador(4)
print(duplicar(2))