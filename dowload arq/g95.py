#Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
#Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

cadastro = dict()
jogadores = list()
gol = []
while True:
    cadastro.clear()
    cadastro['nome'] = input('Nome:')
    part = int(input('Quantas partidas ele jogou?'))
    for c in range(0, part):
        gol.append(int(input(f'Quantos gols ele fez na partida {c+1}?')))
    cadastro["gol"] = gol[:]
    cadastro['total'] = sum(gol)
    jogadores.append(cadastro.copy())
    gol.clear()
    while True:
        cad = str(input(f' Quer cadastrar mais alguém?'))
        if cad in 'sSnN':
            break
        print(f' Responda apenas Sim ou Não.')
    if cad in 'nN':
        break


print(jogadores)
print('-'*40)
print(f'cod.', end='')
for j in cadastro.keys():
    print(f'{j:<15}', end='')
print()
print('-'*40)

for k, v in enumerate(jogadores):
    print(f'{k+1:>3} ',end='')
    for p in v.values():
        print(f'{str(p):<15}', end='')
    print()
print('-'*40)

while True:
    quer = int(input(f'Mostrar os dados de qual jogador[999 para]?'))
    if quer == 999:
        break
    if quer >= len(jogadores):
        print(f' Erro! Esse número {quer} não está cadastrado.')

    else:
        print(f' LEVANTAMENTO DO JOGADOR {jogadores[quer]["nome"]}')
        for i, g in enumerate(jogadores[quer]['gol']):
            print(f'No jogo {i+1} fez {g} gols.')
print('-'*40)
print('>>WELCOME TU D DIANGO<<')

