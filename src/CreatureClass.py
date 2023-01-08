'''
THIS IS A PRIMARY FILE THAT HOLDS THE STRUCTURE FOR EVERY 
CREATURE IN THE GAME AND PROVIDES FUNCTIONS FOR MANIPULATING THEM
'''

#Creates a creature with the basic required components
class creature():
    #Initializes function with the given parameters
    def __init__(self, name, hp, str_die, chr_die):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.str_die = str_die
        self.chr_die = chr_die

    #Return functions for safe access
    def get_name(self):
        return self.name
    def get_hp(self):
        return self.hp
    def get_str_die(self):
        return self.str_die
    def get_chr_die(self):
        return self.chr_die
    def get_max_hp(self):
        return self.max_hp

    #Prints relevant info for a creature
    def get_all(self):
        return f"Name: {self.name :<20}Health: {self.hp :<10}Strength Dice: d{self.str_die :<10}Charisma Dice: d{self.chr_die :<10}"

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

    
