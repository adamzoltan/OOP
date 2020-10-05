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

    def get_status(self):
        for aircraft in self.aircrafts:
            print(aircraft.get_status())
