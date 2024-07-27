#~~~~~~~Math~~~~~~#
def Add(x,y):
    if (type(x or y) != int) or (type(x or y) != float):
        print("error: not a number")
        exit()
    return x+y
def Sub(x,y):
    if (type(x or y) != int) or (type(x or y) != float):
        print("error: not a number")
        exit()
    return x-y
def Mul(x,y):
    if (type(x or y) != int) or (type(x or y) != float):
        print("error: not a number")
        exit()
    return x*y

def Div(x,y):
    if (type(x or y) != int) or (type(x or y) != float):
        print("error: not a number")
        exit()
    if(y==0): print("error cant divide by 0")
    return x/y

def Power(x,y):
    if (type(x or y) != int) or (type(x or y) != float):
        print("error: not a number")
        exit()
    return x**y

def Square(x):
    if (type(x or y) != int) or (type(x or y) != float):
        print("error: not a number")
        exit()
    return x**(0.5)
def Min(x,y):
    if (type(x or y) != int) or (type(x or y) != float):
        print("error: not a number")
        exit()
    if(x < y):
        if (type(x or y) != int) or (type(x or y) != float):
            print("error: not a number")
            exit()
        return x
    return y
def Max(x,y):
    if (type(x or y) != int) or (type(x or y) != float):
        print("error: not a number")
        exit()
    if(x > y):
        return x
    return y
def Assign(x,y):
    x = y
    return x
def Equal(x,y):
    return x==y
def Not_equal(x,y):
    return x != y
def Greater(x,y):
    if (type(x or y) != int) or (type(x or y) != float):
        print("error: not a number")
        exit()
    return x > y
def Smaller(x,y):
    if (type(x or y) != int) or (type(x or y) != float):
        print("error: not a number")
        exit()
    return x < y
def Or (x,y): #or func
    return x or y
def And(x,y):  #and func
    return x and y
