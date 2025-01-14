# Valores padrão e field em dataclasses
# doc: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass, field

# Usando field, posso criar valores padrões, posso ativar ou desativar comparação, entre outro.
# usando fields, mostra os meta dados da função (mostra as configurações dos campos).


@dataclass
class Pessoa:
    nome: str = field(
        default='MISSING', repr=False
    )
    sobrenome: str = 'Not sent'
    idade: int = 100
    enderecos: list[str] = field(default_factory=list)


if __name__ == '__main__':
    p1 = Pessoa()
    # print(fields(p1))
    print(p1)
