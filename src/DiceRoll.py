import random

'''
THIS FILE HOLDS FUNCTIONS TO ROLL DICE IN THE RANGE D2,D4,D6,D8,D12,D20,D100
'''

#Rolls digital dice based on provided sides, at least 1 roll, and default modifier of 0
def dx(sides, num=1, modifier=0):
    roll = 0
    for x in range(0, num):
        roll += random.randint(1, sides)
    return roll+modifier

#Rolls digital d2 with at least 1 roll and a default modifier of 0
def d2(num=1, modifier=0):
    roll = 0
    for x in range(0,num):
        roll += random.randint(1,2)
    return roll+modifier

#Rolls digital d4 with at least 1 roll and default modifier of 0
def d4(num=1, modifier=0):
    roll = 0
    for x in range(0,num):
        roll += random.randint(1,4)
    return roll+modifier

#Rolls digital d6 with at least 1 roll and a default modifier of 0
def d6(num=1, modifier=0):
    roll = 0
    for x in range(0,num):
        roll += random.randint(1,6)
    return roll+modifier

#Rolls digital d8 with at least 1 roll and a default modifier of 0
def d8(num=1, modifier=0):
    roll = 0
    for x in range(0,num):
        roll += random.randint(1,8)
    return roll+modifier

#Rolls digital d10 with at least 1 roll and a default modifier of 0
def d10(num=1, modifier=0):
    roll = 0
    for x in range(0,num):
        roll += random.randint(1,10)
    return roll+modifier

#Rolls digital d12 with at least 1 roll and a default modifier of 0
def d12(num=1, modifier=0):
    roll = 0
    for x in range(0,num):
        roll += random.randint(1,12)
    return roll+modifier

#Rolls digital d20 with at least 1 roll and a default modifier of 0
def d20(num=1, modifier=0):
    roll = 0
    for x in range(0,num):
        roll += random.randint(1,20)
    return roll+modifier

#Rolls digital d100 with at least 1 roll and a default modifier of 0
def d100(num=1, modifier=0):
    roll = 0
    for x in range(0,num):
        roll += random.randint(1,100)
    return roll+modifier