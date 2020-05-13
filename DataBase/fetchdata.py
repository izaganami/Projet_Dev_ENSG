import json
import re
import random
import uuid
import os
import sys
import time

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1,ROOT_DIR )
import Gen_Address
import Revenus
import Calc_Address
import json

T=Gen_Address.Gen_Address()
coordinates_parents_var = T.Gen_Address_local()
coordinates_parents = [coordinates_parents_var[1], coordinates_parents_var[0]]
print(coordinates_parents)

print("emploi")
coordinates_emploi = T.Gen_Address_Within_Distane(coordinates_parents_var[0],coordinates_parents_var[1])
print(coordinates_emploi)

rev_init = 20000
rev_fin = 40000
seuil = 300
ecart_type = 5000

C=Calc_Address.Calc_Address()
dist= C.Calc_Distance(coordinates_parents_var[0], coordinates_parents_var[1], coordinates_emploi[0], coordinates_emploi[1])
print(dist)



R=Revenus.Revenus()
rev_moyen = R.calcul_exp(rev_fin, rev_init, seuil, dist)
revenu_fisc = R.estime_revenu(rev_moyen, ecart_type)
print(revenu_fisc[0])

with open(r'data_domicile.geojson', encoding='utf-8') as fp:
    k=0
    bourse_list = [1, 1]## oui , non
    sexe_list = [1,1]##femme , homme
    comment = json.loads(fp.read())

    for line in comment["features"]:
        try:
            bourse_tracker = 100 * bourse_list[0] / (bourse_list[0] + bourse_list[1])
            sexe_tracker = 100 * sexe_list[0] / (sexe_list[0] + sexe_list[1])

            counter = int(line["properties"]["capacity"])
            coordinates_domicile=line["geometry"]["coordinates"]
##distance max logement - universite
            while counter > 0:
                counter -= 1
                id_student = int(uuid.uuid4())
                sexe = ""
                bourse = ""
                emploi = ""
                coordinates_parents = []

                situation = ""

                type_emploi = ""
                coordinates_travail = []

                if bourse_tracker <= 38:
                    bourse = random.choice(["oui", "non"])
                    ## ajout de quantile (1er = bourse)
                    if bourse == "oui":
                        bourse_list[0] += 1
                    else:
                        bourse_list[1] += 1
                else:
                    bourse = "non"
                    bourse_list[1] += 1

                if sexe_tracker <= 54:
                    sexe = random.choice(["femme", "homme"])
                    if sexe == "femme":
                        sexe_list[0] += 1
                    else:
                        sexe_list[1] += 1
                else:
                    sexe = "homme"
                    sexe_list[1] += 1
                T = Gen_Address.Gen_Address()
                coordinates_parents_var = T.Gen_Address_local()

                coordinates_parents = [coordinates_parents_var[1], coordinates_parents_var[0]]
                emploi = random.choice(["oui", "non"])
                if emploi == "oui":
                    coordinates_travail = T.Gen_Address_Within_Distane(coordinates_parents_var[0],coordinates_parents_var[1])
                    type_emploi = random.choice(["Assistant(e) d'éducation", "Baby-sitter ","Soutien scolaire ","Serveur(se)","Animateur/Animatrice des ventes","distributeur de flyers","Hôte ou hôtesse d'accueil",
                                                 "Employé(e) du commerce ou de fast-food","Livreur à vélo, coursier","Enquêteur/Enquêtrice"])


                else:
                    coordinates_travail = []



                rev_init = 20000
                rev_fin = 40000
                seuil = 300
                ecart_type = 5000

                C = Calc_Address.Calc_Address()
                dist = C.Calc_Distance(coordinates_parents[0], coordinates_parents[1], coordinates_domicile[0],
                                       coordinates_domicile[1])
                print(dist)

                R = Revenus.Revenus()
                rev_moyen = R.calcul_exp(rev_fin, rev_init, seuil, dist)
                revenu_fisc = R.estime_revenu(rev_moyen, ecart_type)
                lat=0
                long=0
                coordinates_etab=[]
                discipline=""



                if random.randint(0, 100) < 7:
                    situation = "Married"
                else:
                    situation = "Single"
                with open(r'Data_proj\implantout.json', encoding='utf-8') as file:
                    track=0
                    for ligne in file:
                        try:
                            track+=1
                            etab = json.loads(ligne)

                            print(track)
                            if (C.Calc_Distance(etab["fields"]["coordonnees"][0], etab["fields"]["coordonnees"][1],
                                                coordinates_domicile[0], coordinates_domicile[1]) < 3000 and track <2559):
                                coordinates_etab=[etab["fields"]["coordonnees"][0],etab["fields"]["coordonnees"][1]]
                                discipline=etab["fields"]["services"]
                                print(discipline)
                                break
                            elif(track >= 2559):
                                coordinates_etab = [etab["fields"]["coordonnees"][0], etab["fields"]["coordonnees"][1]]
                                discipline="Classes Prepa !!!!!!!!!!!!!!!!!!!"
                                print(discipline)
                                break
                            else:
                                continue

                        except KeyError:
                            continue


                k+=1





        except(TypeError):
            print("Error")
