#~~~~~~Loops~~~~~#

# TODO: LETAKEN
def While(condition, body):
    while condition:
        body()

# TODO: LETAKEN
def For(arr, body):
    if len(arr) == 0:
        raise ("error: empty array")
    for item in arr:
        body(item)
        if(item == arr[-1]):
            print(arr)
            break
    


def ForInRange(start, stop, step, body):
    for i in range(start, stop, step):
        body(i)


