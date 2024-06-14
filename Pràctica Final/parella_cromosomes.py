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
        
    def interseccio(self, nou_cromosomes):  #intersecció_cromosomes serà donde se guarda las intersecciones anteriores.
        interseccio_cromosomes = self.get_cromosomes()
        if interseccio_cromosomes is None:
            self.__cromatide1__ = nou_cromosomes
        elif interseccio_cromosomes != '-'*len(nou_cromosomes):
            feature_tret=''
            for i in range(len(nou_cromosomes)):
                if nou_cromosomes[i] == interseccio_cromosomes[i]:
                    feature_tret += interseccio_cromosomes[i]
                else:
                    feature_tret += '-'
            self.__cromatide1__ = feature
