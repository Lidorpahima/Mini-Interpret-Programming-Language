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
def add(array,i,element):

    if isinstance(array, list):
        array.insert(i,element)
        return "Element added successfully"
    else:
        print("error: first argument is not an array")
def Remove(array,i):
    if isinstance(array, list):
       array.pop(i)
       return array