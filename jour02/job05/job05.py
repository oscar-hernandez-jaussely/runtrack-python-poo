
class Forme:

    def aire(self):
        return 0
    
class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        super().__init__()
        self.largeur = largeur
        self.hauteur = hauteur

    def set_hauteur(self, valeur):
        if type(valeur) == int:
            self.hauteur = valeur

    def set_largeur(self, valeur):
        if type(valeur) == int:
            self.largeur = valeur

    def get_hauteur(self):
        return self.hauteur

    def get_largeur(self):
        return self.largeur

    def aire(self):
        super().aire()
        return (self.largeur * self.hauteur)
    
class Cercle(Forme):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def set_radius(self, valeur):
        if type(valeur) == int:
            self.radius = valeur
    
    def get_radius(self):
        return self.radius

    def aire(self):
        super().aire()
        return self.radius
    

R = Rectangle(0, 0)
C = Cercle(0)


