
cent=int(input("Enter a number: "))
def conversion():
    dollar = cent /100
    Quater = cent /25
    dime = cent /10
    nickel = cent /5
    penny = cent /1
    print(f"dollar:{dollar:1.0f} ")
    print(f"quarters:{Quater:1.0f} ")
    print(f"dime:{dime:1.0f} ")
    print(f"nickel:{nickel:1.0f} ")
    print(f"penny:{penny:1.0f} ")

conversion()



