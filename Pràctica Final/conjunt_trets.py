from conjunt_individus import C_individus

class C_trets:
    def __init__(self):
        self.__dic_trets__ = {tret : (str, [])}

    def _present(self, tret, ID):
        for t in self.__dic_trets__:
            if t == tret:
                for i in self.__dic_trets__[t]:
                    if self.__dic_trets__[t][1][i] == ID:
                        return True
            return Fale
        

    def afegir_tret (self, tret,individu):
        if self._present(tret, individu):
            print('error')
        else:
            self._dic_trets_[tret] = individu.consulta_genoma()
            self._dic_trets_[tret] = (self.interseccio(), [])

    def conjunt_individus_tret(self, ID):
        
        

    def consulta_tret(self, tret):
        print(tret)
        print(self.__dic_trets__[tret][0])
        for i in range(len(self.__dic_trets__[tret][1]))
            print(self.__dic_trets__[tret][1][i])
            
        

    




   
