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
    print(f"arr len ={Arrays.Length(arr)}")
    print(f"strArr len ={Arrays.Length(strArr)}")
    print(f"str2Arr len ={Arrays.Length(str2Arr)}")
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

    # Tuples
    print("\n########################################")
    print("Tuples:\n")

    t1 = Tuples.Tuples(1, 2, 3, 4, 5)
    print(f"t1: {t1}")
    t2 = Tuples.Tuples("a", "b", "c")
    print(f"t2: {t2}")

    t3 = Tuples.Tuples(5, 2, 8, 1, 9)
    print(f"Original t3: {t3}")
    sorted_t3 = Tuples.sort(t3)
    print(f"Sorted t3: {sorted_t3}")

    t4 = Tuples.AddTuple(t1, t2)
    print(f"t1 + t2: {t4}")

    print("\nGetting index:")
    print(f"t1[2]: {Tuples.Getindex(t1, 2)}")

    print("\nFinding index of value:")
    print(f"Index of 3 in t1: {Tuples.Index(t1, 3)}")

    # Test Length function
    print("\nGetting length:")
    print(f"Length of t1: {Tuples.Length(t1)}")

    # Math
    print("\n########################################")
    print("Math:\n")
    print(f"Add(5, 3) = {Math.Add(5, 3)}")
    print(f"Sub(10, 4) = {Math.Sub(10, 4)}")
    print(f"Mul(6, 7) = {Math.Mul(6, 7)}")
    print(f"Div(20, 4) = {Math.Div(20, 4)}")
    print(f"Power(2, 3) = {Math.Power(2, 3)}")
    print(f"Square(16) = {Math.Square(16)}")
    print(f"Min(8, 3) = {Math.Min(8, 3)}")
    print(f"Max(8, 3) = {Math.Max(8, 3)}")
    print(f"Equal(5, 5) = {Math.Equal(5, 5)}")
    print(f"Not_equal(5, 6) = {Math.Not_equal(5, 6)}")
    print(f"Greater(7, 3) = {Math.Greater(7, 3)}")
    print(f"Smaller(2, 8) = {Math.Smaller(2, 8)}")
    print(f"Or(True, False) = {Math.Or(True, False)}")
    print(f"And(True, False) = {Math.And(True, False)}")
    x = 5
    print(f"x before assignment: {x}")
    x = Math.Assign(x, 10)
    print(f"x after Assign(x, 10): {x}")

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
