def potato():
    print("potato");


def swap(one, two):
    print("value of one: "+one+" \\ value of two: "+two);
    temp = one; one = two;
    two = temp;
    print("value of one: "+one+" \\ value of two: "+two);


def countWords(s):
    counter = 0;
    prev1 = '';
    prev2 = '';
    for letter in s:
        if letter == 'b' and prev1 == 'o' and prev2 == 'b':
            counter += 1;
        prev2 = prev1;
        prev1 = letter;
    print("Number of times bob occurs is: " + str(counter));


def findLongestStringAlphOrder(s):
    count = 0; max_count = 0; last_position = 0;
    for i in range(len(s) - 1):
        if s[i] <= s[i+1]:
            count += 1;
            if count > max_count:
                max_count = count;
                last_position = i+1;
        else:
            count = 0;
    first_position = last_position-max_count;
    print(s[first_position:last_position+1]);


def findPerfectSquare(number):
    ans = 0;
    while ans**2 < abs(number):
        ans += 1;
    if ans**2 == abs(number):
        print(str(number), "is a perfect square");
    else:
        print(str(number), "is not a perfect square");


def approximationCubeRoot(cube):
    epsilon = 0.01; guess = 0.0; increment = 0.001; count = 0;
    while abs(guess**3 - cube) >= epsilon and guess**2 <= cube:
        guess += increment;
        count += 1;
    print("number of guesses: "+str(count));
    if abs(guess**3 - cube) >= epsilon:
        print("Failed.");
    else:
        print(guess, "is closest to cube root of", cube);


def bisectionSearch(x):
    epsilon = 0.01; numGuesses = 0;
    low = 1.0; high = x;
    ans = (high + low) / 2.0;
    while abs(ans**2 - x) >= epsilon:
        print("low = "+str(low)+" / high = "+str(high)+" / answer: "+str(ans));
        numGuesses += 1;
        if ans**2 < x:
            low = ans;
        else:
            high = ans;
        ans = (high + low) / 2.0;
    print("Number of guesses : "+str(numGuesses));
    print("Closest square root of "+str(x)+" : "+str(ans));


def bisectionEx():
    print("Please think of a number between 0 and 100!")
    low = 0
    high = 100
    while True:
        guess = (low + high) // 2
        print("Is your secret number "+str(guess)+"?")
        response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
        if response != 'h' and response != 'l' and response != 'c':
            print("Sorry, I did not understand your input.")
        elif response == 'h':
            high = guess
        elif response == 'l':
            low = guess
        elif response == 'c':
            print("Game over. Your secret number was: "+str(guess))
            break


def binaryFloats(x):
    isNeg = False;
    if x < 0:
        x = abs(x);
        isNeg = True;
    result = '';
    if x == 0:
        result = '0';
    while x > 0:
        result = str(x % 2) + result;
        x //= 2;
    if isNeg:
        result = '-' + result;
    return result;


def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    return a*(x**2)+b*x+c;


def evaluate(x, y, flag=False):   # In python we can bind variables inside args, don't need to call it
    if not flag:
        return x >= y;


def fibonacci(a):
    # print(a)
    if a == 1 or a == 0:
        return 1;
    return fibonacci(a-1) + fibonacci(a-2);


def oldFibonacci(a, b, times):
    if times == 0:
        return b;
    return oldFibonacci(b, a+b, times-1);


def isPalindrome(text):
    if len(text) == 0 or len(text) == 1:
        return True;
    elif text[0] == text[len(text)-1]:
        return isPalindrome(text[1:len(text)-1]);
    else:
        return False;


