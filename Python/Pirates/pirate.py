class Pirate:
    
    is_alive = True
    intoxication_level = 0

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