def factIter(n):
    assert n >= 0
    answer = 1
    while n > 1:
        answer *= n
        n -= 1
    return answer
# 1 + 5n + 1
# worst case asymptotic complexity = O(n) , dominant term is n because it's linear, +1 +1 are constant


def factRec(n):
    assert n >= 0
    if n <= 1:
        return 1
    return n * factRec(n-1)


# log10 n   complexity
def intToStr(n):
    if n == 0:
        return 0
    result = ''
    while n > 0:
        result = str(n % 10) + result
        n //= 10
    return result


# exponential complexity, 2^n
def genSubsets(l):
    res = []
    if len(l) == 0:
        return [[]]
    smaller = genSubsets(l[:-1]) # all subset w/out last element
    extra = l[-1:] # list of just last element
    newer = []
    for sm in smaller:
        newer.append(sm + extra) # for elements in smaller add one with last element
    return smaller + newer


print(factIter(4))
print(intToStr(123459))
print(genSubsets([1, 2, 3]))