# ~~~~~Strings~~~~~#

# replace func
def Replace(s, old, new):
    if not isinstance(s, str):
        print("Input must be a string")
    return s.replace(old, new)


def Is_upper(s):
    if isinstance(s, str):
        return s.upper()
    elif isinstance(s, list):
        return [item.upper() if isinstance(item, str) else item for item in s]
    else:
        return "Not a string can't convert to upper!"


def Is_lower(s):
    if isinstance(s, str):
        return s.lower()
    elif isinstance(s, list):
        return [item.lower() if isinstance(item, str) else item for item in s]
    else:
        return "Not a string can't convert to lower!"


def Concat(*args):
    return ''.join(str(arg) for arg in args)


def Split(s, val=None):
    if not isinstance(s, str):
        print("Not a string")
        exit()
    return s.split(val)


def Reverse(s):
    for c in s:
        if not isinstance(s, str):
            print("Not a string")
            exit()
        return s[::-1]
