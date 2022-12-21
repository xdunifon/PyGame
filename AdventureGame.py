from CreatureClass import creature
from GameStateClass import game_state
import CreatureLibrary

'''
THIS IS THE MAIN PROFILE THAT THE GAME RUNS UNDER.
IT RELIES ON OTHER CLASSES TO PROVIDE GAMEPLAY STRUCTURE AND LOOPS.
'''

player_name = input("Enter your character's name:")
while len(player_name) > 18:
    player_name = input("Enter a name that's less than 19 characters: ")
Player = creature(player_name, 10, 10, False, False, 10)
print(Player.get_all())

gstate = game_state(False, True, "Forest", False)
#goblin = CreatureLibrary.create_goblin(1)
#print(goblin.get_all())



exitMsg = input("Enter 'exit' to quit: ")
while exitMsg != "exit":
    exitMsg = input("Enter 'exit' to quit: ")
