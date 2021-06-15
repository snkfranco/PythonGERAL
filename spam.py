#Coded by: Kyogin - Franco
#How to use: You need to have a file named : Spamtext (txt) in the same folder
#Requirements: pyautogui (pip install pyautogui)

import pyautogui
import time
import os

print('\n Você tem 5 segundos para entrar na tela desejada...')

time.sleep(5)

words = open("Spamtext.txt","r") 

contador = 0

for word in words:
    os.system('cls')
    pyautogui.typewrite(word)
    print("Comentário número: ", contador)
    time.sleep(1)
    pyautogui.press("enter")
    contador = contador + 1