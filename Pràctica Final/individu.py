from parella_cromosomes import Cromosomes

class Individu:
    def __init__(self, ID, cromosomes):
        self.__ID__ = ID
        self.__cromosomes__ = Cromosomes(cromosomes)
        self.__trets__ = set()
    #getters
    def get_cromosomes (self):
        self.__cromosomes__.get_cromosomes()
    #------------------------------
    def informar(self):
        self.__cromosomes__.informar()
        trets = sorted(self.__trets__)
        for tret in trets:
            print(tret)
    def afegir_tret(self, tret):
        self.__trets__.append(tret)

    def interseccio(self, intersecció_cromosomes = None):  #intersecció_cromosomes serà donde se guarda las intersecciones anteriores.
        cromosomes_propi = self.__cromosomes__.get_cromosomes
        feature_tret = ''
        if intersecció_cromosomes == None:
            return cromosomes_propi
        elif intersecció_cromosomes == '-'*len(cromosomes_propi):
            return intersecció_cromosomes
        else:
            for i in range(len(cromosomes)):
                if cromosoma1[i] == interseció_cromosomes[i]:
                    feature_tret += cromosoma1[i]
                else:
                    feature_tret += '-'
            return feature_tret
        
