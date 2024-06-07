from arbre_binari_amb_nodes import ArbreBinari
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
            return ArbreBinari(x,l,r)
        else:
            return ArbreBinari()
    def assignar_arbre(self, arbre):
        self.__arbre_genealogic__ = arbre
    def consulta_arbre(self):
        self.__arbre_genealogi__.preorde()
        
    def afegir_genoma(self, individu, cromosomes):
        self.__individus__[individu].construir_cromosomes(str)

    def consultar_genoma(self, ID):
        return self.__individus__[ID].get_cromosomes()
    
    def afegir_features(tret, nom, c_trets):
        c_trets.afegir_tret(tret,self.__individus__[nom])

    #Metode privat
    def afegir_individu(self,nom_individu,cromosomes):
        self.__individus__[nom_individu]=Individu(nom_individu,cromosomes)
        
        
    
    
