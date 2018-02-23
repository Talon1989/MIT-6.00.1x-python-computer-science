def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    if base > num:
        return 0
    for i in range(1, 1000):
        if abs((base**i)-num) <= abs((base**(i+1))-num):
            return i


def getSublists(L, n):
    '''
    This function returns a list of all possible sublists in L of length n
    without skipping elements in L. The sublists in the returned list
    should be ordered in the way they appear in L,
    with those sublists starting from a smaller index being
    at the front of the list.
    '''
    newList = []
    for i in range(len(L)-n+1):
        newList.append(L[i:n+i])
    return newList


def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    newList = []
    for d in aDict.items():
        if d[1] == target:
            newList.append(d[0])
    return sorted(newList)


def keysWithValue2(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    newList = []
    for d in aDict:
        if aDict[d] == target:
            newList.append(d)
    return sorted(newList)


def flatten(aList):
    '''
    aList: a list
    Returns a copy of aList, which is a flattened version of aList
    '''
    newList = []
    for i in aList:
        if type(i) == list:
            newList.extend(flatten(i)) # extends appends another list
        else:
            newList.append(i)
    return newList


def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you.
    f takes in an integer, applies a function, returns another integer
    g takes in an integer, applies a Boolean function,
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    newList = []
    for i in L:
        if g(f(i)):
            newList.append(i)
    L[:] = newList
    if len(L) == 0:
        return -1
    return max(newList)