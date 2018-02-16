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


t = ('we', 1, 'are', 'not', 'alone', 123, 555)
print(oddTuples(t))

