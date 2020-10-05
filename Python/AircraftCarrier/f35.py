from aircraft import Aircraft

class F35(Aircraft):
    def __init__(self):
        self.type = 'F35'
        self.max_ammo = 12
        self.base_damage = 50
        self.current_ammo = 0
        self.is_priority = True