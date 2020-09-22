from pirate import Pirate
from ship import Ship

if __name__ == "__main__":
    
    prirate_1 = Pirate("Jack")
    prirate_1.drink_some_rum()
    
    prirate_2 = Pirate("David")

    prirate_1.brawl(prirate_2)

    print("ship1")
    ship_1 = Ship("Black Pearl")
    ship_1.fill_ship()
    ship_1.ship_info()
    print("ship2")
    ship_2 = Ship("Dutchman")
    ship_2.fill_ship()
    ship_2.ship_info()

    ship_1.battle(ship_2)