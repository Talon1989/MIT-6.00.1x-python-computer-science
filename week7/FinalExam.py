def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
        If there are no digits in s it raises a ValueError exception. """
    assert isinstance(s, str)
    listOfDigits = []
    sum = 0
    flag = True
    for l in s:
        try:
            sum += int(l)
            flag = False
        except ValueError:
            pass
    if flag:
        raise ValueError
    return sum

# -----------------------------------------------------------------

def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other.
            If they are permutations of each other, returns a
            tuple of 3 items in this order:
            the element occurring most, how many times it occurs, and its type
    '''
    dicL1 = {}
    dicL2 = {}
    if len(L1) == 0 and len(L2) == 0:
        return None, None, None
    for e in L1:
        if dicL1.get(e, 0) > 0:
            dicL1[e] += 1
        else:
            dicL1[e] = 1
    for e in L2:
        if dicL2.get(e, 0) > 0:
            dicL2[e] += 1
        else:
            dicL2[e] = 1
    if dicL1 != dicL2:
        return False
    else:
        bestPos = next(iter(dicL1))
        for d in dicL1:
            if dicL1[d] > dicL1[bestPos]:
                bestPos = d
        return bestPos, dicL1[bestPos], type(bestPos)

# -----------------------------------------------------------------

def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain
                          N unique lowercase letters.
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where
        each key is a letter in map_from at index i and the corresponding
        value is the letter in map_to at index i.
        decoded is a string that contains the decoded version
        of code using the key_code mapping. """
    key_code = {}
    for m in range(len(map_from)):
        if key_code.get(map_from[m]) is None:
            key_code[map_from[m]] = map_to[m]
    decoded = ''
    for c in code:
        if key_code.get(c) is not None:
            decoded += key_code[c]
    return key_code, decoded

# -----------------------------------------------------------------

class Person(object):
    def __init__(self, name):
        self.name = name
    def say(self, stuff):
        return self.name + ' says: ' + stuff
    def __str__(self):
        return self.name

class Lecturer(Person):
    def lecture(self, stuff):
        return 'I believe that ' + Person.say(self, stuff)

class Professor(Lecturer):
    def say(self, stuff):
        return self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor):
    def say(self, stuff):
        return self.name+' says: '+self.lecture(stuff)
    def lecture(self, stuff):
        return 'It is obvious that ' + Person.say(self, stuff)

# -----------------------------------------------------------------

class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """
    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object
            occurs 0 times in self. """
        self.vals = {}
    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1
    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i)+":"+str(self.vals[i])+"\n"
        return s

class Bag(Container):
    def remove(self, e):
        """ assumes e is hashable
            If e occurs in self, reduces the number of
            times it occurs in self by 1. Otherwise does nothing. """
        # if self.vals.get(e, 0) > 0:
        #     self.vals[e] -= 1
        try:
            self.vals[e] -= 1
        except KeyError:
            pass

    def count(self, e):
        """ assumes e is hashable
            Returns the number of times e occurs in self. """
        return self.vals.get(e, 0)

d1 = Bag()
d1.insert(4)
d1.insert(4)
print(d1)
d1.remove(2)
print(d1)
