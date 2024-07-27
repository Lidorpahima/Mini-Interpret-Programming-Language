from Library import Arrays
from Library import Loops
from Library import Math
from Library import String
from Library import Tuples
from Library import Conditions

    #~~~~~Main~~~~~~#
def main():
    x = 5
    Conditions.If(x == 5, lambda: print("x is 5"))
    Conditions.Else(lambda: print("x is not 5"))

if __name__ == '__main__':
    main()