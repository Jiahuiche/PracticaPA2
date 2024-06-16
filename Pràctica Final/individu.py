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
            print(' ',tret)
            
    def afegir_tret(self, tret):
        self.__trets__.add(tret)
