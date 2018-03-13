def fancy_divide(numbers, index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError:
        print("-1")
    else:
        print("1")
    finally:
        print("0")


def simple_divide(item, denom):
    try:
        return item / denom
    except ZeroDivisionError:
        return 0

fancy_divide([0, 2, 4], 0)
