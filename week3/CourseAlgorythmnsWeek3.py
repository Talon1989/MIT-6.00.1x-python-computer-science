import cmath


def findnum(num, arr):
    if len(arr) == 1:
        if num == arr[0]:
            return True
        else:
            return False;
    low = 0; high = len(arr);
    mid = (low + high) // 2;
    if num == arr[mid]:
        return True
    elif num < arr[mid]:
        return findnum(num, arr[low:mid:]);
    else:
        return findnum(num, arr[mid:high:]);


# RETURNS A TUPLE
def quotientAndRemainder(x, y):
    q = x // y;
    r = x % y
    return q, r;


def get_data(aTuple):
    someTuple = (1, True, 'banana')
    nums = (); words = ();  # instantiation of tuple
    for t in aTuple:
        nums = nums + (t[0],)
        words = words + (t[1],)
    largest = max(nums)
    return largest, nums, words


# LIST IS MUTABLE
def lists():
    a_list = ['a list']
    b_list = [2, 'a', 4, True]
    print(b_list[3])
    b_list[3] = False
    print(b_list[3])
    b_list.append('potato') # doesn't mutate
    print(b_list)
    c_list = a_list + b_list
    c_list.extend([3, 5, 8]) # mutates
    print(c_list)
    s = 'abcd'
    d_list = list(s)
    print(d_list)
    print(s.split('c'))
    print('_'.join(s))


def listAliases():
    warm = ['red', 'yellow', 'orange']
    hot = warm # this means same object, points to the same memory block
    print(hot)
    warm.append('pink')  # hot[0] automatically becomes 'pink'
    print(hot)
    cool = ['blue', 'green', 'grey']
    chill = cool[:] # this means a copy, not the same object
    cool.append('black')
    print(chill)


def removeDuplicates(list1, list2):
    list1_copy = list1[:] # this makes sure when i remove it can still loop properly
    for e in list1_copy:
        if e in list2:
            list1.remove(e)


def applyToEach(l, func):
    '''
    :param l: a list
    :param func: a function
    :return: mutates l by replacing each element, e, of l by func(e)
    '''
    for i in range(len(l)):
        l[i] = func(l[i])


# similar to the 'map' function
def applyFunctions(listOfFunc, num):
    '''
    :param listOfFunc: a list of functions
    :param num: a single number
    :return: prints the num after it has been called by the listOfFunc
    '''
    for f in listOfFunc:
        print(f(num))


# DICTIONARY, behaves like maps in java
def python_dictionaries():
    my_dict = {}
    grades = {'Ana': 'B', 'John': 'A+', 'Denise': 'A', 'Katy': 'A'}
    print(grades.get('Ana')) # B
    print(grades['Ana']) # B
    grades['Talon'] = 'C' # adding new key and value to the dictionary 'grades'
    print(grades['Talon'])
    del grades['Talon'] # removed entry for 'Talon'
    print('Talon' in grades)
    print(grades); print(grades.keys()); print(grades.values())
    # dictionaries keys must be immutable, values of any type
    d = {4: {1: 0}, (1, 3): "twelve", "const": [3.14, 2.7, 6.67]}


def lyricsToFrequency(lyrics):
    '''
    :param lyrics: array of words
    :return: dictionary of words mapped to frequency
    '''
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict


def mostCommonWords(dictionary):
    '''
    :param dict: dictionary of words, mapped to frequency
    :return: most common word with its frequency, using list in case of multiple words with same max frequency
    '''
    values = dictionary.values()
    best = max(values)
    words = []
    for k in dictionary:
        if best == dictionary[k]:
            words.append(k)
    return words, best


def wordsOften(dictionary, times):
    words = []
    flag = False
    while not flag:
        if len(dictionary) < 1:
            break
        temp = mostCommonWords(dictionary)
        if temp[1] >= times:
            words.append(temp)
            for w in temp[0]:
                del dictionary[w]
        else:
            flag = True
    return words


def efficientFibonacci(n, d):
    '''
    :param n: number of iteration of fibonacci
    :param d: dictionary with basic values {1:1, 2:2}
    :return: n-th iteration of fibonacci
    '''
    global numFibCalls # takes a variable from global scope (if defined)
    numFibCalls += 1
    if n in d:
        return d[n]
    else:
        ans = efficientFibonacci(n-1, d) + efficientFibonacci(n-2, d)
        d[n] = ans # saved for future iterations
        return ans


l = [1, -2, 3.4]
print(l)
applyToEach(l, abs) # i'm passing the function itself abs, not the calling abs()
print(l)
applyFunctions([abs, cmath.sqrt], -16)
for a in map(abs, [1, -2, 3, -4, 5, -6]): # map returns an iterable, not a list
    print(a)
frequency = lyricsToFrequency(['she', 'loves', 'you', 'yeah', 'yeah', 'yeah'])
print(wordsOften(frequency, 1))
numFibCalls = 0
print(efficientFibonacci(6, {1: 1, 2: 2}), numFibCalls)