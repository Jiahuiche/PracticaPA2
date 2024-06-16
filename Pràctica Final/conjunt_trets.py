from parella_cromosomes import Cromosomes

class C_trets:
    def __init__(self):
        self.__dic_trets__ = {}
        self.__noms_trets__= set()
        
    #Metodes pricats
    def _present(self, tret, individu):
        return individu in self.__dic_trets__[tret][1]
    
    def tret_in_dic(self, tret):
        return tret in self.__noms_trets__

    def get_set(self, tret):
        return {individu.get_ID() for individu in self.__dic_trets__[tret][1]} 
        
    #Metodes publics
    def afegir_tret (self, tret,individu):
        nou_cromosomes1, nou_cromosomes2=individu.get_cromosomes()
        individu.afegir_tret(tret)
        if tret in self.__noms_trets__ and not self._present(tret,individu):
            self.__dic_trets__[tret][1].add(individu)
            self.__dic_trets__[tret][0].interseccio(nou_cromosomes1, nou_cromosomes2)
        elif tret not in self.__noms_trets__:
            self.__dic_trets__[tret] = (Cromosomes(nou_cromosomes1+nou_cromosomes2),set([individu]))
            self.__noms_trets__.add(tret)
        else:
            print('  error')
            
    def consulta_tret(self, tret):
        if self.tret_in_dic(tret):
            print(' ',tret)
            self.__dic_trets__[tret][0].informar()
            set_individu = self.get_set(tret) 
            individus=sorted(set_individu)
            for individu in individus:
                print(' ',individu)
        else:
            print('  error')
       
        

    




   
