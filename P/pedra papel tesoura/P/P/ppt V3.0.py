'''Bom, pra começar, aqui está o terceiro projeto de Pedra, Papel e Tesoura.
Aqui usando o PySimpleGUI, eu estou em apredizado nesse framwork, mas... o projeto foi bem divertido
gostei muito do resultado, mesmo que tenha sido simples, mas foi bem gratificante ter consluido.
nada de segredo, mas apenas uma pequena interface para jogar pedra papel e tesoura de forma pratica.'''


import PySimpleGUI as sg
from random import choice


#parte da maquina
def jogada_da_maquina():
    opcoes = ['Pedra', 'Papel', 'Tesoura']
    jogadas = choice(opcoes)
    return jogadas
    
#layout
sg.theme("DarkBlue9")
layout = [
    [sg.Text('FAÇA A SUA JOGADA')],
    [sg.Text('------------------------------------------------')],
    [sg.Text(size = (50,4), key = '-OUTPUT-' )],
    [sg.Button('Pedra', size = (10,1)), sg.Button('Papel', size = (10,1)), sg.Button('Tesoura', size = (10,1))],
    [sg.Button('Sair', size = (50,1))]
]

#janela
janela = sg.Window('Jogo do P/P/T', layout, size = (300, 200))

#ler os eventos
while True:
    eventos, valores = janela.read()

    if eventos == sg.WIN_CLOSED or eventos == 'Sair':
        break

    jogada_maquina = jogada_da_maquina()

    if eventos == 'Pedra':
        if jogada_maquina == 'Pedra':
            resultado = 'Empate'
        elif jogada_maquina == 'Papel':
            resultado = 'Você perdeu!'
        else:
            resultado = 'Você ganhou!'
    elif eventos == 'Papel':
        if jogada_maquina == 'Pedra':
            resultado = 'Você ganhou!'
        elif jogada_maquina == 'Papel':
            resultado = 'Empate'
        else:
            resultado = 'Você perdeu!'
    else: #tesoura
        if jogada_maquina == 'Pedra':
            resultado = 'Você perdeu!'
        elif jogada_maquina == 'Papel':
            resultado = 'Você ganhou!'
        else:
            resultado = 'Empate'

    janela ['-OUTPUT-'].update(f'Voce jogou {eventos}.\nComputador jogou {jogada_maquina}.\nLogo o resultado é {resultado}')


