
from arbre_binari_amb_nodes import ArbreBinari
from individu import Individu
from pytokr import pytokr

item = pytokr()

class C_individus:
    def __init__(self, nombreindividus):
        self.__arbre_genealogic__ = ArbreBinari()
        self.__individus__ = [0]*(nombreindividus+1)
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
        self.__arbre_genealogic__.preorde()
    
    def consultar_genoma(self, ID):
        return self.__individus__[ID].get_cromosomes()
    
    def afegir_features(self, tret, nom, c_trets):
        c_trets.afegir_tret(tret,self.__individus__[nom])

    def subarbre(self,tret,c_trets):
        if c_trets.tret_in_dic(tret):
            set = c_trets.get_set(tret)
            print(set)
            subarbre = self.crear_subarbre(set)
            inordre = subarbre.inordre()
            print(inordre)
        else:
            print('error')

    def crear_subarbre(self, conjunto):
        def _subarbre(t):
            if t is None:
                return None
    
            if t.fulla():
                return ArbreBinari(t._element) if t._element in conjunto else ArbreBinari()
            else:
                left_tree = _subarbre(t._left)
                right_tree = _subarbre(t._right)
                if t._element in conjunto:
                    return ArbreBinari(t._element, left_tree, right_tree)
                else:
                    if left_tree.buit() and right_tree.buit():
                        return ArbreBinari()
                    else:
                        return ArbreBinari(-t._element, left_tree, right_tree)
    
        return _subarbre(self.__arbre_genealogic__._root)

    def afegir_individus(self,nom_individu,cromosomes):
        self.__individus__[nom_individu]=Individu(nom_individu,cromosomes)
    
        
        
    
    
