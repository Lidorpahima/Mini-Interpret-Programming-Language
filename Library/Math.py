# ~~~~~~~Math~~~~~~#
#Math functions will contain functions that can be used to perform mathematical operations
#Add two numbers
def Add(x, y):
    if not (isinstance((x or y), int)) or (isinstance((x or y), float)):
        print("error: not a number")
        exit()
    return x + y

#Subtract two numbers
def Sub(x, y):
    if not (isinstance((x or y), int)) or (isinstance((x or y), float)):
        print("error: not a number")
        exit()
    return x - y

#Multiply two numbers
def Mul(x, y):
    if not (isinstance((x or y), int)) or (isinstance((x or y), float)):
        print("error: not a number")
        exit()
    return x * y

#Divide two numbers
def Div(x, y):
    if not (isinstance((x or y), int)) or (isinstance((x or y), float)):
        print("error: not a number")
        exit()
    if y == 0:
        print("error cant divide by 0")
        exit()
    return x / y

#Raise x to the power of y
def Power(x, y):
    if not (isinstance((x or y), int)) or (isinstance((x or y), float)):
        print("error: not a number")
        exit()
    return x ** y

#Get the square root of x
def Square(x):
    if not (isinstance(x, int)) or (isinstance(x, float)):
        print("error: not a number")
        exit()
    return x ** 0.5

#Get the minimum of two numbers
def Min(x, y):
    if not (isinstance((x or y), int)) or (isinstance((x or y), float)):
        print("error: not a number")
        exit()
    if x < y:
        if not (isinstance((x or y), int)) or (isinstance((x or y), float)):
            print("error: not a number")
            exit()
        return x
    return y

#Get the maximum of two numbers
def Max(x, y):
    if not (isinstance((x or y), int)) or (isinstance((x or y), float)):
        print("error: not a number")
        exit()
    if x > y:
        return x
    return y

#Assign y to x
def Assign(x, y):
    x = y
    return x

#Compare two numbers
def Equal(x, y):
    return x == y

#Check if two numbers are not equal
def Not_equal(x, y):
    return x != y

#Check if x is greater than y
def Greater(x, y):
    if not (isinstance((x or y), int)) or (isinstance((x or y), float)):
        print("error: not a number")
        exit()
    return x > y

#Check if x is smaller than y
def Smaller(x, y):
    if not (isinstance((x or y), int)) or (isinstance((x or y), float)):
        print("error: not a number")
        exit()
    return x < y


# or func check if x or y is true
def Or(x, y):
    return x or y


# and func check if x and y is true
def And(x, y):
    return x and y
