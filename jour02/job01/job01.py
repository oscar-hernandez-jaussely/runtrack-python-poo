
class Personne:
    def __init__(self, age=14):
        self.age = age
        
    def afficherAge(self):
        return self.age
    
    def bonjour(self):
        return ("Hello")
    
    def modifierAge(self, valeur):
        if type(valeur) == int:
            self.age = valeur

class Eleve(Personne):

    def allerEnCours():
        print("Je vais en cours")

    def affichageAge(self):
        return("J'ai {} ans".format(self.age))


class Professeur:
    def __init__(self, matiere):
        self.__matiereEnseignee = matiere

    def enseigner(self):
        print("Le cours va commencer")



Personne_1 = Personne()
Eleve_1 = Eleve()

Eleve_1.affichageAge()

