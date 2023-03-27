
class Livre:
    def __init__(self):
        self.__titre = ""
        self.__auteur = ""
        self.__pages = 0
        self.__disponible = True


    def get_titre(self):
        return self.__titre
    
    def get_auteur(self):
        return self.__auteur
    
    def set_titre(self, valeur):
        if type(valeur) == str:
            self.__titre = valeur

    def set_auteur(self, valeur):
        if type(valeur) == str:
            self.__auteur = valeur

    def set_pages(self, valeur):
        if type(valeur) == int:
            self.__pages = valeur

    def vérification(self):
        if self.__disponible == True:
            return True
        else:
            return False
        
    def emprunter(self):
        if self.vérification() == True:
            self.__disponible = False
            return True
        else:
            return False
        
    def rendre(self):
        if self.vérification() == False:
            self.__disponible = True
            return True
        else:
            return False
    
    def get_livre(self):
        return("Ce livre s'intitule {}, a été écrit par {}, et comporte {} pages.".format(self.__titre, self.__auteur, self.__pages))
    

Livre = Livre()

