from conjunt_individus import C_individus

class C_trets:
    def __init__(self):
        self.__dic_trets__ = {}

    def afegir_tret (tret,individu):
        self._dic_trets_[tret] = individu.consulta_genoma()
        self._dic_trets_[tret] = (self.interseccio(), self.get_conjunt_individus())

    def get_conjunt_individus()

    def interseccio(cromosoma1,cromosoma2 = None):
        feature_tret = ['-']*len(cromosoma1)
        if cromosoma2 == None:
            feature_tret = cromosoma1
        for i in range(len(cromosoma1)):
            if cromosoma1[i] == cromosoma2[i]:
                feature_tret[i] = cromosoma1[i]
            else:
                feature_tret[i] = '-'
        return feature_tret
    




   