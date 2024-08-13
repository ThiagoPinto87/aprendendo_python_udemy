# Variáveis livres + nonlocal (locals, globals)
# print(globals())
# def fora(x):
#     a = x

#     def dentro():
#         # print(locals())
#         return a
#     return dentro


# dentro1 = fora(10)
# dentro2 = fora(20)

# print(dentro1())
# print(dentro2())


def concatenar(string_inicial):
    # Freevariavel (variável livre) pois ela está tanto nessa função como na de baixo.
    valor_final = string_inicial

    def interna(valor_a_concatenar=''):
        # nonlocal informa ao python que a variável valor_final está no escopo da função acima.
        nonlocal valor_final
        valor_final += valor_a_concatenar
        return valor_final
    return interna


c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
final = c()
print(final)
