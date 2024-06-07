from conjunt_individus import C_individus

class C_trets:
    def __init__(self):
        self.__dic_trets__ = {tret : (str, [])}

    def _present(self, tret, individu):
        return individu in self.__dic_trets__[tret][2]
        

    def afegir_tret (self, tret,individu):
        if not self._present(tret, individu):
            print('error')
        else:
            self._dic_trets_[tret][1].add(individu)
            self._dic_trets_[tret][0] = self._interseccio()

    def conjunt_individus_tret(self, ID):
        self._dic_trets[]
    def consulta_tret(self, tret):
        print(tret)
        print(self.__dic_trets__[tret][0])
        for i in range(len(self.__dic_trets__[tret][1]))
            print(self.__dic_trets__[tret][1][i])
            
        

    




   
