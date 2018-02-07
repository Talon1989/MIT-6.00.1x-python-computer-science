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


