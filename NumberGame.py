# Made by: Franco
# https://github.com/Kyogin
# Requirements: colorama

from random import randint
import os
import sys
import colorama

contador = 0
while contador == 0:
    os.system('cls')
    print('\033[36m >>> ADIVINHE O NÚMERO <<< \033[m')
    
    x = randint(0,5)
    
    jogador = int(input("\n\033[33m Digite um número entre 0 a 5: \033[m"))

    if jogador == x:
        print('\n\033[32m Voce acertou!\033[m O número escolhido pela máquina também foi o\033[33m', x, '\033[m')
        
    else:
        print('\n\033[31m Voce errou!\033[m O número esolhido pela máquina foi o\033[33m', x,'\033[me o que voce escolheu foi o\033[33m', jogador, '\033[m')
    input('\n\n Pressione ENTER para tentar novamente ou feche o terminal para sair! Obrigado! ')
