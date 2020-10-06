class Aircraft():
    def __init__(self):
        self.type
        self.max_ammo
        self.base_damage
        self.current_ammo
        self.priority
    
    def fight(self):
        dealt_damage = self.current_ammo * self.base_damage
        self.current_ammo = 0
        return(dealt_damage)
    
    def refill(self, ammo):
        needed_ammo = self.max_ammo - self.current_ammo
        if ammo >= needed_ammo:
            self.current_ammo = self.current_ammo + needed_ammo
            print(f"An {self.type} has been filled with {needed_ammo} ammo.")
            return(ammo - needed_ammo)
        else:
            self.current_ammo = self.current_ammo + ammo
            print(f"An {self.type} has been filled with {ammo} ammo.")
            return(0)

    def get_type(self):
        return(self.type)

    def get_status(self):
        return(f"Type: {self.get_type()}, Ammo: {self.current_ammo}, Base Damage: {self.base_damage}, All Damage: {self.current_ammo * self.base_damage}")

    def is_priority(self):
        return(self.priority)

