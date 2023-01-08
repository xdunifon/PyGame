import time
import DiceRoll
from CreatureClass import creature

'''
THIS FILE HOLDS SCRIPTS THAT RUN LOOPS FOR DIFFERENT TYPES
OF ENCOUNTERS, TYPICALLY SOCIAL OR COMBAT.
THEY RUN UNTIL THE ENCOUNTER IS COMPLETED, AFTER WHICH CONTROL
IS GIVEN BACK TO THE PRIMARY FILE
'''

#Returns true if all creatures have 0 or less hp
def all_dead(creatures):
    for x in creatures:
        if x.get_hp() >= 0:
            return False
    return True

#Returns selected target from given array of enemies
def select_target(enemies):
    print("It's your turn: select a target first, then take action")

    while True:
        #   i = enemy index and x = enemy object
        for i, x in enumerate(enemies):
            print(f"{i+1}. {x.get_name()} ({x.get_hp()} HP)")
        
        #Get target selection, ensures integer input
        try:
            target = int(input("\nTarget (Number): "))-1
        except ValueError:
            print("Please enter a number")
            time.sleep(1.5)
            continue
        if target < 0 or target >= len(enemies):
            print("Uhhh. are you sure you entered the right number? Try again")
            time.sleep(1)
        else:
            break

    return target

#Main loop for player action selection
def player_turn(player, enemies):

    #Calls function that prompts user for target selection
    target = select_target(enemies)
    enemy_name = enemies[target].get_name()

    #Case matches input for each possible action, uses "break" for correct input or "continue" for unknown default input
    while True:
        action = input(f"\nYou're targeting {enemy_name}. What action will you take?\n1. Attack\n2. Talk\n3. Health Potion\n4. Change Target\n5. Run\n\nEnter option number: ")
        match action:
            case "1":   #Attack
                #Calculate damage based on player's strength dice
                attack_dmg = DiceRoll.dx(player.get_str_die())
                print(f"You attack {enemy_name} for {attack_dmg} damage")

                time.sleep(2)

                #Check if enemy is at 0 hp or less, remove from combat if so
                if enemies[target].damage(attack_dmg) <= 0:
                    print(f"\n{enemy_name} is down.")
                    enemies.pop(target)
                return False   #return to enemies turn

            case "2":   #Talk
                #Get Player input for charisma attack
                player_talk = input(f"What will you say to {enemy_name}?: ")
                print(f"\nYou look to {enemy_name} and say: {player_talk}")
                time.sleep(1)

                #Calculate charisma attack based on player's charisma dice
                attack_dmg = DiceRoll.dx(player.get_chr_die())
                print(f"{enemy_name} is less inclined to fight and their HP drops by {attack_dmg}")
                
                time.sleep(2)

                #Check if enemy is at 0 hp or less, remove from combat if so
                if enemies[target].damage(attack_dmg) <= 0:
                    print(f"\n{enemy_name} is down.")
                    enemies.pop(target)
                return False   #return to enemies turn

            case "3":   #Health Potion
                healing = DiceRoll.d10()
                player.heal(healing)
                print(f"You heal yourself for {healing} HP")
                time.sleep(2)

                return False   #return to enemies turn

            case "4":   #Change Target
                #Call select_target and update enemy_name. Continue for another prompt
                target = select_target(enemies)
                enemy_name = enemies[target].get_name()
                continue
            case "5":   #Run
                #Use d2 for 50/50 chance to run away
                if DiceRoll.d2() != 1:
                    print("You ran away")
                    time.sleep(2)
                    return True
                else:
                    print("You failed to run away")
                    time.sleep(2)
                    return False    #return into enemies turn
            case _: #Catch all for any inapropriate input
                print("I don't quite understand what you entered, try again")
                time.sleep(2)
                continue

#Main loop for the enemies turn
def enemy_turn(player, enemies):
    print("Now it's the enemies turn\n")
    time.sleep(2)

    #Each enemy has str attack calculated and applied
    for x in enemies:
        attack_dmg = DiceRoll.dx(x.get_str_die())
        player.damage(attack_dmg)
        print(f"{x.get_name()} attacked you for {attack_dmg} damage")
    time.sleep(2)

#Main loop for combat scenarios
def combat_loop_top(player, enemies):
    print("You're under attack!")
    time.sleep(2)

    while len(enemies) > 0:
        print("\n" + player.get_all())

        #Calls function that prompts user for action selection. Returns true if player runs away
        player_ran_away = player_turn(player, enemies)
        if player_ran_away:
            break

        #Calls function to initiate enemy turn as long as they aren't all dead
        if len(enemies) > 0:
            enemy_turn(player, enemies)