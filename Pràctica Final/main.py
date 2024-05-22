from pytokr import pytokr

item,items = pytokr (iter=True)
instruccio = item()
while instruccio != 'fi':
    if instruccio == 'experiment':
        n = int(item()) #nombre participants de l'experiment
        m = int(item()) #mida cromosomes
        print(instruccio,n,m)
        experiment = Experiment()
        """n_participants=0
        lst_participants=[]
        while n_participants < n:
            participant=int(item())
            if participant != 0:
                n_participant+=1
            lst.append(participant)
        experiment.__crear_arbol(lst) """
        cromosoma = item()
        while len(cromosoma) = 2*m:
            nom_individu = item()
            experiment.__assignar_cromosomes(nom_individu,cromosoma)
            comosoma=item()
        
    elif instruccio == 'afegir_tret':
        nom_tret = item()
        nom_individu = item()
        print(instruccio,nom_tret,nom_individu)
        experiment.afegir_tret(nom_tret, nom_individu)
        
    elif instruccio == 'consulta_tret':
        nom_tret = item()
        print(instruccio,nom_tret)
        experiment.consulta_tret(nom_tret)
    elif instruccio == 'consulta_individu':
        nom_individu = item()
        experiment.consulta_individu(nom_individu)
    elif instruccio == 'distribucio_tret':
        nom_tret = item()
        experiment.distribucio_tret(nom_tret)
    instruccio = item()
