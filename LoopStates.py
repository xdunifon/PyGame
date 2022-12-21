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
def combat_loop(enemies):
    while not all_dead(enemies):
        print("You're under attack! Select a target and take action")
        
        for i, x in enumerate(enemies):
            print(f"{i+1}. {x}")
        target = input("\nTarget (Number): ")
        
        while target < 0 or target > len(enemies)+1:
            print("Uhhhh.. are you sure you entered the right number? Try again")
            for i, x in enumerate(enemies):
                print(f"{i+1}. {x}")
            target = input("\nTarget (Number): ")
        
        action = input(f"You're targeting {enemies[target]}. What action will you take?\n1. Attack\n2. Compliment\n3. Run\n4. Give up\n\nEnter option number: ")
        