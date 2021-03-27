# Code by: Franco
# 27/03/2021 - 02:30
# Just give the credits
# --------- Let's code!

import pyqrcode 
import png 
from pyqrcode import QRCode 
import os

os.system('cls')
gerarqrcode = input("\n  >>> Digite o que deseja transformar em QR: ")

url = pyqrcode.create(gerarqrcode) 
url.png('.\myqr.png', scale = 10)