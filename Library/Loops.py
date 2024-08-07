#~~~~~~Loops~~~~~#

def While(condition_func, action_func):
    if condition_func():
        action_func()
        While(condition_func, action_func)


def ForInRange(start, stop, step, body):
    for i in range(start, stop, step):
        body(i)



def For(start, end, step_func, action_func):
    if start < end:
        action_func(start)
        next_step = step_func(start)
        For(next_step, end, step_func, action_func)