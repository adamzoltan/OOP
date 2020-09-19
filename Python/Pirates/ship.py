from pirate import Pirate
import random

class Ship:
    captain = None
    crew = []

    def fill_ship(self):
        self.captain = Pirate("Captain Joe")
        crew_number = r = random.randint(1,25)
        for i in range(crew_number):
            self.crew.append(Pirate(f"Pirate-{i}"))
        print(f"{self.captain.name} recruited {r} bastards into his crew.")