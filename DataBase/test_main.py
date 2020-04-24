import json
import re
import random
import uuid
import os
import sys
import time
import numpy

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, ROOT_DIR)
import Gen_Address
import Revenus
import Calc_Address

coordinates_etab = [42.9273967108, 3.7307720973]
bourse_list = [1, 1]
sexe_list = [1, 1]
data_etud = {}
data_etud['type'] = 'FeatureCollection'

data_etud['features'] = []
bourse_tracker = 100 * bourse_list[0] / (bourse_list[0] + bourse_list[1])
sexe_tracker = 100 * sexe_list[0] / (sexe_list[0] + sexe_list[1])
discipline = "test discipline"


def create_student(coordinates_etab, data_etud, bourse_tracker, sexe_tracker, discipline):
    rev_init = 20000
    rev_fin = 40000
    seuil = 300
    ecart_type = 5000
    emploi = random.choice(["oui", "non"])
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
    id_student = int(uuid.uuid4())
    T = Gen_Address.Gen_Address()
    coordinates_maison = T.Gen_Address_Within_Distane(coordinates_etab[0],
                                                      coordinates_etab[1])
    if emploi == "oui":
        coordinates_travail = T.Gen_Address_Within_Distane(coordinates_maison[0],
                                                           coordinates_maison[1])
        type_emploi = random.choice(
            ["Assistant(e) d'éducation", "Baby-sitter ", "Soutien scolaire ", "Serveur(se)",
             "Animateur/Animatrice des ventes", "distributeur de flyers",
             "Hôte ou hôtesse d'accueil",
             "Employé(e) du commerce ou de fast-food", "Livreur à vélo, coursier",
             "Enquêteur/Enquêtrice"])


    else:
        type_emploi = ""
        coordinates_travail = []
    T = Gen_Address.Gen_Address()
    coordinates_parents_var = T.Gen_Address_local()

    coordinates_parents = random.choice(
        [[coordinates_parents_var[1], coordinates_parents_var[0]], coordinates_maison])
    if (coordinates_parents == coordinates_maison):
        type_domicile = "prive"
    else:
        type_domicile = "parents"
    if random.randint(0, 100) < 7:
        situation = "Married"
    else:
        situation = "Single"
    R = Revenus.Revenus()
    C = Calc_Address.Calc_Address()
    dist = C.Calc_Distance(coordinates_parents[0], coordinates_parents[1], coordinates_maison[0],
                           coordinates_maison[1])
    rev_moyen = R.calcul_exp(rev_fin, rev_init, seuil, dist)
    revenu_fisc = R.estime_revenu(rev_moyen, ecart_type)

    data_etud['features'].append({
        "type": "Feature",
        "geometry": {"type": "Point",
                     "coordinates": coordinates_maison},
        "properties": {"id_student": id_student,
                       "type_domicile": type_domicile,
                       "sexe": sexe,
                       "bourse": bourse,
                       "emploi": emploi,
                       "coordinates_parents": coordinates_parents,
                       "situation": situation,
                       "type_emploi": type_emploi,
                       "coordinates_travail": coordinates_travail,
                       "revenu_fiscal": revenu_fisc[0],
                       "lat": coordinates_maison[0],
                       "long": coordinates_maison[1],
                       "coordinates_etab": coordinates_etab,
                       "discipline": discipline

                       }})
    return data_etud


d=create_student(coordinates_etab, data_etud, bourse_tracker, sexe_tracker, discipline)
print(d)

with open('data_stud_test.geojson', 'w+', encoding='utf-8') as outfile:
    print("out printing")
    json.dump(d, outfile, ensure_ascii=False)

d2=create_student(coordinates_etab, data_etud, bourse_tracker, sexe_tracker, discipline)
print(d2)

with open('data_stud_test.geojson', 'r', encoding='utf-8') as outfile:
    data=json.load(outfile)
    data["features"].append(d2)

with open('data_stud_test.geojson', 'w+', encoding='utf-8') as outfile:
    print("out printing")
    json.dump(data, outfile, ensure_ascii=False)


with open(r'Data_proj\implantout.json', encoding='utf-8') as file:
    track = 0
    for ligne in file:
        if track < 370000:
            effectif=random.randint(300,5000)
            try:
                etab = json.loads(ligne)
                for i in range(effectif):
                    track+=1
                    d=create_student(etab["fields"]["coordonnees"], data_etud, bourse_tracker, sexe_tracker, etab["fields"]["services"])
                    data_etud["features"].append(d)


            except KeyError:
                continue
