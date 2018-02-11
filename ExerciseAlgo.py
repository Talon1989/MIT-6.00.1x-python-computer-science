def iterPower(base, exp):
    result = base;
    if exp == 0:
        return 1;
    while exp > 1:
        result *= base;
        exp -= 1;
    return result;


def recurPower(base, exp):
    if exp == 0:
        return 1;
    if exp == 1:
        return base;
    return base * recurPower(base, exp-1);


def iterGcd(a, b):
    while a != b:
        if a > b:
            a = a-b;
        else:
            b = b-a;
    return a;


def recurGdc(a, b):
    if b == 0:
        return a;
    return recurGdc(b, a % b);


def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) <= 1 and char != aStr:
        return False;
    start = 0;
    end = len(aStr);
    mid = (start + end)//2;
    if aStr[mid] == char:
        return True;
    elif char < aStr[mid]:
        return isIn(char, aStr[start:mid]);
    else:
        return isIn(char, aStr[mid:end]);
