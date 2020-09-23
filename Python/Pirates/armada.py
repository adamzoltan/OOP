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
            ship.fill_ship()
            self.ships.append(ship)
            counter += 1
        print(f"The {self.name} is created with {counter} ships.")

    def war(self, enemy_armada):
        armada_size = len(self.ships)
        enemy_armada_size = len(enemy_armada.ships)
        armada_counter = 0
        enemy_armada_counter = 0
        while armada_counter + 1 < armada_size and enemy_armada_counter + 1 < enemy_armada_size:
            print(armada_size)
            print(armada_counter)
            print(enemy_armada_size)
            print(enemy_armada_counter)
            if self.ships[armada_counter].battle(enemy_armada.ships[enemy_armada_counter]):
                enemy_armada_counter += 1
            else:
                armada_counter += 1
        if enemy_armada_counter + 1 == enemy_armada_size:
            print(f"The {self.name} is victorious!")
        else:
            print(f"The {enemy_armada.name} is victorious!")

