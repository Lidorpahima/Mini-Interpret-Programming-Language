# ~~~~~Tuples~~~~~#
#Tuple functions that can be used to manipulate tuples
#Create a tuple with the given arguments
def Tuples(*args):
    return tuple(args)

#Sort the tuple and return it
def sort(tupple):
    return tuple(sorted(tupple))

#Add two tuples and return the result
def AddTuple(tuple1, tuple2):
    return tuple1 + tuple2

#Get the value at the given index
def Getindex(tupple, i):
    return tupple[i]

#Get the index of the given value
def Index(tupple, i):
    return tupple.index(i)

#Get the length of the tuple
def Length(tupple):
    return len(tupple)
