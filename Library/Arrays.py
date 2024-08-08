#~~~~~~Arrays~~~~~#
#Array functions that can be used to manipulate arrays
#Create a new array with the given arguments
def New_Array(*argv):
    return list(argv)

#Get the length of the array
def Length(Array_Name):
    if isinstance(Array_Name, list):
        return len(Array_Name)
    else:
        print("error: argument is not an array")

#Get the index of the given value
def GetIndex(array, i):
    if isinstance(array, list):
        return array.index(i)
    else:
        print("error: argument is not an array")

#Append the given element to the array
def Append(array, element):
    if isinstance(array, list):
        array.append(element)
    else:
        print("error: first argument is not an array")

#Get the value at the given index
def GetValue(array, i):
    if isinstance(array, list):
        return array[i]
    else:
        print("error: first argument is not an array")

#Add the given element to the given index
def add(array, i, element):
    if isinstance(array, list):
        array.insert(i, element)
        return "Element added successfully"
    else:
        print("error: first argument is not an array")

#Remove the element at the given index
def Remove(array, i):
    if isinstance(array, list):
        array.pop(i)
        return array
