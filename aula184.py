# Variáveis de ambiente com Python
# Para variáveis de ambiente
# Windows PS: $env:SENHA="SENHA ESCOLHIDA" | dir env:
# Linux e Mac: export NOME_VARIAVEL="VALOR" | echo $VARIAVEL
# Para obter o valor das variáveis de ambiente
# os.getenv ou os.environ['VARIAVEL']
# Para configurar variáveis de ambiente
# os.environ['VARIAVEL'] = 'valor'
# Ou usando python-dotenv e o arquivo .env
# pip install python-dotenv
# from dotenv import load_dotenv
# load_dotenv()
# https://pypi.org/project/python-dotenv/
# OBS.: sempre lembre-se de criar um .env-example
import os

from dotenv import load_dotenv  # type: ignore

load_dotenv()

# Imprime todas as variáveis de ambiente do sistema.
# print(os.environ)

# pega a variável de ambiente salvo.
print(os.getenv('BD_PASSWORD'))
