
class Forme:

    def aire(self):
        return 0
    
class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        super().__init__()
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        super().aire()
        return (self.largeur * self.hauteur)
    

R = Rectangle(15, 25)

R.aire()

