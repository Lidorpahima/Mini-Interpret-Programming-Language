from Library import Arrays
from Library import Loops
from Library import Math
from Library import String
from Library import Tuples
from Library import Conditions
from Library import Lexer


# ~~~~~Main~~~~~~#
def main():
    code = '''
def func(name):
    print(f"Hello {name}")   
'''

    print(Lexer.buildTree(code))


if __name__ == '__main__':
    main()
