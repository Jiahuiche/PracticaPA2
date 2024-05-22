from conjunt_individus import C_individus

class C_trets:
    def __init__(self):
        self.__dic_trets__ = {tret:(Parella_Cromosomes(), C_individus())}

    def _present(tret):
        for t in self.__dic_trets__ :
            if t == tret:
                return True
        return False

    def afegir_tret (tret,individu):
        if self._present(tret):
            print('error')
        else:
            self._dic_trets_[tret] = individu.consulta_genoma()
            self._dic_trets_[tret] = (self.interseccio(), self.get_conjunt_individus())

    #def get_conjunt_individus()

    




   
