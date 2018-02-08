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

