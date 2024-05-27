class Cromosomes:
    def __init__(self):
        self.__cromatide1__ = None
    def get_cromosomes(self):
        #Getter que retorn cada cromatida com a string
        return self.__cromatide1__
    def crear(self, str):
        #Assigna cada cromatide amb l'estructura de dades del input 
        self.__cromatide1__ = str
    def informar(self):
        #Imprimeix cada comatide per sdtout
        a = self.get_output()
        print(a)
