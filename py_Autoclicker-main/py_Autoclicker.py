import time
import keyboard
import pyautogui

  #  #####    ####   ###  #####   #####    #  #   #  #      
 #   #    #   #   #   #   #    #      #   ##  #   #   #     
#    #     #  ####    #   #####   #####  # #  #####    #
 #   #    #   #  #    #   #           #    #      #   #
  #  #####    #   #  ###  #      #####     #      #  #

print("This is a Python Autoclicker")
print("")
key = input("which key: ")
mouse = input("L.eft or R.ight: ").lower()
delay = 0.0001 #float(input("The delay between clicks in s (e.g. 0.1): "))

def left_Mouseclick():    
    pyautogui.leftClick()
    time.sleep(delay)
    
def right_Mouseclick():
    pyautogui.rightClick()
    time.sleep(delay) 

while True:
    if keyboard.is_pressed('esc'):
        print("program ended...")
        break
    
    if mouse == "l" and keyboard.is_pressed(key):
        left_Mouseclick()

    if mouse == "r" and keyboard.is_pressed(key):
        right_Mouseclick()



