#~~~~~Strings~~~~~#

def Replace(s):  #replace func ****
    for c in s:
        if type(c) == int or type(c) == float:
            print("error: not a string")
            exit()
    return s[::-1]


def Is_upper(s):
    return s.upper()


def Is_Lower(s):
    return s.lower()
