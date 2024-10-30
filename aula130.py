# method vs @classmethod vs @staticmethod

# method - self, método de instância (sempre terá um self  )
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)

class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        # setter, ele está configurando um valor do atributo 'user' da função '__init__'
        self.user = user

    def set_password(self, password):
        # setter, é o que o set_user, ele está configurando um valor no atributo da função '__init__'.
        self.password = password

    # Anotação: qualquer metodo que for usar self, esse método é um método de instancia. Não há outro jeito.

    @classmethod
    def create_with_auth(cls, user, password):  # cria enquanto autentica.
        connection = cls()  # Neste caso ele está criando a classe já usando ela, de modo que
        connection.user = user
        connection.password = password
        return connection

    @staticmethod  # São metodos que possuem simples funções dentro da classe.
    def log(msg):
        print('LOG:', msg)

    def connection_log(msg):
        print('LOG:', msg)


# Usando a Classe instanciada:
c1 = Connection()
c1.set_user('luiz')
c1.set_password('123')
print(c1.user)
print(c1.password)


# Usando o classmethod
# c1 = Connection.create_with_auth('luiz', '1234')
# print(c1.user)
# print(c1.password)

# # Usando staticmethod
# print(Connection.log('Essa é a mensagem de log'))
