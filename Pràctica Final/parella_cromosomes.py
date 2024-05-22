class Cromosomes:
    def __init__(self):
        self.__cromatide1__ = None
    def get_output(self):
        #Getter que retorn cada cromatida com a string
        return self.__cromatide1__
    def crear(self, str):
        #Assigna cada cromatide amb l'estructura de dades del input
        l=len(str)
        self.__cromatide1__ = str[:l]
        self.__cromatide2__ = str[-l:]
    def informar(self):
        #Imprimeix cada comatide per sdtout
        a,b = self.get_output()
        print(a)
        print(b)
