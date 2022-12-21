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

#Main loop for combat scenarios
def combat_loop(player, enemies):
    player_turn = True
    print("You're under attack!")

    while len(enemies) > 0:
        print("\n" + player.get_all())
        print("It's your turn, select a target first then take action")
        
        for i, x in enumerate(enemies):
            print(f"{i+1}. {x.get_name()} ({x.get_dmg()} HP)")
        target = int(input("\nTarget (Number): "))-1
        
        while target < 0 or target >= len(enemies):
            print("Uhhhh.. are you sure you entered the right number? Try again")
            for i, x in enumerate(enemies):
                print(f"{i+1}. {x.get_name()} ({x.get_dmg()} HP)")
            target = int(input("\nTarget (Number): "))-1
        
        enemy_name = enemies[target].get_name()
        action = input(f"\nYou're targeting {enemy_name}. What action will you take?\n1. Attack\n2. Compliment\n3. Run\n4. Quit\n\nEnter option number: ")
        
        while player_turn == True:
            match action:
                case "1":
                    print(f"You attack {enemy_name} for {str(player.get_dmg())} damage")
                    if enemies[target].damage(player.get_dmg()) <= 0:
                        print(f"Good work, {enemy_name} is down")
                        enemies.pop(target)
                    player_turn = False
                    break
                case "2":
                    comp = input(f"What will you say to compliment {enemy_name}?: ")
                    print(f"\nYou look to {enemy_name} and say: {comp}\n{enemy_name} blushes and their HP drops by {player.get_dmg()}")
                    if enemies[target].damage(player.get_dmg()) <= 0:
                        print(f"\nGood work! {enemy_name} is down")
                        enemies.pop(target)
                    player_turn = False
                    break
                case "3":
                    print("You ran away")
                    return 0
                    break
                case "4":
                    print("You decided you don't wanna play anymore")
                    exit()
                    break
                case _:
                    action = input("I don't quite understand what you entered, try again: ")
        
        if len(enemies) > 0:
            print("Now it's the enemies turn\n")
            for x in enemies:
                player.damage(x.get_dmg())
                print(f"{x.get_name()} attacked you for {x.get_dmg()} damage")
        player_turn = True