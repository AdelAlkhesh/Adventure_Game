import time
import sys

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.03)

place_holder = "PlaceHolder"

delay_print(place_holder + "\n")
delay_print("Hello and welcome to " + place_holder + "!" + """\nThis is a text-based choose your own adeventure game where the choices you make affect the outcome and progression of the game.""")
time.sleep(0.5)
print()
delay_print("""You navigate this game by typing out your choices in the terminal when prompted to do so. \n""")
time.sleep(0.5)
print()
delay_print("""Choices will consist of: \n-Yes or no questions (Y/n) \n-Exploration options \n-Item pickups \n""")
print()
delay_print("""Try to take your time and explore the places you find yourself in. You never know what you might find!\n""")
time.sleep(0.5)
print()
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
print()
time.sleep(0.5)

delay_print("""It's well past midnight, and the raindrops pattering against your window rouse you from what was previously a blissful sleep. Blearly eyed and still half asleep, you turn in your bed, attempting to find a more comfortable position. That's when Your eyes notice the odd shape in the corner of your room. You can't quite make out the shape of it, but the oddity of it gnaws at you, and you sit up slightly, the haze of sleep slowly clearing away to give way to better sight. With growing anxiety, your mind begins to think of the worst case scenarios as you remember that you are home alone this weekend.""")
print()
print()

delay_print("You can make a choice here. 1. Go back to sleep  2. Call out to the shape\n")
choice = str(input("You choose: "))

if choice == '1': 
    print()
    delay_print("""You shake your head, smiling to yourself. You're only being paranoid. You turn over and lay your head back down, hoping to catch some more sleep before sunrise.\n""")
    delay_print("""A few minutes pass with nothing but the sound of rain against your window, and you begin to slowly relax, drifting back to sleep. However just as the warmth of sleep welcomes you back into its fold, you hear it, and it jolts you back awake and wide eyed. A scratching noise coming from the direction of your desk in the corner of the room, like a fingernail dragging slowly against the wood.\n""")
    print()
    delay_print("""Before you realize it, you're sitting up in bed, panic threatning to overwhelm you. Your wide eyes frantically search the dark room, unable to make out anything but silhuotted shapes, and noting to your silent horror, that the shape you saw earlier is no longer there.\n""")
    print()

    delay_print("CHOICE: 1.Call out to the darkness." + " " + "2.Get up and investigate the noise\n")

    choice = str(input("You choose: "))

    if choice == '1': 
        print()
        delay_print("""\"Who's there?\" You call out, your voice filling the empty room, sounding louder than you expected in your ears.\n""")
        delay_print("""There is initially no response from the room, but a few seconds later the noise persists. You sit there frozen in fear for a minute that feels like an eternity, that is until a tapping on the window makes you jump a little in your place. You turn to face the window but are met with nothing but rain drops against the glass, and somewhere in the back of your mind, you tell yourself that you must be hearing things because what could possibly be tapping against your window when your room is three stories up?\n""")
        print()
        delay_print("""As you sit there trying to process all that is happening to you, lightning strikes outside, and for just a brief instance, your room is flooded with light. What you see sends your heart beating hard against your chest, and before you can scream out, a deafening clap of thunder fills your ears, overwhelming your senses, but one image remains fixed in your mind: The pair of eyes that stared at you from across the room.""")








