#Versão 2.0. Melhorada, mais rápido, com melhor tratametendo de bugs, muito mais eficiete que a anterior
#Agora entre e teste a vontade!!
#Perceba que acrescentei laço de repetição While, e ainda por cima acrescentei o Try/except
#Justamente para tratamento de erros como textos e espaços
#A msg do contador é um bonus kkkkk, junto com as cores

#importando bibliotecas 
from random import choice
from time import sleep

#contador de erro
CONTADOR_DE_ERRO = 5

#definindo ações 
print('-=-'*10)
print('BEM-VINDO')
print('-=-'*10)

print('''\033[35mEscolha uma opção:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
[ 3 ] Sair
\033[m''')

while True:

    #Definindo recursos de escolhas do computador e jogador
    opcoes = ['Pedra', 'Papel', 'Tesoura']
    computador = choice(opcoes)


    print('-=-'*15)
    try:
        jogador = int(input('escolha:'))
    except ValueError:
        print('\033[31mOpção invalida, repita o processo\033[m')
        CONTADOR_DE_ERRO -= 1
        if CONTADOR_DE_ERRO == 0:
            print('\033[34mEu sei que você não é burro, tente novamente e siga todos os passos.\033[m')
        continue
    #caso jogador não ponha igual foi pedido, faz voltar ao inicio do laço

    if jogador <0 or jogador >= 4:
        print('\033[31mNão temos essa opção, tente novamente\033[m')
        CONTADOR_DE_ERRO -= 1
        if CONTADOR_DE_ERRO == 0:
            print('\033[34mEu sei que você não é burro, tente novamente e siga todos os passos.\033[m')
        continue

#parte de saída.
    if jogador == 3:
        break


    print(f'\033[35mJogador escolheu {opcoes[jogador]}\033[m')
    print(f'\033[35mComputador escolheu {computador}\033[m')

    #definindo resultados
    if computador == 'Pedra':
        if jogador == 0:
            print('\033[33m--> Empate <--\033[m')
        elif jogador == 1:
            print('\033[32m--> Jogador venceu ! <--\033[m')
        elif jogador == 2:
            print('\033[31m--> Jogador perdeu... <--\033[m')

    elif computador == 'Papel':
        if jogador == 0:
            print('\033[31m--> Jogador perdeu... <--\033[m')
        elif jogador == 1:
            print('\033[33m--> Empate <--')
        elif jogador == 2:
            print('\033[32m--> Jogador venceu ! <--\033[m')

    elif computador == 'Tesoura': 
        if jogador == 0:
            print('\033[32m--> Jogador venceu ! <--\033[m')
        elif jogador == 1:
            print('\033[31m--> Jogador perdeu... <--\033[m')
        elif jogador == 2:
            print('\033[33m--> Empate <--\033[m')

print('CARREGANDO...')
sleep(3)
print('Volte sempre.')
