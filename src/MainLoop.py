from CreatureClass import creature, player
from GameStateClass import game_state
import CreatureLibrary
from CombatLoop import combat_loop_top
import os
import time
import pickle

'''
THIS IS THE MAIN PROFILE THAT THE GAME RUNS UNDER.
IT RELIES ON OTHER CLASSES TO PROVIDE GAMEPLAY STRUCTURE AND LOOPS.
'''
project_path = os.path.dirname(__file__)
print(project_path)

#Loads the data from the txt file into a player object and global game state object
def load_save(save_path):
    '''
    saved_file = open(save_path)
    saved_file.readline() #Takes up "Name" line
    name = saved_file.readline()
    saved_file.readline() #Takes up "Current Health" line
    hp = int(saved_file.readline())
    saved_file.readline() #Takes up "Max Health" line
    max_hp = int(saved_file.readline())
    saved_file.readline() #Takes up "Strength dice" line
    str_dice = int(saved_file.readline())
    saved_file.readline() #Takes up "Charisma dice" line
    chr_dice = int(saved_file.readline())
    saved_file.readline() #Takes up "Inventory" line
    inventory = saved_file.readline()
    '''
    with open(save_path, "rb") as save_file:
        combined = pickle.load(save_file)
        Player = combined[0]
        GState = combined[1]
        print(Player.get_all())

def save_game(Player, Gamestate):
    combined = [Player, Gamestate]
    with open(f"saves/{Player.get_name()}.txt", "wb") as save_file:
        pickle.dump(combined, save_file)

#Open a saved game or create a new one
def game_setup():
    print("WELCOME TO PYRIM\n---------------")
    
    while True:
        try:
            game_select = int(input("Enter '1' if you would like to create a new game and '2' if you would like to continue an existing one: "))
            if game_select == 1 or game_select == 2:
                break
            else:
                print("Please only enter 1 or 2")
                time.sleep(1)
        except ValueError or TypeError:
            print("Please only enter 1 or 2")
            continue

    if game_select == 2:
        player_name = input("Enter your saved character's name: ")
        for filename in os.scandir("src/saves"):
            if filename.name == f"{player_name.upper()}.txt":
                user_input = input(f"Game save for {player_name} found. Loading game...")
                time.sleep(2)
                return load_save(f"src/saves/{player_name.upper()}.txt")
                

game_setup()
#GAME START AND SETUP
player_name = input("Enter your character's name:")
while len(player_name) > 18:
    player_name = input("Enter a name that's less than 19 characters: ")
Player = player(player_name, 10, 10, 6, 6, {"Health Potion":3})
print(Player.get_all())

#SETUP GAME STATE
Gstate = game_state(False, True, "Forest", False)

#COMBAT TEST
goblin1 = CreatureLibrary.create_goblin(1)
enemies = [goblin1]
combat_loop_top(Player, enemies)

save_game(Player, Gstate)
load_save("saves/xav.txt")

#HANDLES EXIT - DEBUG
exitMsg = input("Enter 'exit' to quit: ")
while exitMsg != "exit":
    exitMsg = input("Enter 'exit' to quit: ")
