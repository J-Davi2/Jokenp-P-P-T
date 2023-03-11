#Um jogo simples que aprendi fazendo nos meus exercicios de python, achei que seria interessantemostralos
#vou aprimorando aos poucos
#Pode-se ver que usei o sleep e o randint. randint serviu para sorteio aleatorio da maquina para definir a escolha que jogaria contra o jogador
#Sendo assim, o If, Elif e else, para mostrar os caminhos tomados das jogadas
#uma simples apresentação doprograma usando os Prints
#E uma rápida finalizção.

#importando bibliotecas 
from random import choice
from time import sleep

#Definindo recursos de escolhas do computador 
opcoes = ['Pedra', 'Papel', 'Tesoura']
computador = choice(opcoes)

#definindo ações 
print('-=-'*10)
print('BEM-VINDO')
print('-=-'*10)

print('''Escolha uma opção:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
''')


#Definindo recursos de escolhas do computador e jogador
opcoes = ['Pedra', 'Papel', 'Tesoura']
computador = choice(opcoes)



jogador = int(input('escolha:'))
#parte de saída.


print(f'Jogador escolheu {opcoes[jogador]}')
print(f'Computador escolheu {computador}')

#definindo resultados

if computador == 'Pedra':
    if jogador == 0:
        print('--> Empate <--')
    elif jogador == 1:
        print('--> Jogador venceu ! <--')
    elif jogador == 2:
        print('--> Jogador perdeu... <--')

        
elif computador == 'Papel':
    if jogador == 0:
        print('--> Jogador perdeu... <--')
    elif jogador == 1:
        print('--> Empate <--')
    elif jogador == 2:
        print('--> Jogador venceu ! <--')

elif computador == 'Tesoura': 
    if jogador == 0:
        print('--> Jogador venceu ! <--')
    elif jogador == 1:
        print('--> Jogador perdeu... <--')
    elif jogador == 2:
        print('--> Empate <--')

print('CARREGANDO...')
sleep(3)
print('Volte sempre.')




