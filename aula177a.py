# Aula sobre pathlib
# biblioteca
from pathlib import Path


#### GERANDO STRINGS COM OS CAMINHOS ####

# Pega o caminho para a pasta desse projeto.
caminho_projeto = Path()
# print(caminho_projeto.absolute())

# Pega o caminho do arquivo.
caminho_arquivo = Path(__file__)
# print(caminho_arquivo)


# Pega através do caminho do arquivo, sua pasta pai
# Isso é um pouco diferente do Path, pois caso haja subpastas em variável de ambiente, percebi que ele encontra melhor o caminho do arquivo.
caminho_arquivo = Path(__file__)
# print(caminho_arquivo.parent)

# Pega a pasta pai da pasta pai, e assim por diante.
# print(caminho_arquivo.parent.parent)

# Cria um novo caminho usando da variável 'caminho_arquivo' com o parent dele e criando o caminho ideias.
ideias = caminho_arquivo.parent / 'ideias'
# print(ideias)

# Pegar caminhos específicos dos sistemas operacionais.
# Pega o caminho no Desktop
# print(Path.home() / 'Desktop')


#### CRIANDO E MANIPULANDO ARQUIVOS E PASTAS ####


# Cria uma pasta, se a pasta já está criada, tem que usar a função exist_ok
caminho_pasta = Path.home() / 'Downloads' / 'Criando_Pasta'
caminho_pasta.mkdir(exist_ok=True)

# Criando uma subpasta.
subpasta = caminho_pasta / 'subpasta'
subpasta.mkdir(exist_ok=True)


# Cria/atualiza um arquivo.
arquivo = Path.home() / 'Downloads' / 'Criando_Pasta' / 'arquivo.txt'
print(arquivo)
arquivo.touch()


# Escreve em um arquivo (Atenção substitui o texto, "forma rápida")
arquivo = Path.home() / 'Downloads' / 'Criando_Pasta' / 'arquivo.txt'
arquivo.write_text('ESCREVENDO UM TEXTO GRANDÃO.', encoding='utf-8',)
print(arquivo)


# Escreve em um arquivo de forma avançada.
caminho_do_arquivo = Path.home() / 'Downloads' / 'Criando_Pasta' / 'arquivo.txt'
caminho_do_arquivo.touch()  # Criando um arquivo novo
caminho_do_arquivo.write_text('')  # Apagando qualquer informação


# Escrevendo de forma recursiva adicionando linhas.
with caminho_do_arquivo.open('a+') as file:
    file.write('Escrevendo em uma linha \n')
    file.write('Escrevendo em outra linha \n')


# Ler em um arquivo.
arquivo = Path.home() / 'Downloads' / 'Criando_Pasta' / 'arquivo.txt'
print(arquivo.read_text(encoding='UTF-8'))


# Apaga um arquivo.
arquivo = Path.home() / 'Downloads' / 'Criando_Pasta' / 'arquivo.txt'
print(arquivo)
# arquivo.unlink()
