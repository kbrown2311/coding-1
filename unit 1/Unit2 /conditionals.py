# conditional logic- these are keywords that instruct your program to 

from ast import If
from operator import call


grade=int(input("Enter your grade: ")) 

if grade >= 90:
    print("Congrats!")
else:
    print("try again!")

def college():
    grade=int(input("please type in your grade: "))
    if grade < 90:
     templeUApp()
else:
     ccpApp()

def ccpApp():
    print("congrats! please complete the CCP with the following code")
    print("351256")
    ccpApp()

def templeUApp():
    print("congrats! please complete the CCP with the following code")
     print("abcdef")
    TempleUApp()

print(" press 1 for addition, 2 for subtraction")


def calculate_add():
    print("program started: Please type in some numbers: ")
    num1 = int(input())
    num2 = int(input())
    print(num1 + num2)
    print(" program ended")
    calculate_add():

#1  
def calculate_subtract():
    print("program started: Please type in some numbers: ")
    num1 = int(input())
    num2 = int(input())
    print(num1 - num2)
    print(" program ended")
calculate_subtract()


def calculatorMain():
    print('1 = addition,)
    print('2 = subtraction,)
    print('3 = multiplication')
    print('4 = division')



        
    If userSelects == 1, 
        calculate_add()
    elif userSelects == 2, 
        calculate_subtract()
    elif userSelects == 3,
        calculate_multiply()
    elif userSelects == 4,
        calculate_divide()
 
def movieTicket():
    age = int(input("Please enter your age: "))

if they are younger than 7 its 8.00
print("your ticket is $8.00")
if they are between 7 to 20 its 12.00
print("your ticket is $12.00")
if they are between 21 to 60 its 20.00
print("your ticket is $20.00")  
if they are older than 60 and above its free/0.00
print("your ticket is free!")