from enum import Enum


class Animal:
    def __init__(self, name):
        self.name = name
        self.age = None

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getAge(self):
        return self.age

    def setAge(self, age):
        self.age = age

    def __str__(self):
        return self.name+':'+str(self.age)


class Type(Enum):
    HUMAN = 'human'
    APE = 'ape'
    MONKEY = 'monkey'

class Primate(Animal):
    def __init__(self, name, _type):
        assert isinstance(_type, Type)
        Animal.__init__(self, name)
        self._type = _type
    def getType(self):
        return self._type
    def setType(self, _type):
        assert isinstance(_type, Type)
        self._type = _type
    def __str__(self):
        return self.name+':'+str(self._type.name)+':'+str(self.age)

def powersOfFiveTimes(num):
    try:
        num = int(num)
        for i in range(5):
            yield num**i
    except ValueError:
        raise ValueError("can't cast to int")

# ------------------------------

def bubbleSort(L):
    isSorted = False
    while not isSorted:
        isSorted = True
        for i in range(1, len(L)):
            if L[i-1] > L[i]:
                L[i-1], L[i] = L[i], L[i-1]
                isSorted = False

def selectionSort(L):
    for i in range(len(L)):
        min = i
        for y in range(i, len(L)):
            if L[y] < L[min]:
                min = y
        L[min], L[i] = L[i], L[min]

def mergeSort(L):
    def merge(left, right):
        l, r = 0, 0
        assimilator = []
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                assimilator.append(left[l])
                l += 1
            else:
                assimilator.append(right[r])
                r += 1
        if l < len(left):
            assimilator.extend(left[l:])
        if r < len(right):
            assimilator.extend(right[r:])
        return assimilator
    if len(L) < 2:
        return L[:]
    mid = len(L) // 2
    left = mergeSort(L[:mid])
    right = mergeSort(L[mid:])
    return merge(left, right)


buzuzu = Primate('buzuzu', Type.APE)
buzuzu.setAge(12)
print(buzuzu)

numbers = [56, 22, 16, 99, 5, 11, 76, 33, 69, 81, 7]
print(numbers)
numbers = mergeSort(numbers)
print(numbers)