
class Voiture:
    def __init__(self, marque, modèle, année, km):
        self.__marque = marque
        self.__modèle = modèle
        self.__année = année
        self.__km = km
        self.__en_marche = False
        self.__réservoir = 50


    def get_marque(self):
        return self.__marque

    def get_modèle(self):
        return self.__modèle

    def get_année(self):
        return self.__année
    
    def get_km(self):
        return self.__km
    
    def get_infos(self):
        return self.__marque , self.__modèle , self.__année , "{} km".format(self.__km)
    

    def set_marque(self, valeur):
        self.__marque = valeur

    def set_modèle(self, valeur):
        self.__modèle = valeur

    def set_année(self, valeur):
        self.__année = valeur

    def set_km(self, valeur):
        self.__km = valeur

    def set_réservoir(self, valeur):
        self.__réservoir = valeur


    def démarrer(self):
        if Voiture.__vérifier_plein(self) > 5:
            print("La voiture démarre")
            self.__en_marche = True
        else:
            print("La voiture ne démarre pas")

    def arreter(self):
        if self.__en_marche == True:
            self.__en_marche = False
        else:
            print("Le moteur n'est pas en marche")
    
    def __vérifier_plein(self):
        return self.__réservoir
    

