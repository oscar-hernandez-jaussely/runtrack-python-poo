
class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        return self.age
    
    def bonjour(self):
        print ("Hello")
    
    def modifierAge(self, valeur):
        if type(valeur) == int:
            self.age = valeur

    def get_age(self):
        return self.age
    
    def set_age(self, valeur):
        if type(valeur) == int:
            self.age = valeur  


class Eleve(Personne):

    def allerEnCours(self):
        print("Je vais en cours")

    def affichageAge(self):
        return("J'ai {} ans".format(self.age))

class Professeur():
    def __init__(self, age, matiere ="français"):
        self.__matiereEnseignee = matiere
        self.age = age

    def enseigner(self):
        print("Le cours va commencer")

    def bonjour(self):
        print ("Hello")

    def set_matiere(self, valeur):
        if type(valeur) == str:
            self.__matiereEnseignee = valeur

    def get_matiere(self):
        return self.__matiereEnseignee



Personne_1 = Personne()
Eleve_1 = Eleve()


Eleve_1.bonjour()
Eleve_1.allerEnCours()
Eleve_1.set_age(15)

Professeur_1 = Professeur(40)
Professeur_1.bonjour()
Professeur_1.enseigner()

