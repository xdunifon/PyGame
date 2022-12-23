import time

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
    
    for i, x in enumerate(enemies):
            print(f"{i+1}. {x.get_name()} ({x.get_dmg()} HP)")
    target = int(input("\nTarget (Number): "))-1
        
    while target < 0 or target >= len(enemies):
        print("Uhhhh.. are you sure you entered the right number? Try again")
        for i, x in enumerate(enemies):
            print(f"{i+1}. {x.get_name()} ({x.get_dmg()} HP)")
        target = int(input("\nTarget (Number): "))-1

    return target

#Main loop for player action selection
def player_turn(player, enemies):
    is_player_turn = True

    #Calls function that prompts user for target selection
    target = select_target(enemies)
    enemy_name = enemies[target].get_name()

    #player_turn == True
    while is_player_turn == True:
        action = input(f"\nYou're targeting {enemy_name}. What action will you take?\n1. Attack\n2. Compliment\n3. Change Target\n4. Run\n\nEnter option number: ")
        match action:
            case "1":
                print(f"You attack {enemy_name} for {str(player.get_dmg())} damage")
                time.sleep(2)
                if enemies[target].damage(player.get_dmg()) <= 0:
                    print(f"\nGood work, {enemy_name} is down")
                    enemies.pop(target)
                is_player_turn = False
                break
            case "2":
                comp = input(f"What will you say to compliment {enemy_name}?: ")
                print(f"\nYou look to {enemy_name} and say: {comp}")
                print(f"{enemy_name} blushes and their HP drops by {player.get_dmg()}")
                time.sleep(2)
                if enemies[target].damage(player.get_dmg()) <= 0:
                    print(f"\nGood work! {enemy_name} is down")
                    enemies.pop(target)
                is_player_turn = False
                break
            case "3":
                target = select_target(enemies)
                enemy_name = enemies[target].get_name()
                continue
            case "4":
                print("You run away!")
                time.sleep(2)
                exit()
            case _:
                print("I don't quite understand what you entered, try again")
                time.sleep(2)

#Main loop for the enemies turn
def enemy_turn(player, enemies):
    print("Now it's the enemies turn\n")
    time.sleep(2)

    for x in enemies:
        player.damage(x.get_dmg())
        print(f"{x.get_name()} attacked you for {x.get_dmg()} damage")
    time.sleep(2)

#Main loop for combat scenarios
def combat_loop(player, enemies):
    print("You're under attack!")
    time.sleep(2)

    while len(enemies) > 0:
        print("\n" + player.get_all())

        #Calls function that prompts user for action selection
        player_turn(player, enemies)

        #Calls function to initiate enemy turn as long as they aren't all dead
        if len(enemies) > 0:
            enemy_turn(player, enemies)