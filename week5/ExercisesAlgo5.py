class Coordinate(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __eq__(self, other):
        return self.getX() == other.getX() and self.getY() == other.getY()

    def __repr__(self):
        return "Coordinate("+str(self.getX())+","+str(self.getY())+")"

    def distance(self, other):
        '''
        :param other: another instance of Coordinate class
        :return: distance between the two coordinates
        '''
        assert type(other) is Coordinate
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5

    def __str__(self): # @Override toString in java
        return 'Coordinate: <' + str(self.x) + ',' + str(self.y) + '>'

    def __sub__(self, other): # subtract two Coordinates when '-'
        return Coordinate(self.x - other.x, self.y - other.y)


class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def intersect(self, other):
        '''
        :param other: other 'intSet' class
        :return: new 'intSet' containing elements that appear in both sets
        '''
        assert type(other) is intSet
        newInitSet = intSet()
        for e in self.vals:
            if e in other.vals:
                newInitSet.vals.append(e)
        return newInitSet

    def __len__(self):
        return len(self.vals)
