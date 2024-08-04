#~~~~~~~Math~~~~~~#
def Add(x, y):
    if not (isinstance((x or y), int)) or (isinstance((x or y), float)):
        print("error: not a number")
        exit()
    return x + y


def Sub(x, y):
    if not (isinstance((x or y), int)) or (isinstance((x or y), float)):
        print("error: not a number")
        exit()
    return x - y


def Mul(x, y):
    if not (isinstance((x or y), int)) or (isinstance((x or y), float)):
        print("error: not a number")
        exit()
    return x * y


def Div(x, y):
    if not (isinstance((x or y), int)) or (isinstance((x or y), float)):
        print("error: not a number")
        exit()
    if y == 0:
        print("error cant divide by 0")
        exit()
    return x / y


def Power(x, y):
    if not (isinstance((x or y), int)) or (isinstance((x or y), float)):
        print("error: not a number")
        exit()
    return x ** y


def Square(x):
    if not (isinstance(x, int)) or (isinstance(x, float)):
        print("error: not a number")
        exit()
    return x ** 0.5


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


def Max(x, y):
    if not (isinstance((x or y), int)) or (isinstance((x or y), float)):
        print("error: not a number")
        exit()
    if x > y:
        return x
    return y


def Assign(x, y):
    x = y
    return x


def Equal(x, y):
    return x == y


def Not_equal(x, y):
    return x != y


def Greater(x, y):
    if not (isinstance((x or y), int)) or (isinstance((x or y), float)):
        print("error: not a number")
        exit()
    return x > y


def Smaller(x, y):
    if not (isinstance((x or y), int)) or (isinstance((x or y), float)):
        print("error: not a number")
        exit()
    return x < y


# or func
def Or(x, y):
    return x or y


# and func
def And(x, y):
    return x and y
