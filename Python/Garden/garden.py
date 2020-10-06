from plants import Plant

class Garden():
    def __init__(self):
        self.plants = []

    def add(self, plant):
        self.plants.append(plant)


    def garden_status(self):
        for plant in self.plants:
            plant.status()