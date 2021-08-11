import time
import sys

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)

place_holder = "PlaceHolder"

delay_print(place_holder + "\n")
delay_print("Hello and welcome to " + place_holder + "!" + "\nThis is a text-based choose your own adeventure game where the choices you make affect the outcome and progression of the game.")
time.sleep(0.5)
delay_print("You navigate this game by typing out your choices in the terminal when prompted to do so. \n")
time.sleep(0.5)
delay_print("Choices will consist of: \n-Yes or no questions (Y/n) \n-Exploration options \n-Item pickups \n")
delay_print("Try to take your time and explore the places you find yourself in. You never know what you might find!\n")
time.sleep(0.5)
delay_print("That's it for the tutorial. Good luck, and have fun!")
print()
print()
time.sleep(0.5)



print("----------------- CHARACTER CREATION -----------------")
time.sleep(0.5)
def starting_item_picker(): 
    starting_item = str(input("What is your starting item? You can pick one of the following (1,2,3): \n-1: " + book + "\n-2: " + stone + "\n-3: " + handle + "\nYour Choice?:"))
    if starting_item == '1':
        inventory.append(book)
    elif starting_item == '2':
        inventory.append(stone)
    elif starting_item == '3': 
        inventory.append(handle)
    else: 
       delay_print("\nYou can only pick one of the three. Try again")
       starting_item_picker()
    
inventory = []
book = "Dusty Old Book" 
stone = "Loden Stone"
handle = "Oddly-Shaped Handle"

name = input("What is your name? ")
time.sleep(0.5)


starting_item_picker()
time.sleep(0.5)

print()
delay_print("Alright, you are all set up, " + name +"! \nYou will start the game with the " + inventory[0])

print()
print()

delay_print("-----------------------------------------------------------------------")







