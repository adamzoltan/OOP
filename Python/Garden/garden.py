from plants import Plant

class Garden():
    def __init__(self):
        self.plants = []

    def add(self, plant):
        self.plants.append(plant)

    def garden_status(self):
        for plant in self.plants:
            plant.status()

    def count_dry_plants(plants):
        counter = 0
        for plant in plants:
            if plant.needs_water():
                counter += 1
        return counter

    def water_plants(self, water_amount):
        print(f"Watering with {water_amount}")
        dry_plants = Garden.count_dry_plants(self.plants)
        for plant in self.plants:
            if plant.needs_water():
                plant.water_level = (water_amount / dry_plants) * plant.absorbtion

