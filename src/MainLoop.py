from CreatureClass import creature, player
from GameStateClass import game_state
import CreatureLibrary
from CombatLoop import combat_loop_top

'''
THIS IS THE MAIN PROFILE THAT THE GAME RUNS UNDER.
IT RELIES ON OTHER CLASSES TO PROVIDE GAMEPLAY STRUCTURE AND LOOPS.
'''

#GAME START AND SETUP
player_name = input("Enter your character's name:")
while len(player_name) > 18:
    player_name = input("Enter a name that's less than 19 characters: ")
Player = player(player_name, 10, 6, 6, {"Health Potion":3})
print(Player.get_all())

#SETUP GAME STATE
gstate = game_state(False, True, "Forest", False)

#COMBAT TEST
goblin1 = CreatureLibrary.create_goblin(1)
goblin2 = CreatureLibrary.create_goblin(2)
goblin3 = CreatureLibrary.create_goblin(3)
enemies = [goblin1, goblin2, goblin3]
combat_loop_top(Player, enemies)

#HANDLES EXIT - DEBUG
exitMsg = input("Enter 'exit' to quit: ")
while exitMsg != "exit":
    exitMsg = input("Enter 'exit' to quit: ")
