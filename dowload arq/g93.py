#Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

gerenciamento = dict()
partidas = []
gerenciamento['jogador'] = str(input('Nome do jogador:'))
jogos = int(input(f'Quantas partidas o {gerenciamento["jogador"]} jogou?'))
for g in range (0,jogos):
     partidas.append(int(input(f'Quantos gols {gerenciamento["jogador"]} fez na {g+1}* partida?')))

gerenciamento['gols'] = partidas[:]
gerenciamento['total'] = sum(partidas)

for  k, n in gerenciamento.items():
    print(f' - {k} tem valor {n}')

print('=-'*25)
print(f'   >>TABELA DE APROVEITAMENTO<<')
print(f' O jogador {gerenciamento["jogador"]}, jogou {len(partidas)} partidas.')
for n, m in enumerate(partidas):
     print(f' Na partida {n}, o Jogador fez {m} gols.')
print()
print(f' O valor total dos gols feitos durante o campeonato:{gerenciamento["total"]}')

print(gerenciamento)


#gerenciamento['gols']