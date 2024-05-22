from conjunt_individus.py import C_individus
from conjunt_trets.py import C_trets

class Experiment:
    def __init__(self):
        self.__conjunt_individus__ = C_individus()
        self.__conjunt_trets__ = C_trets()
        
    #Metodes publics
    def afegir_tret(self, nom_tret, nom_individu):
        self._conjunt_trets__.afegir_tret(nom_tret, nom_individu)

    def consulta_tret(self, nom_tret):
        self.__conjunt_trets__.consulta_tret(nom_tret)

    def consulta_individu(self, nom_individu):
        self.__conjunt_individus__.consulta_individu(nom_individu)

    def distribucio_tret(self, nom_tret):
        self.__conjunt_trets__.distribucio_tret(nom_tret)
        
    #Metodes privats
    def __afegir_individu(self, nom_individu):
        self.__conjunt_individus__.afegir_individu(nom_individu)

    def __crear_arbol(self, lst):
        self.__conjunt_individus__.crear_arbol(lst)

    def __construir_cromosomes(self,str):
        self._conjunt_individus__.afegir_genoma(str)
        
        
    
