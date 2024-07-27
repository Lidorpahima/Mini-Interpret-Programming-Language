
#~~~~~~~Math~~~~~~#
def test():
    print("test")

def add(x,y):
    return x+y
def sub(x,y):
        return x-y
def mul(x,y):
    return x*y

def div(x,y):
    if(y==0): print("error cant divide by 0")
    return x/y

def power(x,y):
    return x**y

def square(x):
    return x**(0.5)
def min(x,y):
    if(x < y):
        return x
    return y
def max(x,y):
    if(x > y):
        return x
    return y
def Assign(x,y):
    x = y
    return x
def equal(x,y):
    return x==y
def not_equal(x,y):
    return x != y
def greater(x,y):
    return x > y
def smaller(x,y):
    return x < y
def oho (x,y): #or func
    return x or y
def vegam(x,y):  #and func
    return x and y

#~~~~~Strings~~~~~#

def reverse_string(s): #replace func ****

    for c in s:
        if oho(equal(type(c),int),equal(type(c),float)):
            print("error: not a string")
    return s[::-1]

#def Upper_case(s):



#~~~~~~Loops~~~~~#
#def kol_od(x,condition,y): # While
 #   while(x,condition,y):

#def For() #For



#~~~~~~Arrays~~~~~#
def Array():
    return


def Length():
    retrun list.
#~~~~~Main~~~~~~#
def main():
    x=123
    print(reverse_string(x))

if __name__ == '__main__':
    main()