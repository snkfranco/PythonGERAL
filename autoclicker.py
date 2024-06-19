import mouse
import time

# Tempo de espera antes de começar, para você poder posicionar o mouse
print("Iniciando em 5 segundos...")
time.sleep(5)

print("Clicando...")

try:
    while True:
        mouse.click()
        time.sleep(0.0005)
except KeyboardInterrupt:
    print("Programa interrompido pelo usuário.")
