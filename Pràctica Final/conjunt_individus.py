from ArbreBinari import ArbreBinari
from individu import Individu

class C_individus:
    def __init__(self, nombreindividus):
        self.__arbre_genealogic__ = ArbreBinari()
        self.__individus__ = [Individu()]*nombreindividus
    #Metode public
    def consulta_individu(self, nom_individu):
        individu = self.__individus__[nom_individu]
        return individu.informar() #individu és una instància d'Individu,per això pot usar mètodes d'Individu.
    
    def llegeix_arbrebinari_int(self,marca):
        x = int(item()) 
        if x != marca:
            l = self.llegeix_arbrebinari_int(marca)
            r = self.llegeix_arbrebinari_int(marca)
            return self.__arbre_genealogic__(x,l,r)
        else:
            return self.__arbre_genealogic__()

    def afegir_genoma(self, individu):
        self.__individus__[individu].construir_cromosomes


    #Metode privat
    def afegir_individu(self,nom_individu):
        self.__individus__[nom_individu]=Individu(nom_individu)
        
        
    
    