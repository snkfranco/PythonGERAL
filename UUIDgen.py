import random
import string
import os

class Franco:
    def uuidgen(self):
        print('\n\n UUID GENERATOR')
        input('\n Pressione enter para gerar UUID')
        os.system('cls')
        listasenha = ['a','b','c','d','e','f','1','2','3','4','5','6','7','8','9']
        x1 = ''.join(random.choice(listasenha) for _ in range(8))
        x2 = ''.join(random.choice(listasenha) for _ in range(4))
        x3 = ''.join(random.choice(listasenha) for _ in range(3))
        x4 = ''.join(random.choice(listasenha) for _ in range(4))
        x5 = ''.join(random.choice(listasenha) for _ in range(12))
        print('\n\n UUID GENERATED\n')
        print(' '+x1+'-'+x2+'-4'+x3+'-'+x4+'-'+x5)

Frank = Franco()
Frank.uuidgen()