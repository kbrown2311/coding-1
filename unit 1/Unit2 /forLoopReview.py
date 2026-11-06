
 
mylist = [1,2,3,4,5]

#input("my list is done")
def rpsGame()
    print("welcome to rps")
    userMove = input()
    cpuMove = random. randint(1,3)
    turns = 0

    while turns < 3:
        if cpuMove == 1: