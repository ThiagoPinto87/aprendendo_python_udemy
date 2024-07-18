# try, except, else e finally
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

# finally SEMPRE será executado no bloco de código.
# else será executado caso o código não dê erros.

try:
    print('ABRIR ARQUIVO')
    8/0
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('DIVIDIU ZERO')
except IndexError as error:
    print('IndexError')
except (NameError, ImportError):    # Pode colocar dois erros no mesmo except
    print('NameError, ImportError')
else:
    print('Não deu erro')
finally:
    print('FECHAR ARQUIVO')
