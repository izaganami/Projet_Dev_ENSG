import json
import re
import random
import uuid
import os
import sys
import time
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1,ROOT_DIR )
import Gen_Address
import Revenus
import Calc_Address


bourse_list0 = [1, 1]
sexe_list0 = [1, 1]

bourse_tracker0 = 100 * bourse_list0[0] / (bourse_list0[0] + bourse_list0[1])
sexe_tracker0 = 100 * sexe_list0[0] / (sexe_list0[0] + sexe_list0[1])
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


id_student = ""
coordinates_parents = []

Sexe = ""
Situation = ""

emploi = ""
type_emploi = ""
coordinates_travail = []

bourse = ""

'''
data = {}
data['type'] = []
data['type'].append({
    'name': 'FeatureCollection'
})
data['features'] = []
data['features'].append({
    "type": "Feature",
    "geometry": {"type": "Point",
                 "coordinates": coordinates_domicile},
    "properties": {"id": id,
                   "coordinates_ecole": coordinates_ecole,
                   "type_ecole": type_ecole,
                   "Nom_ecole": Nom_ecole,
                   "Discipline": Discipline,

                   "type_domicile": type_domicile,
                   "coordinates_domicile": coordinates_domicile,
                   "coordinates_parents": coordinates_parents,

                   "Sexe": Sexe,
                   "Situation": Situation,

                   "emploi": emploi,
                   "type_emploi": type_emploi,
                   "coordinates_travail": coordinates_travail,

                   "bourse": bourse,

                   }
})
'''
data_etablis = {}
data_etablis['type'] = []
data_etablis['type'].append({
    'name': 'FeatureCollection'
})
data_etablis['features'] = []

'''
with open(r'Data_proj/implantout.json',encoding='utf-8') as fp:
    try:
        for line in fp:
            id_etab = uuid.uuid4()
            coordinates_ecole = []
            type_ecole = ""
            Nom_ecole = ""
            Discipline = ""


            comment = json.loads(line)
            try:
                coordinates_ecole=comment['fields']['coordonnees']
            except(KeyError):
                print("Coordo indisp")
                coordinates_ecole = []
            try:
                Nom_ecole =comment['fields']['implantation_lib']
            except(KeyError):
                print("Nom indisp")
                Nom_ecole = ""
            try:
                Discipline = comment['fields']['services']
            except(KeyError):
                Discipline = ""
                print("Discipline indisp")
            try:
                type_ecole = comment['fields']['type_d_etablissement']
            except(KeyError):
                print("type indisp")
                type_ecole = ""
            data_etablis['features'].append({
                "type": "Feature",
                "geometry": {"type": "Point",
                             "coordinates": coordinates_ecole},
                "properties": {"id_etab": id_etab,
                               "type_ecole": type_ecole,
                               "Nom_ecole": Nom_ecole,
                               "Discipline": Discipline,

                               }
            })

    except(UnicodeDecodeError,KeyError):
        print("\nLoading 'effectif' Done\n")
        print(len(DataEtab))
with open('data_etablissement.txt', 'w') as outfile:
    json.dump(data_etablis, outfile,ensure_ascii=False)
'''
data_domic = {}
data_domic['type'] = []
data_domic['type'].append({
    'name': 'FeatureCollection'
})
data_domic['features'] = []

with open(r'Data_proj\residout.json', encoding='utf-8') as fp:
    for line in fp:
        id_domic = str(uuid.uuid4())
        type_domicile = ""
        coordinates_domicile = []
        capacity = 0
        try:
            resid = json.loads(line)
            print(resid)
            regex = r"\d+ (ch|Ch|t|T|st|St|lit|L|ST)"
            matches = re.finditer(regex, resid["fields"]["infos"], re.MULTILINE)
            tot = 0
            for a, b in enumerate(matches, start=1):
                tot += b.start()
                print("Places:{}".format(b.start()))
            if (tot == 0):
                tot = random.randint(80, 500)
                print("Randonly generated")
            print("Tot:{}".format(tot))
            try:
                type_domicile = resid["fields"]["title"]
            except(KeyError):
                type_domicile = ""
                print("Type domicile indisp")
            capacity = tot
            try:
                coordinates_domicile = resid["fields"]["geocalisation"]
            except(KeyError):
                coordinates_domicile = []
                print("Coordinate indisp")
            data_domic['features'].append({
                "type": "Feature",
                "geometry": {"type": "Point",
                             "coordinates": coordinates_domicile},
                "properties": {"id_domic": id_domic,
                               "type_domicile": type_domicile,
                               "capacity": capacity

                               }
            })

        except(KeyError):
            continue
    print("\nLoading 'resid' Done\n")

with open('data_domicile.geojson', 'w',encoding='utf-8') as outfile:
    json.dump(data_domic, outfile,ensure_ascii=False)


data_etud_gen = {}
data_etud = {}

data_etud['type'] = []
data_etud['type'].append({
    'name': 'FeatureCollection'
})
data_etud['features'] = []
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
                    coordinates_travail = T.Gen_Address_Within_Distane(coordinates_domicile[0],
                                           coordinates_domicile[1])
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
                    track = 0
                    for ligne in file:
                        try:
                            track += 1
                            etab = json.loads(ligne)

                            print(track)
                            ditance_dom_etab = 2
                            if (C.Calc_Distance(etab["fields"]["coordonnees"][0], etab["fields"]["coordonnees"][1],
                                                coordinates_domicile[0],
                                                coordinates_domicile[1]) < ditance_dom_etab and track < 2559):
                                coordinates_etab = [etab["fields"]["coordonnees"][0], etab["fields"]["coordonnees"][1]]
                                discipline = etab["fields"]["services"]
                                print(discipline)
                                break
                            elif (track >= 2559):
                                coordinates_etab = [etab["fields"]["coordonnees"][0], etab["fields"]["coordonnees"][1]]
                                discipline = "Classes Prepa"
                                print(discipline)
                                break
                            else:
                                ditance_dom_etab *= 2
                                continue

                        except KeyError:
                            continue

                data_etud['features'].append({
                    "type": "Feature",
                    "geometry": {"type": "Point",
                                 "coordinates": coordinates_domicile},
                    "properties": {"id_student": id_student,
                                   "type_domicile": line["properties"]["type_domicile"],
                                   "sexe": sexe,
                                   "bourse": bourse,
                                   "emploi": emploi,
                                   "coordinates_parents": coordinates_parents,
                                   "situation": situation,
                                   "type_emploi": type_emploi,
                                   "coordinates_travail": coordinates_travail,
                                   "revenu_fiscal":revenu_fisc[0],
                                   "lat":coordinates_domicile[0],
                                   "long":coordinates_domicile[1],
                                   "coordinates_etab":coordinates_etab,
                                   "discipline":discipline

                                   }
                })
                k+=1
                bourse_list0 = bourse_list
                sexe_list0 = sexe_list
                print(k)
                print(coordinates_parents)
                data_etud_gen=data_etud


        except(TypeError):
            print("Error")

with open(r'Data_proj\implantout.json', encoding='utf-8') as file:
    track = 0
    for ligne in file:
        if track < 370000:
            effectif=random.randint(300,5000)
            try:
                etab = json.loads(ligne)
                for i in range(effectif):
                    track+=1
                    d=create_student(etab["fields"]["coordonnees"], data_etud_gen, bourse_tracker0, sexe_tracker0, etab["fields"]["services"])
                    data_etud_gen["features"].append(d)


            except KeyError:
                continue
    print(track)

with open('data_stud.geojson', 'w', encoding='utf-8') as outfile:
    json.dump(data_etud, outfile, ensure_ascii=False)






'''''
##id
print uuid.uuid4()



##json fields
{
"type": "FeatureCollection",
"features": [
    {
    "type": "Feature",
    "geometry":{"type": "LineString", "coordinates": [[2.591884, 48.84116, 0, 1586150880.0], [2, 48.83927, 0, 1586152800.0], [2.000001, 48.839271, 0, 1586152800.0001]]},
    "properties": {"name": "allez"}},
        ]
}
'''



