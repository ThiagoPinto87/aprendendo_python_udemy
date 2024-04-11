# if / elif / else

entrada = input('Você quer entrar ou sair? ')


if entrada == 'entrar':
    print('Você entrou no sistema.')
    print('1234')

elif entrada == 'sair':
    print('Você SAIU do sistema.')

else:
    print('Digite um valor válido (entrar ou sair).')

print('FORA DOS BLOCOS')