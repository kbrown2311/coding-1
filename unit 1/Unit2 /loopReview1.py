import random

def vendingMachine():
    print("vendingMachine")
    print("Please type in a value for the item you want")
    userSelection = input()
    while userSelection != 'q':
        if userSelection == 'b3':
            print("Nacho chips")
            print("Please type in a value for the item you want")
            userSelection = input()

        elif userSelection == "G4":
            print("BBQ chips") 
            print("Please type in a value for the item you want")
            userSelection
    print("VENDING MACHINE IS OFF")

    
#vendingMachine()

def diceGame():
    print("DICE GAME IS RUNNING")
    Print("please enter r to roll and q to quit")
    userSelection = input()

    while userSelection != 'q':
        if userSelection == "r":
            randomNumber = random.randint(1, 7)
            if randomNumber == 7:
                print(randomNumber)
                print("YOU WIN")
                print('+ 10 points')
                print("please enter r to roll and q to quit")
                userSelection = input()
             elif randomNumber == 7:

diceGame():                
