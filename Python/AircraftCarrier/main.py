from f16 import F16
from f35 import F35
from carrier import Carrier

if __name__ == "__main__":

    f16 = F16()
    f35 = F35()
    print(f16.current_ammo)
    print(f16.get_type())
    f16.refill(10)
    print(f16.get_status())
    print(f16.fight())
    print(f16.get_status())
    print(f16.is_priority())

    my_carrier = Carrier("carrier", 15, 10000)
    my_carrier.add_aircraft(f16)
    my_carrier.add_aircraft(f35)
    # my_carrier.get_status()

    my_carrier.fill()
    my_carrier.get_status()
