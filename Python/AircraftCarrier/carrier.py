from aircraft import Aircraft

class Carrier():
    def __init__(self, name, ammo, health):
        self.name = name
        self.ammo = ammo
        self.health = health
        self.aircrafts = []

    def add_aircraft(self, aircraft):
        self.aircrafts.append(aircraft)
        print(f"An {aircraft.type} has been loaded to {self.name}.")

    def fill(self):
        if self.calculate_needed_ammo() > self.ammo:
            sorted_aircrafts = Carrier.sort_aircrafts(self.aircrafts)
            i = 0
            while self.ammo > 0:
                self.ammo = sorted_aircrafts[i].refill(self.ammo)
                i += 1
        else:
            for aircraft in self.aircrafts:
                self.ammo = aircraft.refill(self.ammo)

    def get_status(self):
        print(f"Name: {self.name}, Ammo: {self.ammo}, Health: {self.health}")
        for aircraft in self.aircrafts:
            print(aircraft.get_status())

    def calculate_needed_ammo(self):
        needed_ammo = 0
        for aircraft in self.aircrafts:
            needed_ammo += aircraft.max_ammo - aircraft.current_ammo
        return(needed_ammo)

    @staticmethod
    def sort_aircrafts(aircrafts):
        sorted_aircrafts = sorted(aircrafts, key=lambda x: x.priority, reverse=True)
        return(sorted_aircrafts)
