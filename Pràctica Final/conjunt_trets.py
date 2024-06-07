from conjunt_individus import C_individus

class C_trets:
    def __init__(self):
        self.__dic_trets__ = {}
        self.__noms_trets__={}
        

    def _present(self, tret, individu):
        return individu in self.__dic_trets__[tret][1]
        

    def afegir_tret (self, tret,individu):
        if tret in self.__noms_trets__ and not self._present(tret,individu):
            self._dic_trets_[tret][1].add(individu)
            interseccio_cromosomes=self._dic_trets_[tret][0]
            self._dic_trets_[tret][0] = self._interseccio(interseccio_cromosomes)
        else:
            self._dic_trets_[tret] = (individu.interseccio(),{individu})
            self.__noms_trets__.add(tret)
            

    def consulta_tret(self, tret):
        print(tret)
        print(self.__dic_trets__[tret][0])
        individus=sorted(self._dic_trets_[tret][1])
        for individu in individus:
            print(individus.get_nom())
            
        

    




   
