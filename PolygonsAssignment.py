import cmath


def polysum(n, s):
    '''
    :param n: number of polygon sides
    :param s: length of each side
    :return: sum of the area and the square of the perimeter of polygon with given sides, .4 digit precision
    '''
    area = (0.25 * n * s ** 2) / cmath.tan(cmath.pi / n)
    perimeter = n * s
    return round((perimeter ** 2 + area).real, 4)