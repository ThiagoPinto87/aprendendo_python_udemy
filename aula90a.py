import sys

# Generator expression, Iterables e Iterators em Python
# Generator são funções que sabem pausar em determinada ocasião. Todo Generator é um iterator
# Iterator (é uma classe que tem iter e next). Todo Iterator NÃO é um Generator.

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)  # tem __iter__ e __next__
lista = [n for n in range(10000)] # a partir do momento em que se criou a lista ela já está salva inteira na memória, permitindo acessar seus valores pelo índice.
generator = (n for n in range(10000)) ### ESTE É UM GENERATOR EXPRESSION, POIS ESTÁ USANDO O PARENTESES. Com isso, ele irá aguardar ser pedido o valor a ele. O que não permite acessar a lista pelo índice, pois ele não conhece a lista inteira.

# print(lista)
# print(generator)

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

# print(next(generator))
# print(next(generator))
# print(next(generator))

for n in generator:
    print(n)