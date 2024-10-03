import json
from aula127 import CAMINHO_ARQUIVO, Pessoas

with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    dados = json.load(arquivo)

    p1 = Pessoas(**dados[0])
    p2 = Pessoas(**dados[1])
    p3 = Pessoas(**dados[2])

    print(p1.nome)
    print(p2.nome)
    print(p3.nome)
