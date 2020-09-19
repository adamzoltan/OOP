import random

class Pirate:
    
    is_alive = True
    is_conscious = True
    intoxication_level = 0

    def __init__(self, name):
        self.name = name

    def drink_some_rum(self):
        if self.is_alive:
            self.intoxication_level += 1
            print(f"The pirate drank some rum! His intoxication level is {self.intoxication_level}.")
        else:
            print("He is dead...")

    def hows_it_going_mate(self):
        if self.is_alive:
            if self.intoxication_level <= 4:
                print("Pour me anudder!")
            else:
                print("Arghh, I'ma Pirate. How d'ya d'ink its goin?")
                self.intoxication_level = 0
        else:
            print("He is dead...")

    def die(self):
        self.is_alive = False
        print(f"{self.name} died!")

    def pass_out(self):
        self.is_conscious = False
        print(f"{self.name} passed out!")

    def brawl(self, pirate):
        if self.is_alive and pirate.is_alive:
            r = random.randint(1,3)
            if r == 1:
                self.die()
            elif r == 2:
                pirate.die()
            else:
                self.pass_out()
                pirate.pass_out()
        else:
            echo("One of the pirates is already dead, they can't fight...")