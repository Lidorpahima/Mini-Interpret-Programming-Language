# ~~~~Conditions~~~~~
# Conditions functions are used to test a condition and execute action based on the result
# If the condition is True, the action is executed
def If(condition, action):
    if condition:
        action()

# If the condition is False, the action is executed
def Else(action):
    action()
