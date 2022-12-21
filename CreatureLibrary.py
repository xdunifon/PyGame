from CreatureClass import creature

'''
THIS FILE IS A LIBRARY THAT HOLDS EVERY CREATURE IN THE GAME AND THEIR RELEVENT STATS
EACH CREATURE IS CREATED USING THE CREATURE CLASS
'''

def create_goblin(num):
    return creature(f"Goblin{num}", 5, 8, True, True, 5)

def create_Torwell():
    return creature("Torwell", 10, 10, False, False, 10)

def create_King_Leonard():
    return creature("King Leonard", 50, 16, False, False, 50)