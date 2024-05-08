# dir, hasattr e getattr em Python
string = 'Luiz'
metodo = 'lower'

#dir trás todos os atributos dentro do objeto.
#hasattr checa se um determinado objeto tem um nome lá dentro.
#getattr pega o metodo como string e 

# print(string)

if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo)())
    print(string.upper())
else:
    print('Não existe o método', metodo)