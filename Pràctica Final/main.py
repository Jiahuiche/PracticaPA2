from pytokr import pytokr
from class_experiment import Experiment

item,items = pytokr(iter=True)
instruccio = item()
while instruccio != 'fi':
    if instruccio == 'experiment':
        n = int(item()) #nombre participants de l'experiment
        m = int(item()) #mida cromosomes
        print(instruccio,n,m)
        experiment = Experiment(n)
        experiment._crear_arbol()
        ID = 1
        while ID <= n:
            cromosoma=item()
            experiment._afegir_individu(ID,cromosoma)
            ID += 1
        
        
        
    elif instruccio == 'afegir_tret':
        nom_tret = item()
        nom_individu = int(item())
        print(instruccio,nom_tret,nom_individu)
        experiment.afegir_tret(nom_tret, nom_individu)
        
    elif instruccio == 'consulta_tret':
        nom_tret = item()
        print(instruccio,nom_tret)
        experiment.consulta_tret(nom_tret)

    elif instruccio == 'consulta_individu':
        nom_individu = int(item())
        print(instruccio,nom_individu)
        experiment.consulta_individu(nom_individu)
        

    elif instruccio == 'distribucio_tret':
        nom_tret = item()
        print(instruccio, nom_tret)
        experiment.distribucio_tret(nom_tret)

    instruccio = item()
