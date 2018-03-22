class Drink:
    def __init__(self, name, abv):
        assert isinstance(name, str)
        assert isinstance(abv, int)
        self.name = name
        self.abv = abv
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
    def getAbv(self):
        return self.abv
    def setAbv(self, abv):
        self.abv = abv
    def isAlcoholic(self):
        return self.abv > 0


class Water(Drink):
    def __init__(self):
        Drink.__init__(self, 'water', 0)


class SoftDrink(Drink):
    def __init__(self, name):
        Drink.__init__(self, name, 0)


class Beer(Drink):
    def __init__(self, name, abv):
        assert 1 < abv < 10
        Drink.__init__(self, name, abv)


def bubbleSort(L):
    clean = False
    while not clean:
        clean = True
        for i in range(1, len(L)):
            if L[i-1] > L[i]:
                L[i-1], L[i] = L[i], L[i-1]
                clean = False

def selectionSort(L):
    for a in range(len(L)):
        min = a
        for b in range(a, len(L)):
            if L[b] < L[min]:
                min = b
        L[min], L[a] = L[a], L[min]

def mergeSort(L):
    if len(L) < 2:
        return L[:]
    def merge(left, right):
        result = []
        l, r = 0, 0
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
        if l < len(left):
            result.extend(left[l:])
        if r < len(right):
            result.extend(right[r:])
        return result
    mid = len(L) // 2
    lleft = mergeSort(L[:mid])
    rright = mergeSort(L[mid:])
    return merge(lleft, rright)


def meth(a = 'a', b = 'b', c = 'c'):
    print(a,b,c)

meth(b='asd')


# birraMoretti = Beer('moretti', 5)
# print(birraMoretti.getName(), ' / ', birraMoretti.getAbv())
# print(birraMoretti.isAlcoholic())
# acqua = Water()
# print(acqua.isAlcoholic())
ll = ['hotel', 'alpha', 'lima', 'india', 'charlie', 'zulu', 'bravo', '123']
ll = mergeSort(ll)
print(ll)

