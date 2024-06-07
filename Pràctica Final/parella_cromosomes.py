class Cromosomes:
    def __init__(self, cromosomes):
        self.__cromatide1__ = cromosomes

    def get_cromosomes(self):
        #Getter que retorn cada cromatida com a string
        return self.__cromatide1__

    def informar(self):
        #Imprimeix cada comatide per sdtout
        a = self.get_cromosomes()
        print('  ', a[:len(a)//2])
        print('  ',a[len(a)//2:])
