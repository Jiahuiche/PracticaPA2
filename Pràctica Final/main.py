from pytokr import pytokr

item,items = pytokr (iter=True)
instruccio = item()
while instruccio != 'fi':
    if instruccio == 'experiment':
        n = int(item()) #nombre participants de l'experiment
        m = int(item()) #mida cromosomes
        print(instruccio,n,m)
        experiment = Experiment()
        while experiment.mida_arbre() != n:
            nom_individu = item()
            experiment.afegir_individu(nom_individu)
        while 'arbre no ple':
            familia.llegeix_arbrebinari_int(0)
        for i in range(n):
            str = item()
            experiment.afegir_cromosomes(i,str)
        
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
        experiment.consulta_individu(nom_individu)
    elif instruccio == 'distribucio_tret':
        nom_tret = item()
        experiment.distribucio_tret(nom_tret)
    instruccio = item()
