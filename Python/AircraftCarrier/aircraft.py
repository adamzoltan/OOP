class Aircraft():
    def __init__(self):
        self.type
        self.max_ammo
        self.base_damage
        self.current_ammo
    
    def fight(self):
        dealt_damage = self.current_ammo * self.base_damage
        self.current_ammo = 0
        return(dealt_damage)
