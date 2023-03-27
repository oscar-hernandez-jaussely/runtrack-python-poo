
class Livre:
    def __init__(self):
        self.__titre = ""
        self.__auteur = ""
        self.__pages = 0


    def get_titre(self):
        return self.__titre
    
    def get_auteur(self):
        return self.__auteur
    
    def get_pages(self):
        return self.__pages
    
    def set_titre(self, valeur):
        if type(valeur) == str:
            self.__titre = valeur

    def set_auteur(self, valeur):
        if type(valeur) == str:
            self.__auteur = valeur

    def set_pages(self, valeur):
        if type(valeur) == int and valeur > 0 :
            self.__pages = valeur
        elif type(valeur) == float and valeur < 0 :
            return("Erreur, le nombre de pages doit être un nombre entier positif")
        elif valeur < 0 :
            return("Erreur, le nombre de pages doit être un nombre positif")
        elif type(valeur) == float :
            return("Erreur, le nombre de pages doit être un nombre entier")
    
    def get_livre(self):
        return("Ce livre s'intitule {}, a été écrit par {}, et comporte {} pages.".format(self.__titre, self.__auteur, self.__pages))
    

Livre = Livre()

