
class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def périmètre(self):
        p = 2 * (self.__longueur + self.__largeur)
        return p
    
    def surface(self):
        s = self.__longueur * self.__largeur
        return s
    
    def set_longueur(self, valeur):
        if type(valeur) == int:
            self.__longueur = valeur

    def set_largeur(self, valeur):
        if type(valeur) == int:
            self.__largeur = valeur

    def get_longueur(self):
        return self.__longueur
    
    def get_largeur(self):
        return self.__largeur
    

class Parallélépipède(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.hauteur = hauteur

    def volume(self):
        v = self.__longueur * self.__largeur * self.hauteur
        return v



Rectangle_1 = Rectangle(0, 0)

