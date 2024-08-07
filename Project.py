from Library import Arrays
from Library import Loops
from Library import Math
from Library import String
from Library import Tuples
from Library import Conditions
from Library import Lexer


# ~~~~~Main~~~~~~#
def main():
    # Arrays
    print("\n########################################")
    print("Array functions:")
    arr = Arrays.New_Array(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    strArr = Arrays.New_Array("Ron", "Lidor", "Ron", "Avraham")
    str2Arr = Arrays.New_Array("abcdefg")
    print(arr)
    print(strArr)
    print(str2Arr)
    print(f"arr len ={Arrays.Length(arr)}")  #עד פה עובד
    print(f"strArr len ={Arrays.Length(strArr)}")
    print(f"str2Arr len ={Arrays.Length(str2Arr)}")  #עד פה עובד
    print(f"value 1 in Index arr = {Arrays.GetIndex(arr, 1)}")
    print(f"value 3 in Index  = {Arrays.GetIndex(arr, 3)}")
    print(f"value 10 in Index  = {Arrays.GetIndex(arr, 10)}")
    Arrays.Append(arr, 11)
    print(f" append arr 11 => {arr}")
    print(f" arr value Array i=2 => {Arrays.GetValue(arr, 2)}")
    Arrays.add(arr, 11, 22)
    print(f" add arr 22 in new index (11) => {arr}")
    print(f" add arr 24 in index 0 => {Arrays.add(arr, 0, 24)}")
    print(f" remove arr -1 in index 11 => {Arrays.Remove(arr, -1)}")

    # String
    print("\n########################################")
    print("Strings functions:")
    print(String.Replace("asd", "s", "d"))
    print(String.Is_upper("this needs to print in upper case"))
    print(String.Is_lower("this needs to print in lower case"))
    print(String.Concat("C", "o", "c", "a", "t"))
    print(String.Split("Alona koztey the Queen"))
    print(String.Reverse("neeuQ eht yetzok anolA"))

    # Conditions
    print("\n########################################")
    print("Conditions:")
    Conditions.If(True, lambda: print("Condition is True"))
    Conditions.If(False, lambda: print("This should not be printed !"))
    Conditions.If(False, Conditions.Else(lambda: print("Condition is False")))

    # Loops
    print("\n########################################")
    print("Loops:")

    i = 1
    n = 5
    def condition():
        nonlocal i, n
        return i <= n
    def action():
        nonlocal i
        print(i)
        i += 1

    print("\nWhile:")
    Loops.While(condition, action)
    print("\nForInRange:")
    Loops.ForInRange(0, 5, 1, print)
    print("\nFor:")
    Loops.For(1, 513, lambda x: 2 * x, print)

    # Lexer
    print("\n########################################")
    print("Lexer:\n")
    str = '''
def inc_s(s):
    s = Math.Add(s,1)
'''
    print(Lexer.buildTree(str))


if __name__ == '__main__':
    main()
