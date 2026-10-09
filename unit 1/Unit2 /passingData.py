# when we are building complex programs, we need to pass in data that is NOT always from the user.

# functionParameter = "This is placeholder data for the function variable inside the curly brackets."

def check_water_depth(depth):
    print(depth > 10)

    # function argument- this is the real data that we pass into the function call.
check_water_depth(7)

# retrun - allows us to pass data from INSIDE 1 function into another function

def username():
    print("What is your name?")
    name = input()
    return name

def confirmLogin():
name = username("BROWN")
    print("this is the user:" + name)

comfirmLogin()