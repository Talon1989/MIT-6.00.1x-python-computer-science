def genFibonacci(numbers):
    print('inside')
    assert isinstance(numbers, int)
    if numbers < 1:
        raise Exception('number arg needs to be an int higher than 0')
    num1 = 0
    num2 = 1
    for _ in range(numbers):
        yielded = num1 + num2
        yield yielded
        num1 = num2
        num2 = yielded


for y in genFibonacci(15):
    print(y)
