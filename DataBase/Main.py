"""
PARTIE 1 DE LA CRÉATION DES DONNÉES
(partie 2 : Create-flow)

Ce fichier sert à créer un fichier geojson contenant tous nos étudiants et leurs informations :
- id_student
- type_domicile : nom de la résidence
- sexe : ""
- bourse : "oui" / "non"
- emploi : "oui" / "non"
- coordinates_parents : [lat, lng]
- situation : "Married", "Single"
- type_emploi :
- coordinates_travail : [lat, lng]
- revenu_fiscal : revenu fiscal du foyer familial en euros
- lat : latitude du domicile étudiant
- long : longitude du domicile étudiant
- coordinates_etab : [lat, lng]
- discipline : discipline étudiée par l'étudiant
- residence : "oui" / "non"
- region_domicile : région où se trouve le domicile étudiant (France + outre-mer)
- region_parent : région où se trouve le domicile parental (France + outre-mer)

Une fois qu'on a ce fichier, on peut lancer "Create_flow" afin de créer les fichiers de données utiles .

"""




#### MODULES ####
import json, geojson
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
import France
from math import ceil
import codecs
from shapely.geometry import shape, Point









####### CRÉATION D'UNE FEATURE COLLECTION A INSÉRER DANS NOTRE FICHIER GEOJSON #######

data_etud_gen = {}
data_etud = {}

data_etud['type'] = []
data_etud['type'].append({
    'name': 'FeatureCollection'
})
data_etud['features'] = []



####### CRÉATION D'UNE LISTE DES ÉTABLISSEMENTS #######

liste_coord_etab=[]
with open(r'Data_proj/implantout.json', encoding='utf-8') as file:

    for ligne in file:
        try:
            data = json.loads(ligne)
            lat = data["fields"]["coordonnees"][0]
            long = data["fields"]["coordonnees"][1]
            filiere = data["fields"]["services"]

            liste_coord_etab.append([lat,long,filiere])
        except:
            continue


####### CRÉATION D'UN POLYGONE DE LA FRANCE + OUTRE MER #######

with open('france.geojson') as f:
    data = geojson.load(f)
polygon_france = shape(data['geometry'])



####### CRÉATION DE 5 LIEUX D'ÉTUDE POUR CHAQUE LIEUX D'ÉTUDE ########
liste_lieux_travail =[]

with open(r'Data_proj/implantout.json', encoding='utf-8') as file:
    print("Chargement des lieux de travail...")
    i=0
    for ligne in file:
        i += 1
        print(i)
        for k in range(1):
            coordinates_test =""
            try:
                data = json.loads(ligne)
                lat = data["fields"]["coordonnees"][0]
                long = data["fields"]["coordonnees"][1]
                coordinates_lieu_travail =[]
                test_adresse_France= False
                test=0
                while (test_adresse_France == False):
                    test+=1
                    T = Gen_Address.Gen_Address()
                    coordinates_lieu_travail = T.Gen_Address_Within_Distane(lat, long)
                    if (polygon_france.contains(Point(coordinates_lieu_travail[1], coordinates_lieu_travail[0]))):
                        test_adresse_France=True
                    if (test>6):
                        coordinates_test="invalides"
                        break
                if(coordinates_test=="invalides"):
                    continue
                else:
                    type_emploi = random.choice(["Serveur(se)",
                                                 "Hôte ou hôtesse d'accueil",
                                                 "Employé(e) du commerce ou de fast-food"])
                    liste_lieux_travail.append([coordinates_lieu_travail[0],coordinates_lieu_travail[1],type_emploi])

            except:
                continue








#########################################   CRÉATION DES ÉTUDIANTS   #########################################

with open(r'data_domicile.geojson', encoding='utf-8') as fp:
    print("Génération des étudiants...")
    residence_etudiante = True
    C = Calc_Address.Calc_Address()
    k=0
    bourse_list = [1, 1] ## oui , non
    sexe_list = [1,1] ##femme , homme
    comment = json.loads(fp.read())
    i = 0
    #Pour chaque étudiant (164 000 + 36 000 en résidence universitaire)
    for j in range (164000):
        print(j)

        #initialisation de variables
        id_student = int(uuid.uuid4())
        sexe = ""
        bourse = ""
        emploi = ""
        coordinates_parents = []
        coordinates_domicile =[]
        situation = ""
        type_emploi = ""
        coordinates_travail = []

        #Attribution d'une bourse (38% des étudiants)
        bourse_tracker = 100 * bourse_list[0] / (bourse_list[0] + bourse_list[1])
        sexe_tracker = 100 * sexe_list[0] / (sexe_list[0] + sexe_list[1])
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

        #Détermination du sexe (54% de filles)
        if sexe_tracker <= 54:
            sexe = random.choice(["femme", "homme"])
            if sexe == "femme":
                sexe_list[0] += 1
            else:
                sexe_list[1] += 1
        else:
            sexe = "homme"
            sexe_list[1] += 1

        #Si on est à la première itération, on crée les étudiants en résidence, sinon les autres
        if (j == 0):
            for line in comment["features"]:
                try:
                    #On ne récupère qu'un dixième de la capacité des étudiants en résidence pour passer de 2 millions à
                    # 200 000 étudiants (de 360 000 à 36 000 en résidence)

                    #Pour chaque résidence
                    #counter = int(int(line["properties"]["capacity"])/10)
                    counter=0

                    while counter > 0:

                        i += 1
                        print(i)

                        # initialisation de variables
                        id_student = int(uuid.uuid4())
                        sexe = ""
                        bourse = ""
                        emploi = ""
                        coordinates_parents = []
                        coordinates_domicile = line["geometry"]["coordinates"]
                        situation = ""
                        type_emploi = ""
                        coordinates_travail = []

                        # Attribution d'une bourse (38% des étudiants)
                        bourse_tracker = 100 * bourse_list[0] / (bourse_list[0] + bourse_list[1])
                        sexe_tracker = 100 * sexe_list[0] / (sexe_list[0] + sexe_list[1])
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

                        # Détermination du sexe (54% de filles)
                        if sexe_tracker <= 54:
                            sexe = random.choice(["femme", "homme"])
                            if sexe == "femme":
                                sexe_list[0] += 1
                            else:
                                sexe_list[1] += 1
                        else:
                            sexe = "homme"
                            sexe_list[1] += 1

                        counter -= 1

                        #permet de vérifier si notre point est en France
                        test_adresse_France = False

                        #permet de savoir si le domicile parental est situé dans une grande ville ou non
                        random_parent_etudiant = random.randrange(1, 100, 1)

                        #le domicile parental est situé dans une grande ville
                        if (random_parent_etudiant<52):

                                #on choisit au hasard un établissement dans la liste des établissements
                                random_etab =random.randrange(0,len(liste_coord_etab)-1,1)
                                lat = liste_coord_etab[random_etab][0]
                                long = liste_coord_etab[random_etab][1]
                                test = 0
                                #tant que l'adresse n'est pas en France, on recommence
                                while (test_adresse_France == False):
                                    test += 1

                                    #On génère une adresse dans un rayon de distance
                                    T = Gen_Address.Gen_Address()
                                    coordinates_parents = T.Gen_Address_Within_Distane(lat, long)

                                    #si le point de l'adresse se trouve dans le polygone de la France, le test France
                                    #est validé
                                    if (polygon_france.contains(Point(coordinates_parents[1], coordinates_parents[0]))):
                                        test_adresse_France = True

                                    #si on ne trouve rien, on sort
                                    if (test > 100):
                                        break


                        #sinon l'étudiant possède une adresse aléatoire en France
                        else:

                            test = 0
                            #tant que l'adresse n'est pas en France, on recommence
                            while (test_adresse_France == False):
                                test += 1

                                #On génère une adresse aléatoire en France
                                T = Gen_Address.Gen_Address()
                                coordinates_parents = T.Gen_Address_local()

                                # si le point de l'adresse se trouve dans le polygone de la France, le test France
                                # est validé
                                if (polygon_france.contains(Point(coordinates_parents[1], coordinates_parents[0]))):
                                    test_adresse_France = True

                                if (test > 100):
                                    break


                        #1 étudiant sur 2 possède un emploi
                        emploi = random.choice(["oui", "non"])

                        if emploi == "oui":

                            #permet de déterminer où travaillent les étudiants
                            random_travail = random.randrange(6)

                            #1 étudiant sur 6 travaille dans un lieu de travail seul
                            if (random_travail == 0):
                                type_emploi = random.choice(
                                    ["Assistant(e) d'éducation", "Baby-sitter ", "Soutien scolaire ", "Serveur(se)",
                                     "Animateur/Animatrice des ventes", "distributeur de flyers",
                                     "Hôte ou hôtesse d'accueil",
                                     "Employé(e) du commerce ou de fast-food", "Livreur à vélo, coursier",
                                     "Enquêteur/Enquêtrice"])
                                test_adresse_France = False
                                test = 0

                                #tant que l'adresse n'est pas en France, on recommence
                                while (test_adresse_France == False):
                                    test += 1

                                    #On génère une adresse aléatoire dans toute la France
                                    T = Gen_Address.Gen_Address()

                                    coordinates_travail = T.Gen_Address_Within_Distane(coordinates_domicile[0],
                                                                                       coordinates_domicile[1])

                                    if (polygon_france.contains(
                                            Point(coordinates_parents[1], coordinates_parents[0])) == True):
                                        test_adresse_France = True

                                    if (test > 20):
                                        coordinates_travail = []
                                        emploi = "non"
                                        break

                            # 5 étudiants sur 6 qui ont un emploi travaillent sur un lieu de travail collectif
                            else:

                                #ce lieu de travail doit se trouver à 4km du domicile étudiant
                                dist_min = 4
                                dist = 1000
                                test = 0

                                #on cherche dans la liste des lieux de travail un lieu qui est à moins de 4km de notre
                                #domicile étudiant
                                while (dist_min < dist):
                                    test += 1
                                    travail_possible = random.choice(liste_lieux_travail)
                                    dist = C.Calc_Distance(travail_possible[0], travail_possible[1],
                                                           coordinates_domicile[0],
                                                           coordinates_domicile[1])
                                    coordinates_travail = [travail_possible[0], travail_possible[1]]

                                    #si on ne trouve aucun lieu, on s'arrête, l'étudiant ne travaille pas
                                    if (test > 1000):
                                        coordinates_travail = []
                                        emploi = "non"
                                        break

                        #l'étudiant ne travaille pas
                        else:
                            coordinates_travail = []


                        # On calcule le revenu fiscal de la famille de l'étudiant

                        # Revenu fiscal moyen lorsque l'étudiant  étudie à côté de chez ses parents
                        rev_init = 23000

                        # Revenu fiscal moyen lorsque la distance tend vers l'infini
                        rev_fin = 40000

                        # Paramètre qui fait converger plus ou moins vite la fonction exponentielle
                        seuil = 300

                        # Ecart type de la loi normale qui générera le revenu du foyer considéré
                        ecart_type = 4000

                        C = Calc_Address.Calc_Address()

                        # Calcul de la distance entre le lieu d'étude et le domicile parental
                        dist = C.Calc_Distance(coordinates_parents[0], coordinates_parents[1], coordinates_domicile[0],
                                               coordinates_domicile[1])

                        # Importation de la classe Revenus
                        R = Revenus.Revenus()

                        # Calcul du revenu moyen en fonction de la distance entre le lieu d'étude et le domicile parental
                        rev_moyen = R.calcul_exp(rev_fin, rev_init, seuil, dist)

                        # Distinction du cas boursier du cas non boursier
                        if (bourse=="oui"):
                            revenu_fisc = R.estime_revenu()
                        else:
                            revenu_fisc = R.estime_revenu(rev_moyen, ecart_type)

                        lat=0
                        long=0
                        coordinates_etab=[0,0]
                        discipline=""


                        #L'étudiant est-il marrié ou célibataire (7% des étudiants sont marriés)
                        if random.randint(0, 100) < 7:
                            situation = "Married"
                        else:
                            situation = "Single"

                        #On attribue un lieu d'étude et sa filière à l'étudiant en fonction de son lieu d'étude
                        with open(r'Data_proj/implantout.json', encoding='utf-8') as file:

                            dist_min = 1000
                            for ligne in file:
                                etab = json.loads(ligne)
                                try:
                                    if (C.Calc_Distance(etab["fields"]["coordonnees"][0], etab["fields"]["coordonnees"][1],
                                                        coordinates_domicile[0],
                                                        coordinates_domicile[1]) <dist_min):
                                        dist_min = C.Calc_Distance(etab["fields"]["coordonnees"][0],
                                                                   etab["fields"]["coordonnees"][1],
                                                                   coordinates_domicile[0],
                                                                   coordinates_domicile[1])
                                        coordinates_etab = [etab["fields"]["coordonnees"][0], etab["fields"]["coordonnees"][1]]
                                        discipline = etab["fields"]["services"]



                                    else :
                                        continue

                                except KeyError:
                                    continue

                        #On cherche la région du domicile étudiant et la région du domicile parental
                        region_domicile = France.find_region(coordinates_domicile[0], coordinates_domicile[1])
                        region_parent = France.find_region(coordinates_parents[0], coordinates_parents[1])

                        #On ajoute notre étudiant à nos données
                        try:
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
                                           "revenu_fiscal":revenu_fisc,
                                           "lat":coordinates_domicile[0],
                                           "long":coordinates_domicile[1],
                                           "coordinates_etab":coordinates_etab,
                                           "discipline":discipline,
                                           "residence": "oui",
                                           "region_domicile": region_domicile,
                                           "region_parent": region_parent

                                           }
                            })
                        except:
                            continue

                        k+=1
                        bourse_list0 = bourse_list
                        sexe_list0 = sexe_list
                        data_etud_gen = data_etud


                except(TypeError):
                    print("Error")

        #L'étudiant ne vit pas en résidence étudiante
        else:
            #initialisation des variables
            coordinates_test = ""
            test_adresse_France = False
            random_parent_etudiant = 0
            vit_chez_parents = False
            parent_ville_etudiant_loin = False

            #permet de savoir si un étudiant vit chez ses parents
            random_vit_chez_parent = random.randrange(1, 164, 1)

            #69% des étudiants vivent chez leurs parents
            if (random_vit_chez_parent > 42):
                vit_chez_parents = True

            else:
                #permet de savoir si les parents de l'étudiant habitent en ville
                random_parent_etudiant = random.randrange(1, 100, 1)
                test=0
                test_adresse_France = False
                while(test_adresse_France == False):
                    test+=1
                    random_etab = random.randrange(0, len(liste_coord_etab)-1, 1)
                    lat = liste_coord_etab[random_etab][0]
                    long = liste_coord_etab[random_etab][1]
                    T = Gen_Address.Gen_Address()
                    coordinates_domicile = T.Gen_Address_Within_Distane(lat, long)
                    if (polygon_france.contains(Point(coordinates_domicile[1], coordinates_domicile[0]))):
                            test_adresse_France = True
                    if (test>20):
                        break
                        coordinates_test="invalides"
                test_adresse_France = False
                #80% des étudiants vivent en ville (les étudiants qui restent vivre chez leurs parents vivent aussi en
                # ville)
                if (random_parent_etudiant < 51):
                    parent_ville_etudiant_loin= True

            #si l'étudiant vit chez ses parents
            if (vit_chez_parents == True):
                random_etab = random.randrange(0, len(liste_coord_etab)-1, 1)
                lat = liste_coord_etab[random_etab][0]
                long = liste_coord_etab[random_etab][1]
                test=0
                test_adresse_France = False
                #on vérifie que l'adresse est en France, à proximité d'un lieu d'étude
                while (test_adresse_France == False):
                    test+=1
                    T = Gen_Address.Gen_Address()

                    coordinates_parents = T.Gen_Address_Within_Distane(lat, long)
                    if (polygon_france.contains(Point(coordinates_parents[1], coordinates_parents[0]))):
                            test_adresse_France = True

                    if (test>20):
                        coordinates_test="invalides"
                        break

                coordinates_domicile = coordinates_parents

            #si l'étudiant ne vit pas chez ses parents et que ses parents vivent en ville
            elif (parent_ville_etudiant_loin == True):

                random_etab = random.randrange(0, len(liste_coord_etab)-1, 1)
                lat = liste_coord_etab[random_etab][0]
                long = liste_coord_etab[random_etab][1]
                test_adresse_France = False
                test=0

                #on vérifie que l'adresse est en France, à proximité d'un lieu d'étude
                while (test_adresse_France == False):
                    test+=1

                    T = Gen_Address.Gen_Address()
                    coordinates_parents = T.Gen_Address_Within_Distane(lat, long)

                    if (polygon_france.contains(Point(coordinates_parents[1], coordinates_parents[0]))==True):
                            test_adresse_France = True
                    if (test>20):
                        coordinates_test = "invalides"
                        break


            #si l'étudiant ne vit pas chez ses parents et que l'adresse n'est pas en ville
            else:
                test_adresse_France = False
                test = 0
                #on vérifie que l'adresse est en France, dans un lieu au hasard
                while (test_adresse_France == False):
                    test+=1

                    T = Gen_Address.Gen_Address()
                    coordinates_parents = T.Gen_Address_local()

                    if (polygon_france.contains(Point(coordinates_parents[1], coordinates_parents[0]))):
                            test_adresse_France = True
                    if (test>20):
                        coordinates_test = "invalides"
                        break

            ##### on attribue un emploi #####
            emploi = random.choice(["oui", "non"])
            if emploi == "oui":

                random_travail = random.randrange(6)
                if (random_travail == 0):
                    type_emploi = random.choice(
                        ["Assistant(e) d'éducation", "Baby-sitter ", "Soutien scolaire ", "Serveur(se)",
                         "Animateur/Animatrice des ventes", "distributeur de flyers", "Hôte ou hôtesse d'accueil",
                         "Employé(e) du commerce ou de fast-food", "Livreur à vélo, coursier", "Enquêteur/Enquêtrice"])
                    test_adresse_France = False
                    test = 0
                    while (test_adresse_France == False):
                        test += 1

                        T = Gen_Address.Gen_Address()

                        coordinates_travail = T.Gen_Address_Within_Distane(coordinates_domicile[0],
                                                                               coordinates_domicile[1])

                        if (polygon_france.contains(Point(coordinates_parents[1], coordinates_parents[0])) == True):
                            test_adresse_France = True

                        if (test > 20):
                            coordinates_travail = []
                            emploi = "non"
                            break


                else:
                    dist_min=4
                    dist =1000
                    test=0
                    while(dist_min<dist):
                        test+=1

                        travail_possible = random.choice(liste_lieux_travail)
                        dist = C.Calc_Distance(travail_possible[0], travail_possible[1], coordinates_domicile[0],
                                        coordinates_domicile[1])
                        coordinates_travail = [travail_possible[0], travail_possible[1]]
                        if (test>1000):
                            coordinates_travail = []
                            emploi = "non"
                            break



            else:
                coordinates_travail = []


            #### revenu fiscal ####
            rev_init = 23000
            rev_fin = 40000
            seuil = 300
            ecart_type = 4000

            dist = C.Calc_Distance(coordinates_parents[0], coordinates_parents[1], coordinates_domicile[0],
                                   coordinates_domicile[1])

            R = Revenus.Revenus()
            rev_moyen = R.calcul_exp(rev_fin, rev_init, seuil, dist)
            if (bourse == "oui"):
                revenu_fisc = R.estime_revenu()
            else:
                revenu_fisc = R.estime_revenu(rev_moyen, ecart_type)



            lat = 0
            long = 0
            coordinates_etab = []
            discipline = ""


            #### on attribue une situation familial à l'étudiant ####
            if random.randint(0, 100) < 7:
                situation = "Married"
            else:
                situation = "Single"


            #### on attribue un établissement ####
            dist_min = 5
            dist=1000
            test=0
            pas_trouver_etab = False

            #tant qu'on a pas trouver d'établissement à moins de 5km
            while (dist_min < dist):
                    test+=1

                    # on cherche dans la liste des établissements un établissement aléatoirement
                    travail_possible = random.choice(liste_coord_etab)

                    dist = C.Calc_Distance(travail_possible[0], travail_possible[1],
                                           coordinates_domicile[0],
                                           coordinates_domicile[1])
                    coordinates_etab = [travail_possible[0], travail_possible[1]]
                    try:
                        discipline = travail_possible[2]
                    except:
                        continue

                    #si on ne trouve aucun établissement
                    if (test > 1400):
                        pas_trouver_etab = True
                        break
                        dist_min=1000

            #l'étudiant se rend dans l'établissement le plus proche de chez lui
            if(pas_trouver_etab == True):
                with open(r'Data_proj/implantout.json', encoding='utf-8') as file:
                    for ligne in file:
                        etab = json.loads(ligne)
                        try:
                            if (C.Calc_Distance(etab["fields"]["coordonnees"][0], etab["fields"]["coordonnees"][1],
                                                        coordinates_domicile[0],
                                                        coordinates_domicile[1]) < dist_min):

                                dist_min = C.Calc_Distance(etab["fields"]["coordonnees"][0],
                                                                   etab["fields"]["coordonnees"][1],
                                                                   coordinates_domicile[0],
                                                                   coordinates_domicile[1])
                                coordinates_etab = [etab["fields"]["coordonnees"][0],
                                                            etab["fields"]["coordonnees"][1]]
                                discipline = etab["fields"]["services"]




                            else:
                                continue

                        except KeyError:
                            continue

            if (coordinates_test == "invalides"):
                continue

            #### on cherche les régions du domicile étudiant et domicile parental
            region_parent=""
            region_domicile = France.find_region(coordinates_domicile[0], coordinates_domicile[1])
            #si l'étudiant vit chez ses parents, on ne s'embête pas à chercher (moins de temps de calcul)
            if (vit_chez_parents == True):
                region_parent = region_domicile
            else:
                region_parent = France.find_region(coordinates_parents[0], coordinates_parents[1])

            # On ajoute notre étudiant à nos données
            try:
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
                               "revenu_fiscal": revenu_fisc,
                               "lat": coordinates_domicile[0],
                               "long": coordinates_domicile[1],
                               "coordinates_etab": coordinates_etab,
                               "discipline": discipline,
                               "residence" : "non",
                               "region_domicile": region_domicile,
                               "region_parent": region_parent
                               }
                    })

            except:
                continue

        k += 1
        bourse_list0 = bourse_list
        sexe_list0 = sexe_list
        data_etud_gen = data_etud



####### CRÉATION DU FICHIER GEOJSON DE NOS ÉTUDIANTS #######

with open('Data_Created/data_stud_200k.geojson', 'w', encoding='utf-8') as outfile:
    #on insère tous nos étudiants dans le fichier
    json.dump(data_etud, outfile, ensure_ascii=False)
