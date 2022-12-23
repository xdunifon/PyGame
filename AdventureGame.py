from CreatureClass import creature
from GameStateClass import game_state
import CreatureLibrary
import LoopStates

'''
THIS IS THE MAIN PROFILE THAT THE GAME RUNS UNDER.
IT RELIES ON OTHER CLASSES TO PROVIDE GAMEPLAY STRUCTURE AND LOOPS.
'''

player_name = input("Enter your character's name:")
while len(player_name) > 18:
    player_name = input("Enter a name that's less than 19 characters: ")
Player = creature(player_name, 10, 5, False, False)
print(Player.get_all())

gstate = game_state(False, True, "Forest", False)
goblin1 = CreatureLibrary.create_goblin(1)
goblin2 = CreatureLibrary.create_goblin(2)
goblin3 = CreatureLibrary.create_goblin(3)
#print(goblin.get_all())
enemies = [goblin1, goblin2, goblin3]
LoopStates.combat_loop(Player, enemies)

exitMsg = input("Enter 'exit' to quit: ")
while exitMsg != "exit":
    exitMsg = input("Enter 'exit' to quit: ")
