# loop a loop is a construct that repeats itself.
# in programming, a loop allows to repeat code instructions.

# there are two types of loops: for loop and while loop.

# while loop a type of loop that repeats a block of code as long as a specified condition is true.


# syntax
# if/ else and while are all functions.
#while 2+2 == 4:
    #print("The program is running...")
    #num=input("Enter a number: ")
# while looop will ALWAYS run unless you change the condition! 
# to false or use a break statement to exit the loop.
def gussing_game():
attempts = 3
correctNumber= 7
guess = int(input("guess a numbere"))

    while guess != correctNumber:
    print ("sorry thats wrong try again")
    attempts-=1
    print (attempts)
    guess = int(input())
    if attempts == 0 
    print ("GAME OVER- RAN OUT OF ATTEMPTS")
guessinggame():

    