#~~~~Conditions~~~~~#
def If(condition, action):
    if condition:
        action()
def Else(action):
    action()