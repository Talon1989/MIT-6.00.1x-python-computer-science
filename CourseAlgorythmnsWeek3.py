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
    nums = (); words = ();  # instantiation of tuple
    for t in aTuple:
        nums = nums + (t[0],)
        words = words + (t[1],)
    largest = max(nums)
    return largest, nums, words


q, r = quotientAndRemainder(13, 5)
t = ((1, "one"), (2, "two"), (5, "banana"), (3, "car"))
large, numbers, words = get_data(t)
print(large, words)