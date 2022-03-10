# Initialize imports
import pyautogui
from pynput.mouse import Listener
import keyboard  # using module keyboard
import time
import sys


def is_clicked(x, y, button, pressed):
    if pressed:
        print('Clicked ! ')  # in your case, you can move it to some other pos
        return False  # to stop the thread after click


def check_hotkey(hot_key):
    # Checks to see if hot key has been pressed
    if keyboard.is_pressed(hot_key):  # if key 'q' is pressed
        print('Hot key pressed!')
        sys.exit()
    else:
        pass

def set_up():
    # Retrieve hot key and interval time
    while True:
        try:
            hot_key = str(input("Please enter a hotkey/charater: "))
            timer = float(input("Please enter an interval in seconds 0.00 and above: "))
            if len(hot_key) == 1 and timer >= 0:
                break
            else:
                print("Please enter 1 character or a time more than 0")

        except ValueError:
            print("Please enter a valid input")

    print("Please left click the position you would like.")

    # Checks if mouse has been clicked
    with Listener(on_click=is_clicked) as listener:
        listener.join()

    # Records mouse position
    pos = pyautogui.position()


    return hot_key, timer, pos

# Gets hotkey and option
hot_key, timer, pos = set_up()

while True:
    check_hotkey(hot_key)
    pyautogui.moveTo(pos)
    pyautogui.click()
    check_hotkey(hot_key)
    time.sleep(timer)
