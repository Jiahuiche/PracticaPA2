from conjunt_individus import C_individus
from conjunt_trets import C_trets

class Experiment:
    def __init__(self):
        self.__conjunt_individus__ = C_individus()
        self.__conjunt_trets__ = C_trets()
        
    #Metodes publics
    def afegir_tret(self, nom_tret, nom_individu):
        self._conjunt_individus__.afegir_features(nom_tret, nom_individu, self.__conjunt_trets__)

    def consulta_tret(self, nom_tret):
        self.__conjunt_trets__.consulta_tret(nom_tret)

    def consulta_individu(self, nom_individu):
        self.__conjunt_individus__.consulta_individu(nom_individu)

    def distribucio_tret(self, nom_tret):
        self.__conjunt_individus__.crear_subarbre(nom_tret, self.__conjunt_trets__)
        
    #Metodes privats
    def __afegir_individu(self, nom_individu):
        self.__conjunt_individus__.afegir_individu(nom_individu)

    def __crear_arbol():
        self.__conjunt_individus__.llegir_arbre_int(0)

    def __assignar_cromosomes(self,i,str):
        self._conjunt_individus__.afegir_genoma(i,str)
        
        
    
