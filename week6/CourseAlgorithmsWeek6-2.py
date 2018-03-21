import random

# SEARCH ALGORITHMS

# O(len(L)) , not really good
def linear_search(L, e):
    for i in range(len(L)):
        if e == L[i]:
            return True
    return False

def my_bisection_search(L, e):
    if len(L) < 1:
        return False
    low = 0; high = len(L)-1
    while True:
        ans = (low + high) // 2
        if high == low:
            if e == L[ans]:
                return True
            else:
                return False
        if e == L[ans]:
            return True
        elif e < L[ans]:
            high = ans-1
        else:
            low = ans+1

# O(log2(n)) , good
def bisection_search(L, e):
    def bisect_search_helper(L, e, low, high):
        if high == low:
            return L[low] == e
        mid = (low + high) // 2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid: # nothing left to search
                return False
            else:
                return bisect_search_helper(L, e, low, mid-1)
        else:
            return bisect_search_helper(L, e, mid+1, high)
    if len(L) == 0:
        return False
    else:
        return bisect_search_helper(L, e, 0, len(L)-1)


# SORTING ALGORITHMS

# O(unbounded) retarded..
def bogo_sort(L):
    while not sorted(L) == L:
        random.shuffle(L)
        print(L)
    return L

# O(n^2) keep swapping j and j-1 if not sorted until everything is sorted
def bubble_sort(L):
    swapped = True
    while swapped: # keep redoing it from start until no swap = sorted
        swapped = False
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swapped = True
                temp = L[j-1]
                L[j-1] = L[j]
                L[j] = temp

# better, only look for the smallest value and put it at the beginning, proceed
def my_selection_sort(L):
    for i in range(len(L)):
        lowest = i
        for y in range(i, len(L)):
            if L[y] < L[lowest]:
                lowest = y
        L[lowest], L[i] = L[i], L[lowest]


# O((n^2)-n)
def selection_sort(L):
    for suffix in range(len(L)):
        for i in range(suffix, len(L)):
            if L[i] < L[suffix]:
                L[suffix], L[i] = L[i], L[suffix] # swap


# O(n*log2(n))
def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)

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
    # once one of the above is empty append the remaining of other
    if l < len(left):
        result.extend(left[l:])
    if r < len(right):
        result.extend(right[r:])
    # while l < len(left):
    #     result.append(left[l])
    #     l += 1
    # while r < len(right):
    #     result.append(right[r])
    #     r += 1
    return result





# print(my_bisection_search([1,2,3,5,8,11], 2))
# print(bogo_sort([5,6,1,2,5,8,15,99,7,159,111,55,9]))
lista = [2,1,5,9,15,66,55,158,11,3]
lista = merge_sort(lista)
print(lista)

