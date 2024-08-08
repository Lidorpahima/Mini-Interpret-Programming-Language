from Library import Arrays
from Library import Loops
from Library import Math
from Library import String
from Library import Tuples
from Library import Conditions
from Library import Lexer


# ~~~~~Main~~~~~~#
def main():
    # Array functions test
    print("\n########################################")
    print("Array functions:")
    arr = Arrays.New_Array(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) # Create new array
    strArr = Arrays.New_Array("Ron", "Lidor", "Ron", "Avraham") # Create new array
    str2Arr = Arrays.New_Array("abcdefg") # Create new array
    print(arr) # Print arr
    print(strArr) # Print strArr
    print(str2Arr)  # Print str2Arr
    print(f"arr len ={Arrays.Length(arr)}") # Print arr length
    print(f"strArr len ={Arrays.Length(strArr)}") # Print strArr length
    print(f"str2Arr len ={Arrays.Length(str2Arr)}") # Print str2Arr length
    print(f"value 1 in Index arr = {Arrays.GetIndex(arr, 1)}") # Get value in index 1
    print(f"value 3 in Index  = {Arrays.GetIndex(arr, 3)}") # Get value in index 3
    print(f"value 10 in Index  = {Arrays.GetIndex(arr, 10)}") # Get value in index 10
    Arrays.Append(arr, 11) # Append 11 to arr
    print(f" append arr 11 => {arr}") # Print arr after append
    print(f" arr value Array i=2 => {Arrays.GetValue(arr, 2)}") # Get value in index 2
    Arrays.add(arr, 11, 22) # Add 22 in index 11
    print(f" add arr 22 in new index (11) => {arr}") # Print arr after add
    print(f" add arr 24 in index 0 => {Arrays.add(arr, 0, 24)}") # Add 24 in index 0
    print(f" remove arr -1 in index 11 => {Arrays.Remove(arr, -1)}") # Remove value in index 11

    # String functions test
    print("\n########################################")
    print("Strings functions:")
    print(String.Replace("asd", "s", "d")) # Replace s with d in asd
    print(String.Is_upper("this needs to print in upper case")) #This function will print the String in upper case
    print(String.Is_lower("this needs to print in lower case")) #This function will print the String in lower case
    print(String.Concat("C", "o", "c", "a", "t")) # Concatenate the letters to form the word "Concat"
    print(String.Split("Alona koztey the Queen")) # Split the string to words
    print(String.Reverse("neeuQ eht yetzok anolA")) # Reverse the string

    # Conditions test
    print("\n########################################")
    print("Conditions:")
    Conditions.If(True, lambda: print("Condition is True")) # If condition is True print "Condition is True"
    Conditions.If(False, lambda: print("This should not be printed !")) # If condition is False print "This should not be printed !"
    Conditions.If(False, Conditions.Else(lambda: print("Condition is False"))) # If condition is False print "Condition is False"

    # Loops test
    print("\n########################################")
    print("Loops:")

    i = 1
    n = 5

    def condition():
        nonlocal i, n
        return i <= n # Return True if i is less than or equal to n

    def action():
        nonlocal i # nonlocal is used to declare that the variable is not local.
        print(i)
        i += 1

    print("\nWhile:")
    Loops.While(condition, action) # While i is less than or equal to n, print i and increment i by 1
    print("\nForInRange:")
    Loops.ForInRange(0, 5, 1, print) # For i in range 0 to 5, print i
    print("\nFor:")
    Loops.For(1, 513, lambda x: 2 * x, print) # For i in range 1 to 513, multiply i by 2 and print i

    # Tuples test
    print("\n########################################")
    print("Tuples:\n")

    t1 = Tuples.Tuples(1, 2, 3, 4, 5) # Create new tuple
    print(f"t1: {t1}")
    t2 = Tuples.Tuples("a", "b", "c") # Create new tuple
    print(f"t2: {t2}")

    t3 = Tuples.Tuples(5, 2, 8, 1, 9) # Create new tuple
    print(f"Original t3: {t3}")
    sorted_t3 = Tuples.sort(t3) # Sort t3
    print(f"Sorted t3: {sorted_t3}")

    t4 = Tuples.AddTuple(t1, t2) # Add t1 and t2
    print(f"t1 + t2: {t4}")

    print("\nGetting index:")
    print(f"t1[2]: {Tuples.Getindex(t1, 2)}") # Get value in index 2

    print("\nFinding index of value:")
    print(f"Index of 3 in t1: {Tuples.Index(t1, 3)}") # Get index of value 3

    # Test Length function
    print("\nGetting length:")
    print(f"Length of t1: {Tuples.Length(t1)}") # Get length of t1

    # Math functions test
    print("\n########################################")
    print("Math:\n")
    print(f"Add(5, 3) = {Math.Add(5, 3)}") # Add 5 and 3
    print(f"Sub(10, 4) = {Math.Sub(10, 4)}") # Subtract 4 from 10
    print(f"Mul(6, 7) = {Math.Mul(6, 7)}") # Multiply 6 by 7
    print(f"Div(20, 4) = {Math.Div(20, 4)}") # Divide 20 by 4
    print(f"Power(2, 3) = {Math.Power(2, 3)}") # 2 to the power of 3
    print(f"Square(16) = {Math.Square(16)}") # Square root of 16
    print(f"Min(8, 3) = {Math.Min(8, 3)}") # Minimum of 8 and 3
    print(f"Max(8, 3) = {Math.Max(8, 3)}") # Maximum of 8 and 3
    print(f"Equal(5, 5) = {Math.Equal(5, 5)}")  # Check if 5 is equal to 5
    print(f"Not_equal(5, 6) = {Math.Not_equal(5, 6)}") # Check if 5 is not equal to 6
    print(f"Greater(7, 3) = {Math.Greater(7, 3)}") # Check if 7 is greater than 3
    print(f"Smaller(2, 8) = {Math.Smaller(2, 8)}") # Check if 2 is smaller than 8
    print(f"Or(True, False) = {Math.Or(True, False)}") # Check if True or False
    print(f"And(True, False) = {Math.And(True, False)}") # Check if True and False
    x = 5
    print(f"x before assignment: {x}")
    x = Math.Assign(x, 10) # Assign 10 to x
    print(f"x after Assign(x, 10): {x}")

    # Lexer test
    print("\n########################################")
    print("Lexer:\n")
    str = ''' 
def inc_s(s):
    s = Math.Add(s,1)
'''
    print(Lexer.buildTree(str)) # Build tree from str and print it


if __name__ == '__main__':
    main()
