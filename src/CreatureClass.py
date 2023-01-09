import time

'''
THIS IS A PRIMARY FILE THAT HOLDS THE STRUCTURE FOR EVERY 
CREATURE IN THE GAME AND PROVIDES FUNCTIONS FOR MANIPULATING THEM
'''

#Creates a creature with the basic required components
class creature():
    #Initializes function with the given parameters
    def __init__(self, name, hp, max_hp, str_die, chr_die):
        self.name = name
        self.hp = hp
        self.max_hp = max_hp
        self.str_die = str_die
        self.chr_die = chr_die

    #Return functions for creature attributes
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

#Subclass of creature class for player-specific utilities
class player(creature):
    def __init__(self, name, hp, hp_max, str_die, chr_die, inventory, level=1, experience=0, experience_goal=100):
        self.inventory = inventory
        self.level = level
        self.experience = experience
        self.experience_goal = experience_goal
        creature.__init__(self, name, hp, hp_max, str_die, chr_die)
        
    #Return functions for player attributes
    def get_inventory(self):
        return self.inventory
    def get_level(self):
        return self.level
    def get_experience(self):
        return self.experience
    
    #Prints player inventory in readable format
    def print_inventory(self):
        print("Player inventory: ")
        for item, amount in self.inventory.items():
            print(f"{item}: {amount}")
      
    #adds amount of item to inventory      
    def add_item(self, item, amount):
        if item in self.inventory:
            self.inventory[item] = self.inventory[item] + amount    
        else:
            self.inventory.update({item:amount})
    
    #removes amount of item from inventory
    def remove_item(self, item, amount):
        self.inventory[item] -= amount
        if self.inventory[item] <= 0:
            self.inventory.pop(item)
     
    #Levels up the character and str/chr dice based on player input 
    def level_up(self):
        self.level += 1
        print("You've leveled up!")
        time.sleep(1)
        
        #Loop ensures proper input
        while True:
            try:
                
                upgrade_num = int(input(f"Current Strength dice is d{self.get_str_die()} and current Charisma dice is d{self.get_chr_die()}\nYou can either upgrade your Strength(1) or Charisma(2): "))
                if (upgrade_num == 1 or upgrade_num == 2):
                    break
                else:
                    print("Your input should be 1 or 2, let's try again")
                    time.sleep(1)
                    continue
            except ValueError or TypeError:
                    print("Your input should be 1 or 2, let's try again")
                    time.sleep(1)
                    continue
        
        #Updates dice and reports the change to the player
        if upgrade_num == 1:
            self.str_die += 2
            print(f"Strength upgraded, new dice: d{self.get_str_die()}")
            time.sleep(2)
        else:
            self.chr_die += 2
            print(f"Charisma upgraded, new dice: d{self.get_chr_die()}")
            time.sleep(2)
        
    #Returns true and calls level up if player has met experience goal, otherwise returns false
    def check_experience(self):
        if(self.experience >= self.experience_goal):
            self.level_up()
            self.experience_goal *= 2
            return True
        else:
            return False
        