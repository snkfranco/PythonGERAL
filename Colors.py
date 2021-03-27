#Code by Franco
# 27/03/201 - 03:03



import colorama
import os
os.system('cls')
print('\n')

print ('\033[30m  Preto')
print ('\033[31m  Vermelho')
print ('\033[32m  Verde')
print ('\033[33m  Amarelo/laranja') #Depende do terminal.
print ('\033[34m  Azul')
print ('\033[35m  Magenta/roxo') #Depende do terminal.
print ('\033[36m  Ciano')
print ('\033[37m  Cinza claro')

#Repare que a sintaxe também pode ser usando o +.
print ('\033[90m'+'  Aqui temos a cor cinza escuro')
print ('\033[91m'+'  Aqui temos a cor vermelho claro')
print ('\033[92m'+'  Aqui temos a cor verde claro')
print ('\033[93m'+'  Aqui temos a cor amarelo claro')
print ('\033[94m'+'  Aqui temos a cor azul claro')
print ('\033[95m'+'  Aqui temos a cor magenta claro')
print ('\033[96m'+'  Aqui temos a cor cyano claro')
print ('\033[97m'+'  Aqui temos a cor branca')

print ('\033[0m') #reset de cores - O terminal volta ao padrão.

#Repare que aqui uso " " ao invés de ' '. Também funciona!
#Para colocar em negrito, basta acrescentar \033[;1m
#Para colocar com o fundo colorido, basa colocar \033[(cor que voce deseja (90-97);7m
print ("\033[;1m"+" Negrito! ")
print("\n")
print ("\033[;7m"+"Aqui o texto está invertido")
print ("\033[91;7m"+"Também é possível inverter com cores") #Vermelho Escuro.
print ("\033[33;7m"+"Também é possível inverter com cores") #Amarelo/Laranja Claro.
print ("\033[93;7m"+"Também é possível inverter com cores") #Amarelo Escuro.
print ("\033[92;7m"+"Também é possível inverter com cores") #Verde Claro.
print ("\033[94;7m"+"Também é possível inverter com cores") #Azul Claro.
print ("\033[34;7m"+"Também é possível inverter com cores") #Azul Escuro.
print ("\033[95;7m"+"Também é possível inverter com cores") #Magenta Claro.
print ("\033[0m") #reset de cores
