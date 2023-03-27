
class Personne:
    def __init__(self, nom, prenom):
        if nom == "" and prenom == "":
            prenom = "John"
            nom = "Doe"
            self.nom = nom
            self.prenom = prenom
        else:
            self.nom = nom
            self.prenom = prenom
    def SePresenter(self):
        print("Je suis " + self.prenom + " " + self.nom)


Personne_1 = Personne("", "")


