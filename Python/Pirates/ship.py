from pirate import Pirate
import random

class Ship:

    def __init__(self, name):
        self.name = name
        self.captain = None
        self.crew = []

    def fill_ship(self):
        self.captain = Pirate("Captain Joe")
        crew_number = random.randint(1,25)
        for i in range(crew_number):
            self.crew.append(Pirate(f"Pirate-{i}"))
        print(f"{self.captain.name} recruited {crew_number} bastards into his crew.")

    def ship_info(self):
        alive_pirates = 0
        captain_status = ""
        if self.captain.intoxication_level > 0:
           captain_status += "The captain drank some rum."
        if not self.captain.is_alive:
            captain_status += "The captain is dead."
        if not self.captain.is_conscious:
            captain_status += "The captain has passed out."
        for pirate in self.crew:
            if pirate.is_alive:
                alive_pirates += 1
        print(captain_status)
        print(f"There are {alive_pirates} alive pirates on the ship.")
    
    def battle(self, enemy_ship):
        self_score = Ship.calculate_score(self)
        enemy_score = Ship.calculate_score(enemy_ship)
        if self_score > enemy_score:
            print(f"{self.name} won the battle!")
            enemy_ship.kill_crew()
        else:
            print(f"{enemy_ship.name} won the battle!")
            self.kill_crew()
        return(self_score > enemy_score)

    @staticmethod
    def calculate_score(ship):
        alive_pirates = 0
        for pirate in ship.crew:
            if pirate.is_alive:
                alive_pirates += 1
        return(alive_pirates-ship.captain.intoxication_level)

    def kill_crew(self):
        counter = 0
        for pirate in self.crew:
            r = random.randint(1,2)
            if r % 2 == 0:
                pirate.die()
                counter += 1
        print(f"{self.name} lost {counter} members of its crew.")


