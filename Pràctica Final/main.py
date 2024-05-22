from pytokr import pytokr
from parella_comosomes import Cromosomes
from individu import Individu
from conjunt_trets import C_trets
from conjunt_individus import C_individus

item,items = pytokr (iter=True)
trets = C_trets()
instruccio = item()
while instruccio != 'fi':
    if instruccio == 'experiment':
        n = int(item()) #nombre participants de l'experiment
        m = int(item()) #mida cromosomes
        print(instruccio,n,m)
        familia = C_individus(n) #A C_individus ja es crearà les instàncies d'Individu
        #parella_cromosomes = Cromosomes(m)
        experiment = Experiment()
        while experiment.mida_arbre() != n:
            nom_individu = item()
            experiment.afegir_individu(nom_individu)
        while 'arbre no ple':
            familia.llegeix_arbrebinari_int(0)
        for _ in range(n):
            cromo = int(item())
            parella_cromosomes.crear()
            for _ in range(m):
                parella_cromosomes.afegir_cromo(cromo)
                cromo = int(item())  #En dos fors porque pytokr solo lee de uno en uno
        
    elif instruccio == 'afegir_tret':
        nom_tret = item()
        nom_individu = item()
        print(instruccio,nom_tret,nom_individu)
        trets.afegir_tret(nom_tret, nom_individu)
        #Afegir tret a Individus también.
        experiment.afegir_tret(nom_tret, nom_individu)
        
    elif instruccio == 'consulta_tret':
        nom_tret = item()
        print(instruccio,nom_tret)
        C_trets.consulta_tret(nom_tret)
        experiment.consulta_tret(nom_tret)
    elif instruccio == 'consulta_individu':
        nom_individu = item()
        print(instruccio,nom_individu)
        familia.consulta_individu(nom_individu)
        experiment.consulta_individu(nom_individu)
    elif instruccio == 'distribucio_tret':
        nom_tret = item()
        print(instruccio,nom_tret)
        familia.distribucio_tret(nom_tret)
        experiment.distribucio_tret(nom_tret)
    instruccio = item()
