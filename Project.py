import array
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

#~~~~~Strings~~~~~#

def Replace(s): #replace func ****
    for c in s:
        if type(c)==int or type(c)==float:
            print("error: not a string")
            exit()
    return s[::-1]

def Is_upper(s):
    return s.upper()
def Is_Lower(s):
    return s.lower()



#~~~~~~Loops~~~~~#
#def kol_od(x,condition,y): # While
 #   while(x,condition,y):

#def For() #For



#~~~~~~Arrays~~~~~#
def New_Array():
    return []
def Length(Array_Name):
    if isinstance(Array_Name, list):
        return len(Array_Name)
    else:
        print("error: argument is not an array")
def Index(array, i):
    if isinstance(array, list):
        return array.index(i)
    else:
        print("error: argument is not an array")


def Append(array, element):
    if isinstance(array, list):
        array.append(element)
    else:
        print("error: first argument is not an array")
def Array(array,i):
    if isinstance(array, list):
        return array[i]
    else:
        print("error: first argument is not an array")
def Add(array,i,element):

    if isinstance(array, list):
        array.insert(i,element)
        return "Element added successfully"
    else:
        print("error: first argument is not an array")
def Remove(array,i):
    if isinstance(array, list):
       array.pop(i)
       return array

#~~~~~~Tuples~~~~~~#



    #~~~~~Main~~~~~~#
def main():
    new_array = New_Array()
    Append(new_array,5)
    Append(new_array, 52)
    Append(new_array, 2)
    Append(new_array, 4)
    Length(new_array)
    print(Add(new_array,1,8))
    print("CHECK")
    print(new_array)
    print(Remove(new_array,-1))

if __name__ == '__main__':
    main()