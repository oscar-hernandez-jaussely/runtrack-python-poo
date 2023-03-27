
class Animal:
    def __init__(self):
        age = 0
        name = ""
        self.age = age
        self.name = name

    def vieillir(self):
        self.age = self.age + 1
        print ("L'age de l'animal {} ans" .format(int(self.age)))

    def nommer(self, name):
        self.name = name
        print("L'animal se nomme " + self.name)

Animal_1 = Animal()

