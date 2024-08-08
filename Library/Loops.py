#~~~~~~Loops~~~~~#
#Loop functions contains functions that can be used to perform loops
#While loop function
def While(condition_func, action_func):
    if condition_func():
        action_func()
        While(condition_func, action_func)

#For loop function with range and action functions
def ForInRange(start, stop, step, body):
    for i in range(start, stop, step):
        body(i)


#For loop function with step and action functions
def For(start, end, step_func, action_func):
    if start < end:
        action_func(start)
        next_step = step_func(start)
        For(next_step, end, step_func, action_func)