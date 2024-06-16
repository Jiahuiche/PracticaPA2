from conjunt_individus import C_individus
from conjunt_trets import C_trets


class Experiment:
    def __init__(self,n):
        self.__conjunt_individus__ = C_individus(n)
        self.__conjunt_trets__ = C_trets()
        
    #Metodes publics
    def afegir_tret(self, nom_tret, nom_individu):
        self.__conjunt_tret__.afegir_tret(nom_tret, self.__conjunt_individu__.get_individu(nom_individu))

    def consulta_tret(self, nom_tret):
        self.__conjunt_trets__.consulta_tret(nom_tret)

    def consulta_individu(self, nom_individu):
        self.__conjunt_individus__.get_individu(nom_individu).informar()

    def distribucio_tret(self, nom_tret):
        if self.__conjunt_trets__.tret_in_dic(nom_tret):
            set = self.__conjunt_trets__.get_set(nom_tret)
            subarbol = self.__conjunt_individus__.subarbre(set)
            print(' ',end='')
            for i in subarbol:
                print('',i,end='')
            print()
        else:
            print('  error')
        
    #Metodes privats
    def _crear_arbol(self):
        self.__conjunt_individus__.assignar_arbre()

    def _afegir_individu(self, ID, cromosoma):
        self.__conjunt_individus__.afegir_individus(ID,cromosoma)
        
        
    
