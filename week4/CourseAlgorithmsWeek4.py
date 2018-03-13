# TESTING AND DEBUGGING

def rem(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the remainder when x is divided by a.
    """
    print(x, a)
    if x == a:
        return 0
    elif x < a:
        return x
    else:
        return rem(x - a, a)


def f(n):
    """
    n: integer, n >= 1.
    """
    if n == 1:
        return n
    else:
        return n * f(n - 1)


# EXCEPTIONS AND ASSERTIONS

def tryCatch(myList):
    v = -1
    try:
        v = myList[len(myList)]
    except IndexError:
        print('index error mate.')
    finally:
        print("ready to print v ...")
    print(v)


def entNum():
    while True:
        try:
            n = input("Please enter an integer")
            n = int(n)
            # break
        except ValueError:
            print(n, 'is not an integer')
        # same as break above
        else:
            break
    print("Exiting program...")


def getRatios(l1, l2):
    '''
    :param l1: list of numbers of size x
    :param l2: list of number of size x
    :return: a list containing l1[i]/l2[i]
    '''
    assert type(l1) is list; assert type(l2) is list
    assert len(l1) == len(l2), "list not of the same size"
    ratios = []
    for i in range(len(l1)):
        try:
            ratios.append(l1[i] / l2[i])
        except ZeroDivisionError:
            ratios.append(float('NaN'))
        except:
            raise ValueError('bad argument')
    return ratios


def normalize(numbers):
    max_number = max(numbers)
    for i in range(len(numbers)):
        numbers[i] /= float(max_number)
    return numbers

# try:
#       normalize([0, 0, 0])
# except ZeroDivisionError:
#       print('Invalid maximum element')


l = [4, 79, 9]
print(getRatios(l, [2,2]))
