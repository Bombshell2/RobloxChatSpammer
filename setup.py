import os
import sys
if sys.version_info[0] < 3 or sys.version_info[1] < 4:
    raise Exception("Must be using Python Version <= 3.4, please update at https://www.python.org/downloads/ OR run 'py -3 setup.py'")
print("Installing Pynput...")
os.system("pip install pynput")
print("Installing PyAutoGui...")
os.system("pip install pyautogui")
print("Done!")
