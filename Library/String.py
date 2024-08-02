#~~~~~Strings~~~~~#

def Replace(s):  #replace func ****
    for c in s:
        if type(c) == int or type(c) == float:
            print("error: not a string")
            exit()
    return s[::-1]


def Is_upper(s):
    if isinstance(s, str):
        return s.upper()
    elif isinstance(s, list):
        print("Enter list")
        return [item.upper() if isinstance(item, str) else item for item in s]
