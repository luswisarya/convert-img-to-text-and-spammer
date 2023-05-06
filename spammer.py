import time
import pyautogui
import keyboard
import win32api, win32con

while 1: 
    keyboard.wait('esc')
    mystring = "Selamat malam kak Asep, saya Vivi ingin menawarkan kesempatan jp 100%"
    keyboard.write(mystring)
    keyboard.press_and_release('enter')