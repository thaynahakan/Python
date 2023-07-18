#Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados
# da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da bragantino.

tupla = (' Botafogo',' Palmeiras', ' Fluminense',  ' Atlético-MG',
' Cruzeiro ', ' Flamengo', ' Athletico-PR',' São Paulo ',' Santos ',
' Grêmio', ' Fortaleza',' Bragantino',' Bahia' ,' Cuiabá',
'Internacional','Goiás',' Vasco', ' Corinthians',' América-MG',
' Coritiba')
#A)
print(f' A tabela de colocação é a seguinte: {tupla}')
#B)
print('=-'*10)
print(f' Os 5 primeiros times são:')
for cont in range(0,5):
    print(f'{cont+1}º colocado o time {tupla[cont]} ')
print('=-'*10)
#C)
print(f' Os ultimos quatro colocados são:{tupla[-4:]}')
print('=-'*10)
print('Os times em Ordem ALFABÉTICA:')
print(sorted(tupla))
print('=-'*10)
#D)
print(f' O Goiás está na posição', tupla.index('Goiás'))
