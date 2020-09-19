class Pirate:
    
    intoxication_level = 0

    def drink_some_rum(self):
        self.intoxication_level += 1
        print(f"The pirate drank some rum! His intoxication level is {self.intoxication_level}.")

    def hows_it_going_mate(self):
        if self.intoxication_level <= 4:
            print("Pour me anudder!")
        else:
            print("Arghh, I'ma Pirate. How d'ya d'ink its goin?")
            self.intoxication_level = 0