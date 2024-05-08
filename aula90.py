#Generator expression, Iterables e Iterators em Python

iterable = ['Eu', 'Tenho', '__iter__'] # é ter os valores
iterator = iterable.__iter__()  #tem __iter__ e __next__ os dois underlines são chamados de 'dander'

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))