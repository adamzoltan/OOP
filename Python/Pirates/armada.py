from pirate import Pirate
from ship import Ship
import random

class Armada():
    def __init__(self, name):
        self.name = name
        self.ships = []

    def fill_armada(self):
        armada_size = random.randint(10,30)
        counter = 0
        for i in range(armada_size):
            ship = Ship(f"ship-{i}")
            self.ships.append(ship)
            counter += 1
        print(f"The {self.name} is created with {counter} ships.")
