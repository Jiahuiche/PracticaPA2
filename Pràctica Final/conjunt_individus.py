
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
        self.__individus__[nom_individu].informar() #individu és una instància d'Individu,per això pot usar mètodes d'Individu.
    
    def llegeix_arbrebinari_int(self,marca):
        x = int(item()) 
        if x != marca:
            l = self.llegeix_arbrebinari_int(marca)
            r = self.llegeix_arbrebinari_int(marca)
            return ArbreBinari(x,l,r)
        else:
            return ArbreBinari()
            
    def assignar_arbre(self):
        self.__arbre_genealogic__ = self.llegeix_arbrebinari_int(0)
    
    def afegir_features(self, tret, nom, c_trets):
        c_trets.afegir_tret(tret,self.__individus__[nom])

    def subarbre(self,tret,c_trets):
        if c_trets.tret_in_dic(tret):
            set = c_trets.get_set(tret)
            subarbol = self.__arbre_genealogic__.sub_arbre(set)
            print(' ',end='')
            for i in subarbol:
                print('',i,end='')
            print()
        else:
            print('  error')

    def afegir_individus(self,nom_individu,cromosomes):
        self.__individus__[nom_individu]=Individu(nom_individu,cromosomes)
    
        
        
    
    
