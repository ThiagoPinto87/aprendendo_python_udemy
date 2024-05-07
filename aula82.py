#def e lambda é a mesma coisa.

def executa(funcao, *args):
    return funcao(*args)


#Função 1
def soma(x, y):
    return x + y

#O print abaixo está executando uma função lambda que tem a mesma funcionalidade da Função 1 acima.
print(
    executa(
        lambda x, y: x + y,
        2, 3
    )
    )

###########################################################################

#função 2
def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

#O print abaixo está executando uma função lambda que tem a mesma funcionalidade da Função 2 acima.

duplica = executa(
    lambda m: lambda n: n * m,
    2
)

print(duplica(2))

print(
    executa(
        lambda *args: sum(args),
        1, 2, 3, 4, 5, 6, 7
    )
)