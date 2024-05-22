from conjunt_individus.py import C_individus
from conjunt_trets.py import C_trets

#kdkdkkd 
class Experiment:
    def __init__(self):
        self.__conjunt_individus__ = C_individus()
        self.__conjunt_trets__ = C_trets()
        
    #Metodes publics
    def afegir_tret(self, nom_tret, nom_individu):
        #PENDIENTE

    def consulta_tret(self, nom_tret):
        self.__conjunt_trets__.consulta_tret(nom_tret)

    def consulta_individu(self, nom_individu):
        #PENDIENTE
        #self.__conjunt_individus__.consulta_individu(nom_individu)

    def distribucio_tret(self, nom_tret):
        #PENDIENTE
        #self.__conjunt_trets__.distribucio_tret(nom_tret)

    #Metodes privats
    def afegir_individu(self, nom_individu):
        self.__conjunt_individus__.afegir_individu(nom_individu)
        
    
