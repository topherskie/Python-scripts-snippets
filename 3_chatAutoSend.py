import pyautogui
import time

# access pyautogui module
# automate the send btn for fb,instagram etc
# can do infinite loop
current_count = 0;
while current_count != 3:
    time.sleep(2)
    pyautogui.typewrite('testing')
    pyautogui.press('enter')
    current_count+=1

print('Total count reach:', current_count)
