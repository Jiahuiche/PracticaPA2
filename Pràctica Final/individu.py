from parella_cromosomes import Cromosomes

class Individu:
    def __init__(self, ID,cromosomes):
        self.__ID__ = ID
        self.__cromosomes__ = Cromosomes(cromosomes)
        self.__trets__ = set()
    
    #getters
    def get_cromosomes (self):
        return self.__cromosomes__.get_cromosomes()

    def get_ID(self):
        return self.__ID__
        
    #------------------------------
    def informar(self):
        self.__cromosomes__.informar()
        trets = sorted(self.__trets__)
        for tret in trets:
            print(tret)
            
    def afegir_tret(self, tret):
        self.__trets__.add(tret)

    def interseccio(self, interseccio_cromosomes = None):  #intersecció_cromosomes serà donde se guarda las intersecciones anteriores.
        cromosomes_propi = self.__cromosomes__.get_cromosomes()
        comosomes_comparatiu=inteseccio_cromosomes.get_cromosomes()
        if interseccio_cromosomes == None:
            return Cromosomes(cromosomes_propi)
        elif interseccio_cromosomes == '-'*len(cromosomes_propi):
            return interseccio_cromosomes
        else:
            for i in range(len(cromosomes_comparatiu)):
                if cromosomes_propi[i] == cromosoma_comparatiu[i]:
                    feature_tret += cromosomes_propi[i]
                else:
                    feature_tret += '-'
            return Cromosomes(feature_tret)
        
