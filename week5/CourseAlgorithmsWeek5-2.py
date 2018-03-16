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
        return self.name + ' says: ' + word

    def __str__(self):
        return self.name + 'id: ' + str(self.id)


class Student(MitPerson):
    pass


class UG(Student):
    def __init__(self, name, year):
        MitPerson.__init__(self, name)
        self.classYear = year
    def speak(self, word):
        return MitPerson.speak(self, 'Dude: ' + word)


class Grad(Student):
    pass


class TransferStudent(Student):
    pass


class Professor(MitPerson):
    def __init__(self, name, department):
        MitPerson.__init__(self, name)
        self.department = department
    def speak(self, word):
        phrase = 'In course ' + self.department + 'we say: ' + word
        return MitPerson.speak(self, phrase)
    def lecture(self, topic):
        return self.speak('it is obvious that ' + topic)


def isStudent(obj):
    # isinstance checks also the parent unlike 'type()'
    return isinstance(obj, Student)


class Grades:
    def __init__(self):
        self.students = []
        self.grades = {}
        self.isSorted = True
    def addStudent(self, student):
        assert isinstance(student, Student)
        if student in self.students:
            raise ValueError(student, 'is duplicate.')
        self.students.append(student)
        self.grades[student.getId()] = []
        self.isSorted = False
    def addGrade(self, student, grade):
        try:
            self.grades[student.getId()].append(grade)
        except KeyError:
            raise ValueError('Student not in grades')
    def getGrades(self, student):
        try:
            return self.grades[student.getId()][:]
        except KeyError:
            raise ValueError('Student not in grades')
    def allStudents(self):
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        return self.students[:]



def printList(lista):
    assert type(lista) is list
    for l in lista:
        print(l)


def gradeReport(course):
    assert isinstance(course, Grades)
    report = []
    for s in course.allStudents():
        tot = 0.0; counter = 0;
        for g in course.getGrades(s):
            tot += g
            counter += 1
            print(counter)
        try:
            avg = tot / counter
            report.append('student:'+str(s)+': has an mean grade of '+str(avg))
        except ZeroDivisionError:
            report.append('student:'+str(s)+': has no grades')
    return '\n'.join(report)


def genTest():
    yield 1
    yield 2


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
print(isinstance(mit1, Person))

grad = Grades()
mark = UG('Mark Lenn', 2018)
grad.addStudent(mark)
Grades.addGrade(grad, mark, 8.9)
Grades.addGrade(grad, mark, 9.2)
print(grad.getGrades(mark))
print(gradeReport(grad))

generator = genTest()
print(generator)
print(generator.__next__())
print(generator.__next__())
print()
gen2 = genTest()
for y in gen2:
    print(y)