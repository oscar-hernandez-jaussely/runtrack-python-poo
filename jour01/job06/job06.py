
class Rectangle:
    def __init__(self):
        self.__longueur = 0
        self.__largeur = 0

    def get_longueur(self):
        return self.__longueur
    
    def get_largeur(self):
        return self.__largeur
    
    def set_longueur(self, valeur):
        if type(valeur) == int:
            self.__longueur = valeur
        else:
            print('mauvais type')

    def set_largeur(self, valeur):
        if type(valeur) == int:
            self.__largeur = valeur
        else:
            print('mauvais type')
    
    def get_rectangle(self):
        return("Les dimensions du rectangle sont de {} de longueur pour {} de largeur".format(self.__longueur, self.__largeur))



Rectangle = Rectangle()

