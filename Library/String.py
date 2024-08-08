# ~~~~~Strings~~~~~#
#String functions contains functions that can be used to manipulate strings
# replace the old value with the new value in the given string
def Replace(s, old, new):
    if not isinstance(s, str):
        print("Input must be a string")
    return s.replace(old, new)

#Convert the string to upper case
def Is_upper(s):
    if isinstance(s, str):
        return s.upper()
    elif isinstance(s, list):
        return [item.upper() if isinstance(item, str) else item for item in s]
    else:
        return "Not a string can't convert to upper!"

#Convert the string to lower case
def Is_lower(s):
    if isinstance(s, str):
        return s.lower()
    elif isinstance(s, list):
        return [item.lower() if isinstance(item, str) else item for item in s]
    else:
        return "Not a string can't convert to lower!"

#Concatenate the given strings
def Concat(*args):
    return ''.join(str(arg) for arg in args)

#Split the string with the given value
def Split(s, val=None):
    if not isinstance(s, str):
        print("Not a string")
        exit()
    return s.split(val)

#Reverse the string
def Reverse(s):
    for c in s:
        if not isinstance(s, str):
            print("Not a string")
            exit()
        return s[::-1]
