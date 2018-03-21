class Drink:
    def __init__(self, name, abv):
        assert isinstance(name, str)
        assert isinstance(abv, int)
        self.name = name
        self.abv = abv
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
    def getAbv(self):
        return self.abv
    def setAbv(self, abv):
        self.abv = abv
    def isAlcoholic(self):
        return self.abv > 0


class Water(Drink):
    def __init__(self):
        Drink.__init__(self, 'water', 0)


class SoftDrink(Drink):
    def __init__(self, name):
        Drink.__init__(self, name, 0)


class Beer(Drink):
    def __init__(self, name, abv):
        assert 1 < abv < 10
        Drink.__init__(self, name, abv)


birraMoretti = Beer('moretti', 5)
print(birraMoretti.getName(), ' / ', birraMoretti.getAbv())
print(birraMoretti.isAlcoholic())
acqua = Water()
print(acqua.isAlcoholic())
