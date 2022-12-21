'''
THIS IS A PRIMARY FILE THAT HOLDS THE STRUCTURE FOR EVERY 
CREATURE IN THE GAME AND PROVIDES FUNCTIONS FOR MANIPULATING THEM
'''

#Creates a creature with the basic required components
class creature():
    #Initializes function with the given parameters
    def __init__(self, name, hp, ac, enemy, hostile, max_hp):
        self.name = name
        self.hp = hp
        self.ac = ac
        self.enemy = enemy
        self.hostile = hostile
        self.max_hp = max_hp

    #Return functions for safe access
    def get_name(self):
        return self.name
    def get_hp(self):
        return self.hp
    def get_ac(self):
        return self.ac
    def is_enemy(self):
        return self.enemy
    def is_hostile(self):
        return self.hostile
    def get_max_hp(self):
        return self.max_hp

    #Prints relevant info for a creature
    def get_all(self):
        return f"Name: {self.name :<20}Health: {self.hp :<10}Armor: {self.ac :<10}"

    #Adjusting creature aspects
    def damage(self, num):
        self.hp -= num
        return self.hp
    def heal(self, num):
        if self.hp + num <= self.max_hp:
            self.hp += num
        else:
            self.hp = self.max_hp
        return self.hp
    def change_ac(self, num):
        old_ac = self.ac
        self.ac = num
        return old_ac
    def become_hostile(self):
        self.hostile = True
        return True
    def remove_hostile(self):
        self.hostile = False
        return False
    def become_enemy(self):
        self.enemy = True
        return True
    def become_friendly(self):
        self.enemy = False
        return False

    
