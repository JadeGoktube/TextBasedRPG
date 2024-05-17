import sys
import os
import time
import random

screen_width = 100


# Player Setup #

class Player:  # player class
    def __init__(self):
        self.name = ''
        self.gameover = False
        self.hp = 0
        self.atk = 0
        self.inventory = {'fish': 1, 'catnip': 1}  # inventory
        self.shoelace = 12
        self.location = 'b3'
        self.job = ' '


myPlayer = Player()


# myPlayer.inventory

# TITLE SCREEN #
def title_screen_selections():  # start menu links to various functions
    option = input("> ")
    if option.lower().strip() == 'play':
        setup_game()  # starts game prompts
    elif option.lower().strip() == 'help':
        help_menu()  # prints help menu
    elif option.lower().strip() == 'quit':
        sys.exit()  # exits
    while option.lower().strip() not in ["play", "help", "quit"]:
        print("Please enter a valid command.")
        option = input("> ")
        if option.lower().strip() == 'play':
            setup_game()
        elif option.lower().strip() == 'help':
            help_menu()
        elif option.lower().strip() == 'quit':
            sys.exit()


def title_screen():  # display title_screen_selections
    os.system('cls')  # clears all previous text
    print('####################################')
    print("#     Welcome to the Gato Game     #")
    print('####################################')
    print("              -  Play -              ")
    print("              -  Help -              ")
    print("              -  Quit -              ")
    print("              Game by Jade        ")
    title_screen_selections()


def help_menu():  # visual guide to controls
    print("####################################")
    print("#    Navigation and Interaction    #")
    print("####################################")
    print("- Use move, walk, go, travel or run")
    print("  to select the movement option")
    print("- Then use up, down, left, right, north, ")
    print("  south, east or west to input a direction")
    print("- Use examine, interact or look to investigate the room")
    print("- Use leave to try and exit when you find the door ")
    print("- Use info to view player information")
    print("- Use quit to exit the game")
    print("- Use 'm' or map to view map")
    print("- Use 'use' to use an item from your inventory")
    print('####################################')
    input('Press [enter] to close menu. ')
    title_screen_selections()


# MAP #

# PLAYER STARTS AT B3

# 1 2 3 4
# O O O O A
# O O X O B
# O O O O C
##########


ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'info'
SOLVED = False
ENEMY = ''
UP = "up", "north"
DOWN = "down", "south"
LEFT = "left", "right"
RIGHT = "right", "east"

solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
                 'b1': False, 'b2': False, 'b3': False, 'b4': False,
                 'c1': False, 'c2': False, 'c3': False, 'c4': False}
fight_places = {'a1': True, 'a2': True, 'a3': True, 'a4': True,
                'b1': True, 'b2': True, 'b3': True, 'b4': True,
                'c1': True, 'c2': True, 'c3': True, 'c4': True}

zonemap = {  # list of locations and their variables
    # b #
    'a1': {
        'ZONENAME': 'Study',  # area name
        'DESCRIPTION': 'This is the study, there is is a desk with a laptop and mouse.',  # area desc
        'SOLVED': False,  # area starts unsolved
        'ENEMY': 'mouse',  # enemy name
        'BOSS': 0,  # enemy number to correlate with a list of enemies
        'UP': "",
        'DOWN': "b1",
        'LEFT': " ",
        'RIGHT': "a2",
        'INSIDE': "O",  # map area sector
    },

    'a2': {
        'ZONENAME': 'Bedroom',
        'DESCRIPTION': "A bed, a desk, and a suspicious pillow?",
        'SOLVED': False,
        'ENEMY': 'pillow',
        'BOSS': 1,
        'UP': "",
        'DOWN': "b2",
        'LEFT': "a1",
        'RIGHT': "a3",
        'INSIDE': "O",
    },

    'a3': {
        'ZONENAME': 'Living Room',
        'DESCRIPTION': 'This is living room',
        'SOLVED': False,
        'ENEMY': 'pot',
        'BOSS': 2,
        'UP': " ",
        'DOWN': "a3",
        'LEFT': "a2",
        'RIGHT': "a4",
        'INSIDE': "O",
    },

    'a4': {
        'ZONENAME': 'Litter Box',
        'DESCRIPTION': 'This is the litter box, and the only place I get alone time',
        'SOLVED': False,
        'ENEMY': 'scoop',
        'BOSS': 3,
        'UP': " ",
        'DOWN': "b4",
        'LEFT': "a3",
        'RIGHT': " ",
        'INSIDE': "O",
    },
    # b #
    'b1': {
        'ZONENAME': 'Front Door',  # also exit to end game
        'DESCRIPTION': "Welcome to the front door, it's where the humans come and go from",
        'SOLVED': False,
        'ENEMY': 'doormat',
        'BOSS': 4,
        'UP': "a1",
        'DOWN': "c1",
        'LEFT': " ",
        'RIGHT': "b2",
        'INSIDE': "O",
    },

    'b2': {
        'ZONENAME': 'Hallway',
        'DESCRIPTION': 'The Hallway is the pathway to somewhere important..',
        'SOLVED': False,
        'ENEMY': 'carpet',
        'BOSS': 5,
        'UP': "a2",
        'DOWN': "c2",
        'LEFT': "b1",
        'RIGHT': "b3",
        'INSIDE': "O",

    },

    'b3': {
        'ZONENAME': 'Lounge',
        'DESCRIPTION': 'This is the Lounge, a very comfortable place to sit',
        'SOLVED': False,
        'ENEMY': 'sofa',
        'BOSS': 6,
        'UP': "a3",
        'DOWN': "c3",
        'LEFT': "b2",
        'RIGHT': "b4",
        'INSIDE': "H",
    },

    'b4': {
        'ZONENAME': 'Bathroom',
        'DESCRIPTION': 'The bathroom, pretty shiny and with a nice fresh roll of rare toilet paper.',
        'SOLVED': False,
        'ENEMY': 'tp',
        'BOSS': 7,
        'UP': "a4",
        'DOWN': "c4",
        'LEFT': "b3",
        'RIGHT': " ",
        'INSIDE': "O",
    },
    # c #
    'c1': {
        'ZONENAME': 'Greenhouse',
        'DESCRIPTION': 'Welcome to the Greenhouse, I just like the smell, and sun.',
        'SOLVED': False,
        'ENEMY': 'ladybug',
        'BOSS': 8,
        'UP': "b1",
        'DOWN': " ",
        'LEFT': " ",
        'RIGHT': "c2",
        'INSIDE': "O",
    },

    'c2': {
        'ZONENAME': 'Dining Room',
        'DESCRIPTION': 'This is the Dining Room, where Milo the Dog likes to scavange for scraps.',
        'SOLVED': False,
        'ENEMY': 'dog',
        'BOSS': 9,
        'UP': "b2",
        'DOWN': " ",
        'LEFT': "c1",
        'RIGHT': "c3",
        'INSIDE': "O",
    },

    'c3': {
        'ZONENAME': 'Kitchen',
        'DESCRIPTION': 'The Kitchen, home of the vibrating hell spawn box',
        'SOLVED': False,
        'ENEMY': 'fridge',
        'BOSS': 10,
        'UP': "b3",
        'DOWN': " ",
        'LEFT': "c2",
        'RIGHT': "c4",
        'INSIDE': "O",
    },

    'c4': {
        'ZONENAME': 'Windowsill',
        'DESCRIPTION': 'Jumping up to this Windowsill always impresses the humans',
        'SOLVED': False,
        'ENEMY': 'reflection',
        'BOSS': 11,
        'UP': "b4",
        'DOWN': " ",
        'LEFT': "c3",
        'RIGHT': " ",
        'INSIDE': "O",
    },

}


# ENEMY #
class Enemy:
    def __init__(self, name, hp, atk, loot):
        self.name = name
        self.hp = int(hp)
        self.atk = int(atk)
        self.loot = loot


LootDistribution = []  # list of 1-12 for each boss's loot drop
for i in range(12):
    LootDistribution.append('')

# randomly distributes 4 catnip and 8 fish to each boss loot table's assigned number
CatnipLoot = 0
while CatnipLoot != 4:
    for i in range(12):
        if LootDistribution[i] == 'catnip' or CatnipLoot == 4:
            if LootDistribution[i] != 'catnip':
                LootDistribution[i] = 'fish'
        else:
            if random.randint(1, 3) == 3:
                CatnipLoot += 1
                LootDistribution[i] = 'catnip'
            else:
                LootDistribution[i] = 'fish'

mouse = Enemy('mouse', 200, 10, LootDistribution[0])
pillow = Enemy('pillow', 200, 10, LootDistribution[1])
pot = Enemy('pot', 300, 5, LootDistribution[2])
scoop = Enemy('scoop', 100, 20, LootDistribution[3])
doormat = Enemy('doormat', 300, 20, LootDistribution[4])
carpet = Enemy('carpet', 300, 10, LootDistribution[5])
sofa = Enemy('sofa', 300, 25, LootDistribution[6])
tp = Enemy('tp', 100, 30, LootDistribution[7])
ladybug = Enemy('ladybug', 100, 5, LootDistribution[8])
dog = Enemy('dog', 400, 20, LootDistribution[9])
fridge = Enemy('fridge', 600, 5, LootDistribution[10])
reflection = Enemy('reflection', 400, 10, LootDistribution[11])
# enemy list for reference in combat system
Enemies = [mouse, pillow, pot, scoop, doormat,
           carpet, sofa, tp, ladybug, dog, fridge,
           reflection]


# GAME INTERACTIVITY #


def print_location():  # consistent way of printing the location
    print('\n' + ('#' * (4 + len(zonemap[myPlayer.location]["ZONENAME"]))))
    print('# ' + (zonemap[myPlayer.location]["ZONENAME"]).upper() + ' # ')
    print('##' + str(('#' * (len(zonemap[myPlayer.location]["DESCRIPTION"])) + '## ')))
    print('# ' + zonemap[myPlayer.location]["DESCRIPTION"] + ' # ')
    print('#' * (4 + len(zonemap[myPlayer.location]["DESCRIPTION"])))


def prompt():  # main block loop of game, takes inputs and processes them
    print('\n' + '===========================')
    print("What would you like to do?")
    action = input("> ")
    acceptable_actions = ["move", "walk", "go", "travel", "quit", "examine", "interact", "look", "m",
                          "use", "quit", "help", "map", "info", "leave", "cheat"]
    # if myPlayer.shoelace >= 12:
    # print('This seems like enough shoelaces hmm maybe I can use these to get out...')
    while action.lower().strip() not in acceptable_actions:
        print('Unknown action, Please try again.\n')
        action = input("> ")
    if action.lower().strip() == "quit":
        sys.exit()
    elif action.lower() in ["move", "walk", "go", "travel"]:
        player_move(action.lower())
    elif action.lower().strip() in ["examine", "interact", "look"]:
        player_examine()  # ISSUE removed player_examine(action.lower().strip())
    elif action.lower().strip() == "info":
        player_info(action.lower().strip())
    elif action.lower().strip() == "help":  # except here
        print("####################################")
        print("#    Navigation and Interaction    #")
        print("####################################")
        print("- Use move, walk, go, travel or run")
        print("  to select the movement option")
        print("- Then use up, down, left, right, north, ")
        print("  south, east or west to input a direction")
        print("- Use examine, interact or look to investigate the room")
        print("- Use leave to try and exit when you find the door ")
        print("- Use info to view player information")
        print("- Use quit to exit the game")
        print("- Use 'm' or map to view map")
        print("- Use 'use' to use an item from your inventory")
        print('####################################')
        input('Press [enter] to close menu. ')
        prompt()
    elif action.lower().strip() in ["m", "map"]:
        print("==================================")
        print("X means it has been completed.")
        print("H means your current location.")
        print("O means it hasn't been completed.")
        print("==================================")
        print("###########")  # prints map by determining each zone's completion
        print('# ' + zonemap['a1']["INSIDE"] + ' ' + zonemap['a2']["INSIDE"] + ' '
              + zonemap['a3']["INSIDE"] + ' ' + zonemap['a4']["INSIDE"] + ' #')
        print('# ' + zonemap['b1']["INSIDE"] + ' ' + zonemap['b2']["INSIDE"] + ' '
              + zonemap['b3']["INSIDE"] + ' ' + zonemap['b4']["INSIDE"] + ' #')
        print('# ' + zonemap['c1']["INSIDE"] + ' ' + zonemap['c2']["INSIDE"] + ' '
              + zonemap['c3']["INSIDE"] + ' ' + zonemap['c4']["INSIDE"] + ' #')
        print('###########')

    elif action.lower() == 'use':
        print(myPlayer.inventory)
        print("What will you use? ")
        item = input("> ")
        if item.lower() in myPlayer.inventory and myPlayer.inventory[item.lower()] > 0:
            myPlayer.inventory[item.lower()] -= 1
            if item.lower() == 'catnip':
                print("You just received +20 attack damage.")
                myPlayer.atk += 20
            else:
                print("You just received +50 health.")
                myPlayer.hp += 50


    elif action.lower() == 'leave':
        if myPlayer.shoelace == 12 and zonemap[myPlayer.location]['ZONENAME'] == 'Front Door':
            win()
        elif myPlayer.shoelace == 12:  # player has enough shoelaces but is in wrong room
            print("You can't leave the room when there isn't a door out.")
        elif zonemap[myPlayer.location][
            'ZONENAME'] == 'Front Door':  # player does not have enough shoelaces but is in right room
            print("Pfft, you think I'll let you go with that many laces.")
            print("Bring back more and I just may consider it...")
        else:
            print(
                "There isn' t a door to escape through.")  # player does not have enough shoelaces and is incorrect room


# PLAYER OPTIONS #
def player_move(
        myaction):  # process inputs of direction and setting destination as well as error messages for out of bounds
    print("Where would you like to " + myaction + " to?")
    destination = input("> ")
    if destination in ["up", "north"]:
        if zonemap[myPlayer.location]["UP"] != " ":
            destination = zonemap[myPlayer.location]["UP"]  # moves player to what is defined in the UP section
            movement_handler(destination)
        else:
            print("The path is blocked")
            prompt()
    elif destination in ["down", "south"]:
        if zonemap[myPlayer.location]["DOWN"] != " ":
            destination = zonemap[myPlayer.location]["DOWN"]
            movement_handler(destination)
        else:
            print("The path is blocked")
            prompt()
    elif destination in ["left", "west"]:
        if zonemap[myPlayer.location]["LEFT"] != " ":
            destination = zonemap[myPlayer.location]["LEFT"]
            movement_handler(destination)
        else:
            print("The path is blocked")
            prompt()
    elif destination in ["right", "east"]:
        if zonemap[myPlayer.location]["RIGHT"] != " ":
            destination = zonemap[myPlayer.location]["RIGHT"]
            movement_handler(destination)
        else:
            print("The path is blocked")
            prompt()
    elif destination.lower() == 'back':
        prompt()
    else:
        player_move(myaction)


def movement_handler(destination):  # prints new location, sets new location for myPlayer.location
    if zonemap[myPlayer.location]['SOLVED'] == True:
        zonemap[myPlayer.location]['INSIDE'] = 'X'  # sets zone to X when solved
    else:  # sets player current location to H
        zonemap[myPlayer.location]['INSIDE'] = 'O'
    print("\n" + "You have moved to the " + destination + ".")
    myPlayer.location = destination
    zonemap[myPlayer.location]['INSIDE'] = 'H'
    print_location()


def player_examine():  # checks for enemies
    if zonemap[myPlayer.location]['SOLVED']:
        print("There is nothing new here anymore")  # if already solved prints
    else:
        print("Look out! There's a " + str(
            zonemap[myPlayer.location]['ENEMY']) + '!\n')  # if zone not solved and examine is run
        loop = True
        while loop == True:  # combat initiation loop
            print("Would you like to Fight or Run? ")
            action = str(input("> "))
            if str(action.lower().split()) == "['run']":  # moves player back into the room (state before examine)
                print("You got away safely...")
                time.sleep(1)
                print_location()
                loop = False
                prompt()
            elif str(action.lower().split()) == "['fight']":  # initiates fight
                loop = False
                player_fight(action.lower(), zonemap[myPlayer.location]['BOSS'])
            else:
                print('Unknown action, Please try again.\n')  # error message for invalid input


def player_info(info):  # shows all player stats, location and inventory
    print("You are " + myPlayer.name + " the " + myPlayer.job + " gato.\n" +
          "Your stats are: \n" + "HP: " + str(myPlayer.hp) + "\n" + "ATK: " +
          str(myPlayer.atk) + "\n" + "INVENTORY: " + str(myPlayer.inventory) + "\n" + "SHOELACES:" +
          str(myPlayer.shoelace) + "\n" + "LOCATION: " + zonemap[myPlayer.location]['ZONENAME'])


def player_fight(command, enemy):  # combat
    if Enemies[enemy].hp >= 0:
        temp = myPlayer.hp
        while command.lower().strip() == "fight" and int(Enemies[enemy].hp) > 0:
            print("##################")
            print("#     Attack     #")
            print("#       Bag      #")
            print("##################")
            print("The enemy has " + str(Enemies[enemy].hp) + "hp")
            print("Are you gonna ATTACK or BAG? ")
            move = input("> ")
            if move.lower().strip() == "attack":
                dmg = myPlayer.atk
                hit = random.randint(1, 10)  # sets 10% chance of miss
                if hit == 1:
                    print("Oh no! You MISSED!")  # miss message
                else:
                    Enemies[enemy].hp = Enemies[enemy].hp - dmg  # calc enemy hp
                    print("You did " + str(dmg) + " to " + Enemies[enemy].name)
                hit = random.randint(1, 10)
                time.sleep(0.7)
                if hit == 1:
                    print("The Enemy MISSED!")
                else:
                    print(str(Enemies[enemy].name) + " did " + str(Enemies[enemy].atk) + " damage to you!")
                    myPlayer.hp = myPlayer.hp - Enemies[enemy].atk
                time.sleep(0.7)
                if Enemies[enemy].hp < 0:
                    Enemies[enemy].hp = 0
                print("They have " + str(Enemies[enemy].hp) + "hp left.")
                time.sleep(0.7)
                if myPlayer.hp < 0:
                    myPlayer.hp = 0
                print("You have " + str(myPlayer.hp) + " health left.")
                time.sleep(0.7)
                if myPlayer.hp <= 0:  # player dies
                    time.sleep(3.5)
                    print("You lost all of your hp...")
                    time.sleep(1)
                    print("...")
                    time.sleep(1)
                    print("*COUGH*")
                    time.sleep(1)
                    print("...")
                    time.sleep(1)
                    print("YOU FAILED")
                    time.sleep(5)
                    quit()


            elif move.lower().strip() == "bag":  # player inventory
                print(myPlayer.inventory)
                bag = True
                while bag == True:
                    print("What will you use? Input 'back' to return")
                    item = input('> ')
                    if item.lower() == 'catnip' and myPlayer.inventory[item.lower()] > 0:  # use catnip to boost atk
                        print("You just received +20 attack damage.")
                        myPlayer.atk += 20
                        myPlayer.inventory[item] -= 1
                        bag = False
                    elif item.lower() == 'fish' and myPlayer.inventory[item.lower()] > 0:  # use fish to boost hp
                        print("You just received +50 health.")
                        myPlayer.hp += 50
                        myPlayer.inventory[item] -= 1
                        bag = False
                    elif item.lower() == 'back':
                        bag = False
                    else:
                        print("That isn't in your inventory.")

            else:
                print("Invalid move, please try again.")
        print("===========================")
        print(Enemies[enemy].name + " is defeated")  # enemy dies
        time.sleep(0.7)
        print("You been put back to full health.")  # sets player health to max
        myPlayer.hp = temp
        time.sleep(0.7)
        myPlayer.shoelace += 1  # adds a shoelace to myPlayer.shoelace
        print(str(zonemap[myPlayer.location]["ZONENAME"]) + " has been solved!")  # sets zone to solved
        time.sleep(1)
        print("You collected a shoelace and a " + Enemies[enemy].loot + "!")
        myPlayer.inventory[
            Enemies[enemy].loot] += 1  # adds loot item to player inventory (random 4/12 chance of catnip, rest is fish)
        zonemap[myPlayer.location]["SOLVED"] = True
        time.sleep(1)

        if myPlayer.shoelace == 12:  # when player defeats final enemy and collects last shoelace
            print("I think you got all of them...\n")
            print("Let's go find the front door and ask to 'leave'.")

    else:
        print("Maximum slap already achieved enemy is aliven't!")


# GAME FUNCTIONALITY #

def maingameloop():  # checks if game is finished (checks requirements)
    while myPlayer.gameover is False:
        prompt()
    if zonemap[myPlayer.location] == 'b1':
        if myPlayer.inventory['shoelace'] >= 12:
            myPlayer.gameover = True
            win()  # win message
        else:
            maingameloop()


def win():
    print('You bribe the door guardian by return- I mean... ')
    print('gifting him shoelaces you totally did not steal earlier and get outside.')

    time.sleep(5)
    print('Goodbye! YOU WON!')
    time.sleep(5)
    print("Thanks for playing! Input 'bye' to leave")

    finish_game = input("> ")
    if finish_game.lower() == 'bye':
        quit()
    while finish_game.lower() != 'bye':  # if player input is not valid
        print(finish + " is not an avaliable input")
        finish = input("> ")  # repeats bye input
        if finish_game.lower() == 'bye':
            quit()


def setup_game():
    os.system('cls')

    # Name #
    question1 = "Hello what is your name?\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()  # prints letters one by one
        time.sleep(0.04)  # print speed
    player_name = input("> ")  # displays an arrow > for your input
    myPlayer.name = player_name

    # CLASS #
    question2 = "What gato are you?\n"
    question2added = "(You can be a lazy, angry, fat or tabby gato.)\n"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)
    for character in question2added:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    player_job = input("> ")
    valid_jobs = ['lazy', 'angry', 'fat', 'tabby']
    if player_job.lower() in valid_jobs:
        myPlayer.job = player_job
        print("You are now a " + player_job + " gato!\n")
        if player_job == 'lazy':  # little messages to accompany each job/class choice
            print("mmm... me lazy... attacks will be VERY weak...")
        elif player_job == 'angry':
            print("angry gato will pack a punch!")
        elif player_job == 'tabby':
            print("tabby gato has balanced stats")
        elif player_job == 'fat':
            print("fat gato has a lot of hp with lower attack")

    while player_job.lower() not in valid_jobs:  # if player input is not valid
        print(player_job + " is not an available gato\n")
        player_job = input("> ")  # repeats job input
        if player_job.lower() in valid_jobs:
            myPlayer.job = player_job
            print("You are now a " + player_job + " gato!\n")

    # STATS # defines each class' stats
    if myPlayer.job == "fat":  # tank
        myPlayer.hp = 175
        myPlayer.atk = 75
        myPlayer.location = 'b3'
        myPlayer.game_over = False
    elif myPlayer.job == "lazy":  # does this even count as a tank? a blob
        myPlayer.hp = 200
        myPlayer.atk = 50
        myPlayer.location = 'b3'
        myPlayer.game_over = False
    elif myPlayer.job == "tabby":  # balanced
        myPlayer.hp = 125
        myPlayer.atk = 125
        myPlayer.location = 'b3'
        myPlayer.game_over = False
    elif myPlayer.job == "angry":  # attacker
        myPlayer.hp = 75
        myPlayer.atk = 175
        myPlayer.location = 'b3'
        myPlayer.game_over = False

    # Start #
    speech1 = "Welcome " + player_name + " the " + player_job + " to the Gato Game!\n"
    speech2 = "I hope it treats you well.\n"
    speech3 = "Try and get out of the house...\n"
    speech4 = "Good luck exploring!\n"

    for character in speech1:  # prints each bit of text with customised speeds
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
    for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
    for character in speech3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
    for character in speech4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
    time.sleep(2)

    os.system('cls')
    print("#######################")
    print("#   Let's start now   #")
    print("#######################")
    maingameloop()


title_screen()
