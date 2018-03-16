import datetime


class Person:

    def __init__(self, name):
        assert type(name) is str
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]

    def getLastName(self):
        return self.lastName

    def setBirthday(self, month, day, year):
        self.birthday = datetime.date(year, month, day)

    def getAge(self):
        if self.birthday is None:
            raise ValueError('no birthday')
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other): # less than
        assert type(other) is Person
        if self.lastName == other.lastName:
            return self.name < other.lastName
        else:
            return self.lastName < other.lastName

    def __str__(self):
        return self.name


class MitPerson(Person):

    nextIdNumber = 0 # like static

    def __init__(self, name):
        Person.__init__(self, name)
        self.id = MitPerson.nextIdNumber
        MitPerson.nextIdNumber += 1

    def getId(self):
        return self.id

    def __lt__(self, other):
        assert type(other) is MitPerson
        return self.id < other.id

    def speak(self, word):
        return self.getLastName() + ' says: ' + word

    def __str__(self):
        return self.name + 'id: ' + str(self.id)


def printList(lista):
    assert type(lista) is list
    for l in lista:
        print(l)


p1 = Person('Mark Zuckerberg')
p1.setBirthday(5,14,84)
p2 = Person('Drew Houston')
p2.setBirthday(3,4,83)
p3 = Person('Bill Gates')
p3.setBirthday(10,28,55)
p4 = Person('Andrew Gates')
p5 = Person('Steve Wozniak')
personList = [p1, p2, p3, p4, p5]
print(personList)
printList(personList)
# printList(sorted(personList))
personList.sort(); print();
printList(personList)

mit1 = MitPerson('Mark')
mit2 = MitPerson('Luke')
mit3 = MitPerson('Tony')
print(mit1 < mit2)
