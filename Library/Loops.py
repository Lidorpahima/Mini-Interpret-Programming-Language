#~~~~~~Loops~~~~~#

# TODO: LETAKEN
def While(condition, body):
    while condition:
        body()

# TODO: LETAKEN
def For(arr, body):
    if len(arr) == 0:
        raise ValueError("error: empty array")
    new_arr = [body(item) for item in arr]
    return new_arr
    


def ForInRange(start, stop, step, body):
    for i in range(start, stop, step):
        body(i)


