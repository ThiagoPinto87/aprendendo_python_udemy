"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
Não temos acesso a nomes de escopos internos nos escopos externos.
A palavra global faz uma variável do escopo externo ser a mesma no escopo interno.
"""

x = 1


def escopo():
    x = 10

    def outra_funcao():
        x = 11
        y = 2
        '''
        Ao executar esse módulo DEBUGANDO, observe na aba "CALL STACK", onde o empilhamento das funções vão ocorrendo uma após a outra onde todas estarão acima do módulo. Observe também que ao parar a execução do debug no 'print(x, y)' [abaixo], e clicar em cada empilhamento, você vai observar que a variável 'x' possui valores diferentes, isso ocorre justamente por causa do empilhamento dessas funções.
        '''
        print(x, y) # <- este 'print(9)x, y)' que foi citado no comentário acima.

    outra_funcao()
    print(x)


print(x)
escopo()
print(x)