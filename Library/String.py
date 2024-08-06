# ~~~~~Strings~~~~~#

# replace func
def Replace(s):
    for c in s:
        if not (isinstance(c, int)) or (isinstance(c, float)):
            print("error: not a string")
            exit()
    return s[::-1]


def Is_upper(s):
    if isinstance(s, str):
        return s.upper()
    elif isinstance(s, list):
        return [item.upper() if isinstance(item, str) else item for item in s]


def Is_lower(s):
    if isinstance(s, str):
        return s.lower()
    elif isinstance(s, list):
        return [item.lower() if isinstance(item, str) else item for item in s]


def Concat(*args):
    return ''.join(str(arg) for arg in args)


def Split(s, val=None):
    if not isinstance(s, str):
        print("Not a string")
        exit()
    return s.split(val)
