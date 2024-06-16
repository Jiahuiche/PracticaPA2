class Cromosomes:
    def __init__(self, cromosomes):
        self.__cromatide1__ = cromosomes[:len(cromosomes)//2]
        self.__cromatide2__ = cromosomes[len(cromosomes)//2:]

    def get_cromosomes(self):
        #Getter que retorn cada cromatida com a string
        return self.__cromatide1__, self.__cromatide2__

    def informar(self):
        #Imprimeix cada comatide per sdtout
        a,b = self.get_cromosomes()
        print(' ',a)
        print(' ',b)

    def interseccio(self, nou_cromosomes1, nou_cromosomes2):  #intersecció_cromosomes serà donde se guarda las intersecciones anteriores.
        interseccio_cromosomes1, interseccio_cromosomes2 = self.get_cromosomes()
        if interseccio_cromosomes1 or interseccio_cromosomes2 != '-'*len(nou_cromosomes1):
            feature_tret1=''
            feature_tret2=''
            for i in range(len(nou_cromosomes1)):
                if nou_cromosomes1[i] == interseccio_cromosomes1[i] and nou_cromosomes2[i] == interseccio_cromosomes2[i]:
                    feature_tret1 += interseccio_cromosomes1[i]
                    feature_tret2 += interseccio_cromosomes2[i]
                else:
                    feature_tret1 += '-'
                    feature_tret2 += '-'
            self.__cromatide1__ = feature_tret1
            self.__cromatide2__ = feature_tret2
