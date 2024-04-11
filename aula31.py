"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 61  # velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada


# A convenção entre os desenvolvedores Python é que a variável criada em caixa alta é uma variável constante (não deve ser mudada)
RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

vel_carro_pass_radar = velocidade > RADAR_1

carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)

carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar


if vel_carro_pass_radar:
    print('Velocidade carro passou do radar 1')

if carro_passou_radar_1:
      print('Carro passou radar 1')

if carro_passou_radar_1 and vel_carro_pass_radar:
        print(f'MULTADO! Velocidade: {velocidade}KM/h.')
