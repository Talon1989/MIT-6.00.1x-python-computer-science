class Tt:

    def method(self):
        self.banana = 'ban'


one = Tt()
one.method()
print(one.banana)


def genPrimes():
    num = 2
    while True:
        flag = True
        for n in range(2, num):
            if num % n == 0:
                flag = False
                break
        if flag:
            yield num
        num += 1


p = genPrimes()
print(p.__next__())
print(p.__next__())
print(p.__next__())
print(p.__next__())
print(p.__next__())
print(p.__next__())


def gen():
    yield 1
    print('banana')


for g in gen():
    print(g)
