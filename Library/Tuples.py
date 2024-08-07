# ~~~~~Tuples~~~~~#
def Tuples(*args):
    return tuple(args)


def sort(tupple):
    return tuple(sorted(tupple))


def addTuple(tuple1, tuple2):
    return tuple(list(tuple1) + tuple2)


def Getindex(tupple, i):
    return tupple[i]


def Index(tupple, i):
    return tupple.index(i)


def Length(tupple):
    return len(tupple)
