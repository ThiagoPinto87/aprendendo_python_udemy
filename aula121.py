# Métodos em instâncias de classes Python
# Hard coded - É algo que foi escrito diretamente no código
class Carro:
    # Atributos ou parâmetros
    def __init__(self, nome):
        # self.nome = 'Fusca' # Hard coded
        self.nome = nome

    # Métodos
    # usa-se o "self" também para referenciar à instância que está sendo executada na classe.
    def acelerar(self):
        print(f'{self.nome} está acelerando...')


string = 'Luiz'
print(string.upper())

fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()

celta = Carro(nome='Celta')
print(celta.nome)
celta.acelerar()
