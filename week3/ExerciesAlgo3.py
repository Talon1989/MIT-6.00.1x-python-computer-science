def oddTuples(aTup):
    '''
    aTup: a tuple
    returns: tuple, every other element of aTup.
    '''
    returnTup = ()
    for i in range(len(aTup)):
        if i % 2 == 0:
            returnTup += (aTup[i],)
    return returnTup


def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.
    returns: int, how many values are in the dictionary.
    '''
    counter = 0
    for v in aDict.values():
        for _ in v:
            counter += 1
    return counter


def myBiggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.
    returns: The key with the largest number of values associated with it
    '''
    maxVals = max(aDict.values())
    for d in aDict.items():
        if maxVals == d[1]:
            return d[0]


def courseBiggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.
    returns: The key with the largest number of values associated with it
    '''
    result = ""
    biggestValue = 0
    for k in aDict.keys():
        if biggestValue < len(aDict[k]):
            biggestValue = len(aDict[k])
            result = k
    return result


animals = {'a': ['alupa'], 'b': ['baboon'], 'c': ['coati', 'cat']}
print(courseBiggest(animals))


tup1 = 1
tup2 = 2
tup1, tup2 = tup2, tup1
print(tup1, tup2)