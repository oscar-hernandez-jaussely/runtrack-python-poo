
class Vehicule:
    def __init__(self, marque, année, prix):
        self.marque = marque
        self.année = année
        self.prix = prix

    def informationsVehicule(self):
        return self.marque , self.année , self.prix
    
    def demarrer(self):
        return ("Attention, je roule.")

class Voiture(Vehicule):
    def __init__(self, marque, année, prix, portes=4):
        super().__init__(marque, année, prix)
        self.portes = portes

    def informationsVehicule(self):
        return super().informationsVehicule(), self.portes
    
    def demarrer(self):
        super().demarrer()
        return("V8 goes brrrrrr")


class Moto(Vehicule):
    def __init__(self, marque, année, prix, roue=2):
        super().__init__(marque, année, prix)
        self.roue = roue

    def informationsVehicule(self):
        return super().informationsVehicule(), self.roue
    
    def demarrer(self):
        super().demarrer()
        return("Rolling thunder time")
    

Karmann_Ghia = Voiture("Volkswagen", "1955", "35000")

R_18 = Moto("BMW", "2020", "24000")

