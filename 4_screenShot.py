import pyautogui
import time
import string
import random

# generate random string
# can add while loop to take PS very given seconds or unlimited PS
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def ps_img():
    timer = int(input('enter countdown shot in seconds: '))
    time.sleep(timer)
    dot_png = ".png"
    result_name = id_generator(5, '0987654321abcdefghigklmnopqrstuvwxyz')

    im1 = pyautogui.screenshot()
    im2 = pyautogui.screenshot(result_name + dot_png)
    if im2 == result_name:
        print('Random name generated coincide, please try again.')
    else:
        print("File name generated", result_name + dot_png)


# invoke the function
ps_img()
