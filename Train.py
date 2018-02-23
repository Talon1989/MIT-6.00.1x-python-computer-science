def bisectionalIteration(numbers, num):
    low = 0; high = len(numbers);
    while True:
        print("low: "+str(low)+" / high: "+str(high))
        mid = (low + high) // 2;
        if num == numbers[mid]:
            return True;
        elif low == high or low == high-1:
            return False
        elif num < numbers[mid]:
            high = mid;
        elif num > numbers[mid]:
            low = mid;


def bisectionalRecursion(numbers, num):
    if len(numbers) == 1:
        if num == numbers[0]:
            return True;
        else:
            return False;
    low = 0; high = len(numbers); mid = (low+high) // 2;
    if num == numbers[mid]:
        return True
    elif num < numbers[mid]:
        return bisectionalRecursion(numbers[:mid], num)
    elif num > numbers[mid]:
        return bisectionalRecursion(numbers[mid:], num)


def bisectionalSquare(x):
    epsilon = 0.001; low = 1.0; high = x;
    guess = (low + high) / 2.0;
    while abs(guess**2 - x) >= epsilon:
        if guess**2 > x:
            high = guess
        else:
            low = guess
        guess = (low + high) / 2.0;
    y = int(guess)
    if 0.999 < guess % y < 1:  # same as : guess%y > 0.999 and guess%y < 1
        guess = y+1;
    print("closes square of "+str(x)+" is "+str(guess))


def sumAndProduct(num1, num2):
    return num1+num2, num1*num2


def iterateDictionary():
    my_dictionary = {"Fabio": "Italy", "Gin": "UK", "Tom": "Canada"}
    print(my_dictionary.keys())
    print(my_dictionary.values())
    print(my_dictionary)


# prep ------------------------------------------


def isPalindrome(text):
    '''
    :param text: text
    :return: is palindrome ?
    '''
    if len(text) <= 1:
        return True
    return text[0] == text[-1] and isPalindrome(text[1:-1])


fibonacciCounter = 0
def fibonacci(num):
    '''
    :param num: integer number
    :return: num-th iteration of fibonacci
    '''
    global fibonacciCounter
    fibonacciCounter += 1
    if num == 1 or num == 0:
        return 1;
    else:
        return fibonacci(num-1) + fibonacci(num-2)


improvedFibonacciCounter = 0
def improvedFibonacci(num, d):
    '''
    :param num: integer number
    :param d: dictionary with basic values {1:1, 2:2}
    :return: num-th iteration of fibonacci
    '''
    global improvedFibonacciCounter
    improvedFibonacciCounter += 1
    if num in d:
        return d[num]
    else:
        answer = improvedFibonacci(num-1, d) + improvedFibonacci(num-2, d)
        d[num] = answer
        return answer


def hanoi(n, fr, to, spare):
    '''
    :param n: size of hanoi tower
    :param fr: starting position
    :param to: ending position
    :param spare: spare position
    :return: void
    '''
    if n == 1:
        print('move from', fr, 'to', to)
    else:
        hanoi(n-1, fr, spare, to)
        hanoi(1, fr, to, spare)
        hanoi(n-1, spare, to, fr)


def closesRoot(num):
    '''
    :param num: positive number
    :return: closest square root, if multiple ending decimal digit, consider perfect
    '''
    epsilon = 0.001
    low = 1
    high = num
    ans = (low + high) / 2
    while abs(ans**2-num) > epsilon:
        if ans**2 > num:
            high = ans
        else:
            low = ans
        ans = (low + high) / 2
    return ans


bisectionalSquare(81)
myDictionary = {}
myDictionary.update({'banana': 1}) # update in dictionary == append in list
myDictionary.update({'apple': 1.2})
# hanoi(3, 'left', 'right', 'center')
print(closesRoot(2568.56))
