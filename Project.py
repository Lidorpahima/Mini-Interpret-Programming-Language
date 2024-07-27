from Library.Arrays import *
from Library.Loops import *
from Library.Math import *
from Library.String import *
    #~~~~~Main~~~~~~#
def main():
    new_array = New_Array()
    Append(new_array,5)
    Append(new_array, 52)
    Append(new_array, 2)
    Append(new_array, 4)
    Length(new_array)
    print(add(new_array,1,8))
    print("CHECK")
    print(new_array)
    print(Remove(new_array,-1))

if __name__ == '__main__':
    main()