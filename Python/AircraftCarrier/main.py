from f16 import F16

if __name__ == "__main__":

    f16 = F16()
    print(f16.current_ammo)
    print(f16.get_type())
    f16.refill(10)
    print(f16.get_status())
    print(f16.fight())
    print(f16.get_status())
