
from arbre_binari_amb_nodes import ArbreBinari
from individu import Individu
from pytokr import pytokr

item = pytokr()

class C_individus:
    def __init__(self, nombreindividus):
        self.__individus__ = [0]*(nombreindividus+1)
        self.__arbre_genealogic__ = ArbreBinari()

    #Metode public
    def get_individu(self,ID):
        return self.__individus__[ID]
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

    def afegir_individus(self,nom_individu,cromosomes):
        self.__individus__[nom_individu]=Individu(nom_individu,cromosomes)

    
    def subarbre(self, set):
        def _subarbre(arbre):
            if arbre.fulla():
                return ArbreBinari(arbre.valor_arrel()) if arbre.valor_arrel() in set else ArbreBinari()
            else:
                l=_subarbre(arbre.fill_esq())
                r=_subarbre(arbre.fill_dre())
                if arbre.valor_arrel() in set:
                    return ArbreBinari(arbre.valor_arrel(),l,r)
                else:
                    if not l.buit() or not r.buit():
                        return ArbreBinari(-arbre.valor_arrel(),l,r)
                    else:
                        return ArbreBinari()
        if self.__arbre_genealogic__.buit():
            return self.__arbre_genealogic__.inordre() 
        else:
            subarbre= _subarbre(self.__arbre_genealogic__)
            return subarbre.inordre() if subarbre is not None else None
    
