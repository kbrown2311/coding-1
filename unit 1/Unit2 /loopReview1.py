def vendingMachine():
    print("vendingMachine")
    print("Please type in a value for the item you want")
    userSelection = input()
    while userSelection != 'q':
        if userSelection == 'b3':
            print("Nacho chips")
            print("Please type in a value for the item you want")
            userSelection = input()
    print("vending Machine is off")