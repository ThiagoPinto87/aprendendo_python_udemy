# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo

# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.
#  🐍🤓🤯🤯🤯🤯

class Caneta:
    def __init__(self, cor):
        # private protected
        self.cor = cor
        # Por convenção, quando se inicia o atributo com o "_" ou "__" no começo, estamos informando a outro dev que o atributo
        # não deve ser usado, pois ele é protegido pela classe e deve ser usado somente dentro da classe.
        self._cor_tampa = None

    # property, é um metodo que se comporta como um atributo que pega o valor do atributo.
    @property
    def cor(self):
        print('ESTOU NO GETTER')
        return self._cor

    # O setter é um metodo que recebe um valor e altera o valor do atributo.
    # Isso pode ser usado inclusive para controlar o que o usuário pode fazer ou não, como
    # colocar condições ex.: "if valor < 2: print('valor não permitido.')"
    @cor.setter
    def cor(self, valor):
        print('ESTOU NO SETTER')
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa

    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor


caneta = Caneta('Azul')
caneta.cor = 'Rosa'
caneta.cor_tampa = 'Azul'
print(caneta.cor)
print(caneta.cor_tampa)
