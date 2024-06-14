from conjunt_individus import C_individus
from parella_cromosomes import Cromosomes
class C_trets:
    def __init__(self):
        self.__dic_trets__ = {}
        self.__noms_trets__= set()
        

    #Metodes pricats
    def _present(self, tret, individu):
        return individu in self.__dic_trets__[tret][1]
    
    def tret_in_dic(self, tret):
        print(self.__noms_trets__)
        return tret in self.__noms_trets__

    def get_set(self, tret):
        return self.__dic_trets__[tret][1]
    
    def _get_info(self,tret):
        if tret in self.__noms_trets__:
            return self.__dic_trets__[tret]
        else:
            print ('error')
        
    #Metodes publics
    def afegir_tret (self, tret,individu):
        if tret in self.__noms_trets__ and not self._present(tret,individu):
            self.__dic_trets__[tret][1].add(individu)
            nou_cromosomes=individu.get_cromosomes()
            self.__dic_trets__[tret][0].interseccio(interseccio_cromosomes)
        else:
            self.__dic_trets__[tret] = (Cromosomes(None),set([individu]))
            self.__noms_trets__.add(tret)
            

    def consulta_tret(self, tret):
        if self.tret_in_dic(tret):
            print(tret)
            print(self.__dic_trets__[tret][0])
            individus=sorted(self.__dic_trets__[tret][1])
            for individu in individus:
                print(individu)
        else:
            print('error')
       
            
        

    




   
