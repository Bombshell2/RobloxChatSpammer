from textwrap import wrap
import time
from pynput.keyboard import Key, Controller
import pyautogui
import sys
import json
from pynput import keyboard as listen
#check python version, yell at user if not <= 3.4
if sys.version_info[0] < 3 or sys.version_info[1] < 4:
    raise Exception("Must be using Python Version <= 3.4, please update at https://www.python.org/downloads/ OR run 'py -3 main.py' instead.")
pause = False
config = json.load(open("config.json", "r"))
def on_press(key):
    global pause,config
    try:
        #toggle pause when pipe is pressed
        if key.char == config["pausekey"]:
            pause = not pause
            if pause:
                print("[Paused]")
            else:
                print("[Unpaused]")
    except AttributeError:
        print()
keyboard = Controller()
print("Roblox Chat Spammer v1.0\nWritten by Bombshell2#8591")
message = "Enter name of txt file here, leave blank for " + config["defaultfile"] + ": "
filename = input(message)
if filename == "":
    filename = config["defaultfile"]
filepath = "files/" + filename
#open file and read one line, too lazy to add multiline support
file = open(filepath, "r")
text = file.readline()
#first result for how to cut string python, dont know if this is good lol
cut = wrap(text, config["messagelength"])
listener = listen.Listener(
    on_press=on_press)
listener.start()
print(len(cut), "Messages")
time.sleep(config["startdelay"])
for i in cut:
    time.sleep(1)
    while pause:
        time.sleep(0.1)
    time.sleep(0.5)
    pyautogui.press("/")
    pyautogui.write(i, interval=0.01)
    keyboard.press(Key.enter) #dont know why, but pyautogui has a skill issue with pressing enter on windows, someone pls fix.
