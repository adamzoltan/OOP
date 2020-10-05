from aircraft import Aircraft

class F16(Aircraft):
    def __init__(self):
        self.type = 'F16'
        self.max_ammo = 8
        self.base_damage = 30
        self.current_ammo = 0
        self.priority = False