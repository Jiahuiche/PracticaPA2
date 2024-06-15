
from arbre_binari_amb_nodes import ArbreBinari
from individu import Individu
from pytokr import pytokr

item = pytokr()

class C_individus:
    def __init__(self, nombreindividus):
        self.__individus__ = [0]*(nombreindividus+1)
        self.__arbre_genealogic__ = ArbreBinari()

    #Metode public
    def consulta_individu(self, nom_individu):
        individu = self.__individus__[nom_individu]
        return individu.informar()  #individu és una instància d'Individu,per això pot usar mètodes d'Individu.
    
    def llegeix_arbrebinari_int(self,marca):
        x = int(item()) 
        if x != marca:
            l = self.llegeix_arbrebinari_int(marca)
            r = self.llegeix_arbrebinari_int(marca)
            arbol = ArbreBinari(x,l,r)
            return arbol
        else:
            arbol = ArbreBinari()
            return arbol
    
    def assignar_arbre(self):
        self.__arbre_genealogic__ = self.llegeix_arbrebinari_int(0)
        self.consulta_arbre()
        
        
    def consulta_arbre(self):
        print(self.__arbre_genealogic__.preordre())
        subarbol = self.__arbre_genealogic__.subarbre({3,4,5})
        print(subarbol)
    
    def consultar_genoma(self, ID):
        return self.__individus__[ID].get_cromosomes()
    
    def afegir_features(self, tret, nom, c_trets):
        c_trets.afegir_tret(tret,self.__individus__[nom])

    def subarbre(self,tret,c_trets):
        if c_trets.tret_in_dic(tret):
            set = c_trets.get_set(tret)
            subarbol = self.__arbre_genealogic__.subarbre(set)
            print(subarbol)
        else:
            print('error')

    def afegir_individus(self,nom_individu,cromosomes):
        self.__individus__[nom_individu]=Individu(nom_individu,cromosomes)
    
        
        
    
    
