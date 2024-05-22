from parella_cromosomes import Cromosomes

class Individu:
    def __init__(self,):
        self.__cromosomes__ = [Cromosomes()]
        self.__trets__ = set()
    def construir_cromosomes (self, lst):
        self.__cromosomes__.creacio(lst)
    def informar(self):
        self.__cromosomes__.informar()
        trets = sorted(self.__trets__)
        for tret in trets:
            print(tret)
    def afegir_tret(self, tret):
        self.__trets__.append(tret)

    def interseccio(self, cromosoma2 = None):
        feature_tret = ['-']*len(cromosoma1)
        if cromosoma2 == None:
            feature_tret = cromosoma1
        for i in range(len(cromosoma1)):
            if cromosoma1[i] == cromosoma2[i]:
                feature_tret[i] = cromosoma1[i]
            else:
                feature_tret[i] = '-'
        return feature_tret
        
