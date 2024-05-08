# isinstace - para saber se objeto é de determinado tipo (é instancia de)
lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
]


for item in lista:
    
    if isinstance(item, set):
        print('SET')
        item.add(5)
        print(item, isinstance(item, set))

    elif isinstance(item, str):
        print('STR')
        print(item.upper())

    elif isinstance(item, (int, float)): # É possível colocar dois tipos a serem validados.
        print('NUM')
        print(item, item * 2)
    else:
        print('OUTRO')
        print(item)