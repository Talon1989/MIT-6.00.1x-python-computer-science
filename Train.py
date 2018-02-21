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


bisectionalSquare(81)