#Tracks key aspects of the current game state to influence gameflow
class game_state():
    def __init__(self, combat, base, biome, night):
        self.combat = combat
        self.base = base
        self.biome = biome
        self.night = night

    #Return functions for safe access
    def in_combat(self):
        return self.combat
    def in_base(self):
        return self.base
    def get_biome(self):
        return self.biome
    def is_night(self):
        return self.night

    #Functions for adjusting the game state
    def change_combat(self, bool):
        self.combat = bool
    def change_base(self, bool):
        self.base = bool
    def change_biome(self, new_biome):
        old_biome = self.biome
        self.biome = new_biome
        return old_biome
    def change_time(self, bool):
        self.is_night = bool