from math import sin, cos, sqrt, atan2, radians
from random import randrange
import math as m
import datetime
import geojson
import numpy as np
import random
import csv

############ TEMPS DE TRAJET ###########

def Calc_Temps_Trajet(lat1, long1, lat2, long2):
    """

    :param lat1: latitude du lieu 1
    :param long1: longitude du lieu 1
    :param lat2: latitude du lieu 2
    :param long2: longitude du lieu 2
    :return: temps de trajet entre 2 positions
    """
    distance = Calc_Distance(lat1, long1, lat2, long2)
    random = randrange(5)*0.1+0.8
    if (distance <= 2 ):
        temps_trajet = (distance / 2.9) * random
    elif (distance >2 and distance <= 5):
        temps_trajet = (distance / 7) * random
    elif (distance>5 and distance <=18):
        temps_trajet = (distance / 20) * random
    elif (distance > 18 and distance <= 35):
        temps_trajet = (distance / 35) * random
    elif (distance > 35 and distance <= 300):
        temps_trajet = (distance / 65) * random
    elif (distance > 300 and distance <= 500):
        temps_trajet = (distance / 100) * random
    elif (distance > 500):
        temps_trajet = (distance / 130) * random

    return temps_trajet


def Calc_Distance(lat1, long1, lat2, long2):
    """

    :param lat1: latitude du lieu 1
    :param long1: longitude du lieu 1
    :param lat2: latitude du lieu 2
    :param long2: longitude du lieu 2
    :return: distance entre 2 positions
    """

    # approximate radius of earth in km
    R = 6373.0

    lat1 = radians(lat1)
    long1 = radians(long1)
    lat2 = radians(lat2)
    long2 = radians(long2)

    dlon = long2 - long1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    return distance


def horaires_cours(lat_domicile, long_domicile, lat_etude, long_etude):
    """

    :param lat_domicile: latitude du domicile de l'étudiant
    :param long_domicile: longitude du domicile de l'étudiant
    :param lat_etude: latitude du lieu d'étude
    :param long_etude: longitude du lieu d'étude
    :return: horaires auquel l'étudiant quitte son domicile,
    auquel il débute les cours,
    auquel il finit les cours,
    et auquel il est rentré chez lui
    """
    random_debut = randrange(99)
    if (random_debut < 20):
        heure_debut_cours = 8
        random_duree = random.uniform(5,12)

    elif (random_debut >= 20 and random_debut < 39):
        heure_debut_cours = 8.5
        random_duree = random.uniform(5,11.5)

    elif (random_debut >= 39 and random_debut < 63):
        heure_debut_cours = 9
        random_duree = random.uniform(5,11)

    elif (random_debut >= 63 and random_debut < 78):
        heure_debut_cours = 9.5
        random_duree = random.uniform(5,10.5)

    elif (random_debut >= 78 and random_debut < 86):
        heure_debut_cours = 10
        random_duree = random.uniform(5,10)

    elif (random_debut >= 86 and random_debut < 93):
        heure_debut_cours = 10.5
        random_duree = random.uniform(5,9.5)

    elif (random_debut >= 93 and random_debut < 96):
        heure_debut_cours = 11
        random_duree = random.uniform(5,9)

    elif (random_debut >= 96 and random_debut < 98):
        heure_debut_cours = 11.5
        random_duree = random.uniform(5,8.5)

    elif (random_debut >= 98 and random_debut < 99):
        heure_debut_cours = 12
        random_duree = random.uniform(5,8)

    elif (random_debut >= 99 ):
        heure_debut_cours = 12.5
        random_duree = random.uniform(5,7.5)

    int
    a = int(random_duree);
    dif = random_duree - float(a);
    if (dif < 0.25):
        random_duree = a;
    elif ( dif < 0.75 ):
        random_duree = float(a) + 0.5;

    else:
        random_duree = a + 1;

    heure_fin_cours = random_duree+heure_debut_cours




    temps_trajet = Calc_Temps_Trajet(lat_domicile, long_domicile, lat_etude, long_etude)


    heure_depart_domicile = heure_debut_cours - temps_trajet
    heure_arrivee_domicile = heure_fin_cours + temps_trajet


    return heure_depart_domicile, heure_debut_cours, heure_fin_cours, heure_arrivee_domicile




def travail_soir(heure_arrivee_minimale_travail,temps_domicile_travail):
    """

    :param heure_arrivee_minimale_travail: heure d'arrivée la plus tôt à laquelle l'étudiant peut arriver à son travail
    :param temps_domicile_travail: temps de trajet entre le domicile de l'étudiant et son lieu de travail
    :return: heure à laquelle l'étudiant part travailler,
    à laquelle il arrive au travail,
    à laquelle il finit son travail,
    à laquelle il est de retour chez lui
    """

    plage_horaire = 24 - heure_arrivee_minimale_travail
    random_plage = randrange(int(plage_horaire)-2)
    random_debut = randrange(m.ceil(heure_arrivee_minimale_travail),21,1)
    nombre_heures = randrange(21 - random_debut)
    nombre_heures+=2

    heure_debut_travail = random_debut
    heure_fin_travail = heure_debut_travail+nombre_heures
    heure_depart_domicile = heure_debut_travail-temps_domicile_travail
    heure_arrivee_domicile = heure_fin_travail+temps_domicile_travail

    return heure_depart_domicile, heure_debut_travail, heure_fin_travail, heure_arrivee_domicile





def travail_weekend(temps_domicile_travail):
    """

    :param temps_domicile_travail: temps de trajet entre le domicile de l'étudiant et son lieu de travail
    :return:heure à laquelle l'étudiant part travailler,
    à laquelle il arrive au travail,
    à laquelle il finit son travail,
    à laquelle il est de retour chez lui
    """

    nombre_heures = randrange(6) +2
    heure_debut_travail = randrange(15-nombre_heures)+8
    heure_fin_travail = heure_debut_travail+nombre_heures
    heure_depart_domicile = heure_debut_travail - temps_domicile_travail
    heure_arrivee_domicile = heure_fin_travail + temps_domicile_travail

    return heure_depart_domicile, heure_debut_travail, heure_fin_travail, heure_arrivee_domicile




def horaires_travail(heure_arrivee_domicile, lat_domicile, long_domicile, lat_travail, long_travail,visite_parent):

    random = randrange(2)
    temps_domicile_travail = Calc_Temps_Trajet(lat_domicile, long_domicile, lat_travail,long_travail)
    heure_arrivee_minimale_travail = heure_arrivee_domicile + temps_domicile_travail

    if (visite_parent == True and heure_arrivee_minimale_travail >= 20):
        return None,None,None,None

    if (random == 0):
        if (heure_arrivee_minimale_travail < 20)  :
            return travail_soir(heure_arrivee_minimale_travail,temps_domicile_travail)
        else:
            return travail_weekend(temps_domicile_travail)
    else:
        if (visite_parent == False ):
            return travail_weekend(temps_domicile_travail)
        else:
            return travail_soir(heure_arrivee_minimale_travail,temps_domicile_travail)



def horaires_parent(lat_domicile, long_domicile, lat_parent, long_parent):
    
    temps_trajet = Calc_Temps_Trajet(lat_domicile, long_domicile, lat_parent, long_parent)
    heure_depart_domicile = random.uniform(7,11)
    heure_arrivee_domicile = random.uniform(17.5, 23.5)
    heure_arrivee_parent = heure_depart_domicile + temps_trajet
    heure_depart_parent = heure_arrivee_domicile - temps_trajet

    return heure_depart_domicile,heure_arrivee_parent,heure_depart_parent,heure_arrivee_domicile



def creer_donnees_arc(nom_fichier_arc, travail, lat_domicile, long_domicile, lat_etude, long_etude, lat_parent, long_parent, lat_travail, long_travail,visite_parent):

    with open(nom_fichier_arc, 'a', newline='') as csvfile:

        fieldnames = ['depart_lat', 'depart_lng','arrivee_lat','arrivee_lng','type']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writerow({'depart_lat': lat_domicile, 'depart_lng' : long_domicile, 'arrivee_lat': lat_etude,'arrivee_lng' : long_etude,'type':'etude'})

        if (lat_parent is not None and visite_parent ==True):
            writer.writerow({'depart_lat': lat_domicile, 'depart_lng' : long_domicile, 'arrivee_lat': lat_parent,'arrivee_lng' : long_parent,'type':'parent'})

        if(travail is not None):
            writer.writerow({'depart_lat': lat_domicile, 'depart_lng' : long_domicile, 'arrivee_lat': lat_travail,'arrivee_lng' : long_travail, 'type':'travail'})







def creer_donnees_trip(lat_1, long_1, lat_2, long_2, heure_1_depart, heure_1_arrivee, heure_2_depart, heure_2_arrivee, sexe, filiere, boursier, revenu_fiscal, situation):
    """

    :param lat_1: latitude du domicile étudiant
    :param long_1: longitude du domicile étudiant
    :param lat_2: latitude du domicile familial
    :param long_2: longitude du domicile familial
    :param heure_1_depart: heure départ du domicile
    :param heure_1_arrivee: heure arrivée parent
    :param heure_2_depart: heure départ des parents
    :param heure_2_arrivee: heure retour au domicile
    :return: trip du domicile au parent
    """

    timestamp_heure_1_depart = datetime.datetime.strptime("04/11/20 "+str(int(heure_1_depart))+":"+str(int(heure_1_depart % 1 * 60)),'%m/%d/%y %H:%M')
    timestamp_heure_1_arrivee = datetime.datetime.strptime("04/11/20 "+str(int(heure_1_arrivee))+":"+str(int(heure_1_arrivee % 1 * 60)),'%m/%d/%y %H:%M')
    timestamp_heure_2_depart = datetime.datetime.strptime("04/12/20 "+str(int(heure_2_depart))+":"+str(int(heure_2_depart % 1 * 60)),'%m/%d/%y %H:%M')
    timestamp_heure_2_arrivee = datetime.datetime.strptime("04/12/20 "+str(int(heure_2_arrivee))+":"+str(int(heure_2_arrivee % 1 * 60)),'%m/%d/%y %H:%M')


    allez_parent = geojson.LineString([[long_1, lat_1, 0,datetime.datetime.timestamp(timestamp_heure_1_depart)+7200],
                           [long_2, lat_2, 0,datetime.datetime.timestamp(timestamp_heure_1_arrivee)+7200 ],
                                [long_2+0.000001, lat_2+0.000001, 0, datetime.datetime.timestamp(timestamp_heure_1_arrivee)+7200.0001]])

    retour_parent = geojson.LineString([[long_2, lat_2, 0,datetime.datetime.timestamp(timestamp_heure_2_depart)+7200],
                           [long_1, lat_1, 0,datetime.datetime.timestamp(timestamp_heure_2_arrivee)+7200 ],
                                 [long_1+0.000001, lat_1+0.000001, 0, datetime.datetime.timestamp(timestamp_heure_2_arrivee)+7200.0001]])



















    ################# ICI TU PEUX AJOUTER DES PROPERTIES #######################
    # IL FAUT LES PASSER EN ATTRIBUTS DE CETTE FONCTION ET DE LA FONCTION EMPLOI DU TEMPS



    properties1 = {'name': "allez",'type_trip' : "parent_domicile",'sexe' : sexe, 'filiere': filiere,'boursier' : boursier,'revenu_fiscal': revenu_fiscal,'situation': situation}
    allez_feature = geojson.Feature(geometry=allez_parent, properties=properties1)
    properties2 = {'name': "retour",'type_trip' : "domicile_parent",'sexe' : sexe, 'filiere': filiere,'boursier' : boursier,'revenu_fiscal': revenu_fiscal,'situation': situation}
    retour_feature = geojson.Feature(geometry=retour_parent, properties=properties2)

    return allez_feature, retour_feature









def Emploi_Temps (nom_fichier_arc, lat_domicile, long_domicile, lat_etude, long_etude, lat_parent, long_parent, lat_travail, long_travail,sexe, filiere, boursier, revenu_fiscal, situation):
    """

    :param nom_fichier_arc: nom du fichier avec les arcs
    :param lat_domicile: latitude du domicile de l'étudiant
    :param long_domicile: longitude du domicile de l'étudiant
    :param lat_etude: latitude du lieu d'étude
    :param long_etude: longitude du lieu d'étude
    :param lat_parent: latitude du domicile parental
    :param long_parent: longitude du domicile parental
    :param lat_travail: latitude du lieu de travail
    :param long_travail: longitude du lieu de travail
    :return:
    """

    heure_depart_domicile_cours, heure_debut_cours, heure_fin_cours, heure_arrivee_domicile_cours = horaires_cours(
        lat_domicile, long_domicile, lat_etude, long_etude)
    random_parent = randrange(10)
    if (random_parent<=6 and lat_parent is not None and lat_parent != lat_domicile and Calc_Distance(lat_domicile, long_domicile, lat_parent, long_parent)<650):
        heure_depart_domicile_parent, heure_arrivee_parent,  heure_depart_parent,heure_arrivee_domicile_parent = horaires_parent(
            lat_domicile, long_domicile, lat_parent, long_parent)
        visite_parent = True
        allez_feature, retour_feature = creer_donnees_trip(lat_domicile, long_domicile, lat_parent, long_parent,heure_depart_domicile_parent, heure_arrivee_parent, heure_depart_parent,heure_arrivee_domicile_parent,sexe, filiere, boursier, revenu_fiscal, situation)
        features.append(allez_feature)
        features.append(retour_feature)


    else :
        visite_parent = False

    if (lat_travail is not None):
        heure_depart_domicile_travail, heure_debut_travail, heure_fin_travail, heure_arrivee_domicile_travail = horaires_travail(
            heure_arrivee_domicile_cours, lat_domicile, long_domicile, lat_travail, long_travail, visite_parent)
        if (heure_depart_domicile_travail is None):
            travail = False
        else :
            travail = True

    else:
        travail = False


    creer_donnees_arc(nom_fichier_arc, travail, lat_domicile, long_domicile, lat_etude, long_etude, lat_parent, long_parent, lat_travail, long_travail,visite_parent)





if __name__ == "__main__":
    with open("data_stud.geojson") as f:
        data = geojson.load(f)
    features = data['features'][0]["properties"]
    print(features)



    ############## PARAMETRES A MODIFIER ################

    nom_fichier_arc = 'test_arc_5.csv'

    nom_fichier_trip = 'test_trip_5.geojson'

    nombre_etudiants = 3000

####################################################

    features =[]

    with open(nom_fichier_arc, 'w', newline='') as csvfile:
        fieldnames = ['depart_lat', 'depart_lng', 'arrivee_lat', 'arrivee_lng','type',]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
    for feature in data['features']:

############## DÉFINIR CES VALEURS ################
########## METTRE None SI PAS DE VALEUR ###########


        if (feature['properties']['emploi'] == "oui"):
            lat_travail = feature['properties']['coordinates_travail'][0]
            long_travail = feature['properties']['coordinates_travail'][1]
        else :
            lat_travail = None
            long_travail = None
        lat_domicile = feature['geometry']['coordinates'][0]
        lat_parent = feature['properties']['coordinates_parents'][0]
        lat_etude = feature['properties']['coordinates_etab'][0]
        long_etude = feature['properties']['coordinates_etab'][1]
        long_domicile = feature['geometry']['coordinates'][1]
        long_parent = feature['properties']['coordinates_parents'][1]

        sexe = feature['properties']['sexe']
        boursier = feature['properties']['bourse']
        situation = feature['properties']['situation']
        filiere = feature['properties']['discipline']
        revenu_fiscal = feature['properties']['revenu_fiscal']

##################################################

        Emploi_Temps(nom_fichier_arc, lat_domicile, long_domicile, lat_etude, long_etude, lat_parent, long_parent, lat_travail,
                     long_travail,sexe, filiere, boursier, revenu_fiscal, situation)
    
    feature_collection = geojson.FeatureCollection(features)
    with open(nom_fichier_trip, 'w') as f:
        geojson.dump(feature_collection, f)




