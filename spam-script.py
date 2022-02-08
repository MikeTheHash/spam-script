import pyautogui as pg
import time
#by MikeTheHash
#ATTENTION: The script work like an autoclicker


print(" ___ _ __   __ _ _ __ ___  _ __ ___   ___ _ __ ")
print("/ __| '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \ '__|")
print("\__ \ |_) | (_| | | | | | | | | | | |  __/ |   ")
print("|___/ .__/ \__,_|_| |_| |_|_| |_| |_|\___|_|")   
print("    |_|                        by MikeTheHash")         
print("\nATTENTION: The script work like an autoclicker")
print("------------------------------------------------")
input_user = input("What content do you want to spam? \n>")          
user_input = input("Do you want to start spam [y/n] \n>")
if user_input == "Y" or user_input == "y":
	time.sleep(5)
	while True:
		pg.write(input_user)
		pg.press("Enter")
