from time import sleep
import pyperclip
import keyboard


s = input("Type Your String: ")
x = int (input("Number Of Times To Print: "))
z= int (input("Per Print Sleep: "))
pyperclip.copy(s)
while True:
    keyboard.press_and_release("ctrl+v")
    sleep(.600)
    keyboard.press('enter')
    sleep(z)
    x=x-1
    if x==0:
        break
