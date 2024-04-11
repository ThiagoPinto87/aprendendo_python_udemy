#Conversão de tipos.
#Converte um tipo em outro.

#'str', 'int, 'float', 'bool' são tipos imutáveis, há tipos mutáveis.

print('1', type('1'))
print(int('1'), type(int('1')))

print(float('1') + 1, type(float('1') + 1))

print(bool(''))     #sem nada
print(bool(' '))    #com espaço

print(str(11) + 'b')