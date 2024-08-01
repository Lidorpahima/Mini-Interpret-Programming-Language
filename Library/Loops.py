#~~~~~~Loops~~~~~#

# TODO: LETAKEN
def While(condition, body):
    while condition:
        body()

# TODO: LETAKEN
def For(arr, body):
    for item in arr:
        body(item)


def ForInRange(start, stop, step, body):
    for i in range(start, stop, step):
        body(i)


