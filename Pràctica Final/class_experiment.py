from conjunt_individus import C_individus
from conjunt_trets import C_trets


class Experiment:
    def __init__(self,n):
        self.__conjunt_individus__ = C_individus(n)
        self.__conjunt_trets__ = C_trets()
        
    #Metodes publics
    def afegir_tret(self, nom_tret, nom_individu):
        self.__conjunt_individus__.afegir_features(nom_tret, nom_individu, self.__conjunt_trets__)

    def consulta_tret(self, nom_tret):
        self.__conjunt_trets__.consulta_tret(nom_tret)

    def consulta_individu(self, nom_individu):
        self.__conjunt_individus__.consulta_individu(nom_individu)

    def distribucio_tret(self, nom_tret):
        self.__conjunt_individus__.subarbre(nom_tret, self.__conjunt_trets__)
        
    #Metodes privats
    def _crear_arbol(self):
        self.__conjunt_individus__.assignar_arbre()
        

    def _afegir_individu(self, ID, cromosoma):
        self.__conjunt_individus__.afegir_individus(ID,cromosoma)
        
        
    
