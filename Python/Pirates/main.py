from pirate import Pirate
from ship import Ship

if __name__ == "__main__":
    
    prirate_1 = Pirate("Jack")
    prirate_1.drink_some_rum()
    prirate_1.hows_it_going_mate()
    
    prirate_2 = Pirate("David")

    prirate_1.brawl(prirate_2)

    ship = Ship()
    ship.fill_ship()