# CLASSES
import random


class MyClass:

    name = 'apple'

    def __init__(self):
        self.name = 'banana'


# extends MyClass
class MyClass2(MyClass):
    def pp(self):
        print(self.name)


# COURSE STARTS HERE


class Coordinate(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

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


class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator; self.denominator = denominator;

    def __str__(self):
        return str(self.numerator) + ' / ' + str(self.denominator)

    def getNumerator(self):
        return self.numerator
    def getDenominator(self):
        return self.denominator

    def __add__(self, other):
        num = other.getDenominator()*self.getNumerator() \
              + other.getNumerator()*self.getDenominator()
        den = other.getDenominator()*self.getDenominator()
        return Fraction(num, den)
    def __sub__(self, other):
        num = other.getDenominator()*self.getNumerator() \
              - other.getNumerator()*self.getDenominator()
        den = other.getDenominator()*self.getDenominator()
        return Fraction(num, den)
    def convert(self):
        return self.getNumerator() / self.getDenominator()


class IntSet:
    def __init__(self):
        self.vals = []
    def insert(self, e):
        if not e in self.vals:
            self.vals.append(e)
    def isPresent(self, e):
        return e in self.vals
    def remove(self, e):
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e)+' not present in the list')
    def __str__(self):
        self.vals.sort()
        result = ''
        for e in self.vals:
            result = result + str(e) + ','
        result = result[:-1] # remove last ','
        return '{' + result + '}'



c = Coordinate(3, 4)
origin = Coordinate(0, 0)
print(c.distance(origin))
print(Coordinate.distance(c, origin)) # makes it static, need arg for 'self'
print(c)
print(isinstance(c, Coordinate)) # True
print(origin - c)

c2 = c # now same obj, like in list
c2.x = 3.14
print(c.x)
print()

oneHalf = Fraction(1, 2)
twoThirds = Fraction(2, 3)
print(oneHalf)
print(Fraction.getNumerator(twoThirds))
print(Fraction.__sub__(oneHalf, twoThirds))
print()

s = IntSet()
s.insert(3); s.insert(4); s.insert(3)
print(s)
print(s.isPresent(5))


# INHERITANCE

class Animal(object):

    def __init__(self, age):
        self.age = age
        self.name = None

    def getAge(self):
        return self.age
    def getName(self):
        return self.name
    def setAge(self, age):
        self.age = age
    def setName(self, name):
        self.name = name

    def __str__(self):
        return "animal:"+str(self.name)+":"+str(self.age)


class Cat(Animal):
    def speak(self):
        print('meow')
    def __str__(self):
        return "cat:"+str(self.name)+":"+str(self.age)


class Rabbit(Animal):
    tag = 0 # static counter
    def __init__(self, age):
        Animal.__init__(self, age)
        Rabbit.tag += 1
        self.id = Rabbit.tag
    def speak(self):
        print('meep')
    def __str__(self):
        return "rabbit:" + str(self.name) + ":" + str(self.age)


class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        Animal.setName(self, name)
        self.friends = []
    def getFriends(self):
        return self.friends
    def addFriend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def speak(self):
        print('hello')
    def age_diff(self, other):
        diff = self.getAge() - other.getAge()
        if diff < 0:
            print(self.name, 'is', abs(diff), 'younger than', other.name)
        else:
            print(self.name, 'is', diff, 'older than', other.name)
    def __str__(self):
        return 'person:'+str(self.name)+":"+str(self.age)


class Student(Person):
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self.major = major
    def changeMajor(self, major):
        self.major = major
    def speak(self):
        r = random.randint(0, 15)
        print('i need sleep, '+str(r))
    def __str__(self):
        return 'student:' + str(self.name) + ":" + str(self.age) + ":" + str(self.major)


jelly = Cat(1)
jelly.setName('JellyBelly')
print(jelly)
print(Animal.__str__(jelly))
p1 = Person('Mark', 30)
p2 = Person('Lucas', 42)
p1.age_diff(p2)
st1 = Student('Tony', 22, 'Telecomunication')
print(st1)
st1.speak()
rab1 = Rabbit(2); rab2 = Rabbit(1); rab3 = Rabbit(2);
print(Rabbit.tag)
print(rab2.id)
