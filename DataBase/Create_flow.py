from math import sin, cos, sqrt, atan2, radians
from random import randrange
import math as m
import datetime
import geojson
import numpy as np
import random
import csv
import France
from shapely.geometry import shape, Point

###brui sur les horaires###
def gen_random_noise(decimal):
    return round(random.uniform(-10, 10), decimal)

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
        return None,None,None,None,None

    if (random == 0):
        if (heure_arrivee_minimale_travail < 20)  :
            heure_depart_domicile_travail, heure_debut_travail, heure_fin_travail, heure_arrivee_domicile_travail = travail_soir(heure_arrivee_minimale_travail,temps_domicile_travail)
            travail_semaine_weekend = "soir"
            return heure_depart_domicile_travail, heure_debut_travail, heure_fin_travail, heure_arrivee_domicile_travail, travail_semaine_weekend


        else:
            heure_depart_domicile_travail, heure_debut_travail, heure_fin_travail, heure_arrivee_domicile_travail = travail_weekend(
                temps_domicile_travail)
            travail_semaine_weekend = "week-end"
            return heure_depart_domicile_travail, heure_debut_travail, heure_fin_travail, heure_arrivee_domicile_travail, travail_semaine_weekend

    else:
        if (visite_parent == False ):
            heure_depart_domicile_travail, heure_debut_travail, heure_fin_travail, heure_arrivee_domicile_travail =travail_weekend(temps_domicile_travail)
            travail_semaine_weekend = "week-end"
            return heure_depart_domicile_travail, heure_debut_travail, heure_fin_travail, heure_arrivee_domicile_travail, travail_semaine_weekend
        else:
            heure_depart_domicile_travail, heure_debut_travail, heure_fin_travail, heure_arrivee_domicile_travail = travail_soir(heure_arrivee_minimale_travail,temps_domicile_travail)
            travail_semaine_weekend = "soir"
            return heure_depart_domicile_travail, heure_debut_travail, heure_fin_travail, heure_arrivee_domicile_travail, travail_semaine_weekend



def horaires_parent(lat_domicile, long_domicile, lat_parent, long_parent):
    """

    :param lat_domicile: latitude du domicile de l'étudiant
    :param long_domicile: longitude du domicile de l'étudiant
    :param lat_parent: latitude du domicile des parents
    :param long_parent: longitude du domicile des parents
    :return: heure de départ du domicile de l'étudiant pour se rendre chez ses parents,
    heure d'arrivée chez ses parents,
    heure de départ du domicile parental pour rentrer à son domicile étudiant
    heure d'arrivée à son domicile étudiant
    """
    
    temps_trajet = Calc_Temps_Trajet(lat_domicile, long_domicile, lat_parent, long_parent)
    heure_depart_domicile = random.uniform(7,11)
    heure_arrivee_domicile = random.uniform(17.5, 23.5)
    heure_arrivee_parent = heure_depart_domicile + temps_trajet
    heure_depart_parent = heure_arrivee_domicile - temps_trajet

    return heure_depart_domicile,heure_arrivee_parent,heure_depart_parent,heure_arrivee_domicile



def creer_donnees_arc(nom_fichier_arc, lat_domicile, long_domicile, lat_etude, long_etude, lat_parent,
                          long_parent, lat_travail, long_travail, visite_parent, sexe, filiere, boursier, revenu_fiscal,
                          situation, region_domicile, region_parent):
    """
    créer un fichier csv dans lequel se trouve les arcs entre les différents lieux
    :param nom_fichier_arc: nom du fichier dans lequel seront stockés les arcs
    :param lat_domicile: latitude du domicile de l'étudiant
    :param long_domicile: longitude du domicile de l'étudiant
    :param lat_etude: latitude du lieu d'étude
    :param long_etude: longitude du lieu d'étude
    :param lat_parent: latitude du domicile des parents
    :param long_parent: longitude du domicile des parents
    :param lat_travail: latitude du lieu de travail de l'étudiant
    :param long_travail: longitude du lieu de travail de l'étudiant
    :param visite_parent: boolean, True si il rentre chez ses parents le week-end, False sinon
    :param sexe: sexe de l'étudiant
    :param filiere: filière de l'étudiant
    :param boursier: oui ou non
    :param revenu_fiscal: revenu fiscal du foyer parental de l'étudiant
    :param situation: marrié ou célibataire
    :param region_domicile: région où vit l'étudiant
    :param region_parent: région où vivent les parents de l'étudiant
    :return:
    """

    with open(nom_fichier_arc, 'a', newline='') as csvfile:

        fieldnames = ['depart_lat', 'depart_lng', 'arrivee_lat', 'arrivee_lng', 'type', 'sexe', 'filiere', 'boursier',
                      'revenu_fiscal', 'situation', 'region_domicile', 'region_parent']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writerow({'depart_lat': lat_domicile, 'depart_lng': long_domicile, 'arrivee_lat': lat_etude,
                         'arrivee_lng': long_etude, 'type': 'etude',
                         'sexe': sexe, 'filiere': filiere, 'boursier': boursier, 'revenu_fiscal': revenu_fiscal,
                         'situation': situation, 'region_domicile': region_domicile, 'region_parent': region_parent})

        if (lat_parent is not None and visite_parent == True):
            writer.writerow({'depart_lat': lat_domicile, 'depart_lng': long_domicile, 'arrivee_lat': lat_parent,
                             'arrivee_lng': long_parent, 'type': 'parent', 'sexe': sexe, 'filiere': filiere,
                             'boursier': boursier, 'revenu_fiscal': revenu_fiscal, 'situation': situation,
                             'region_domicile': region_domicile, 'region_parent': region_parent})

        if (lat_travail is not None):
            writer.writerow({'depart_lat': lat_domicile, 'depart_lng': long_domicile, 'arrivee_lat': lat_travail,
                             'arrivee_lng': long_travail, 'type': 'travail', 'sexe': sexe, 'filiere': filiere,
                             'boursier': boursier, 'revenu_fiscal': revenu_fiscal, 'situation': situation,
                             'region_domicile': region_domicile, 'region_parent': region_parent})


def creer_donnees_trip(lat_domicile, long_domicile, lat_parent, long_parent, lat_etude, long_etude, lat_travail,
                           long_travail,
                           heure_domicile_etude_depart,
                           heure_domicile_etude_arrivee, heure_etude_domicile_depart, heure_etude_domicile_arrivee,
                           heure_domicile_parent_depart, heure_domicile_parent_arrivee, heure_parent_domicile_depart,
                           heure_parent_domicile_arrivee, heure_depart_domicile_travail, heure_debut_travail,
                           heure_fin_travail, heure_arrivee_domicile_travail, travail_semaine_weekend,
                           sexe, filiere, boursier, revenu_fiscal, situation,
                           region_domicile, region_parent):

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


    ###### FORMATAGE DES HEURES AU FORMAT TIMESTAMP ######

    timestamp_heure_domicile_etude_depart_lundi = datetime.datetime.strptime(
        "04/06/20 " + str(int(heure_domicile_etude_depart)) + ":" + str(int(heure_domicile_etude_depart % 1 * 60)),
        '%m/%d/%y %H:%M')

    timestamp_heure_domicile_etude_arrivee_lundi = datetime.datetime.strptime(
        "04/06/20 " + str(int(heure_domicile_etude_arrivee)) + ":" + str(int(heure_domicile_etude_arrivee % 1 * 60)),
        '%m/%d/%y %H:%M')
    timestamp_heure_etude_domicile_depart_lundi = datetime.datetime.strptime(
        "04/06/20 " + str(int(heure_etude_domicile_depart)) + ":" + str(int(heure_etude_domicile_depart % 1 * 60)),
        '%m/%d/%y %H:%M')
    timestamp_heure_etude_domicile_arrivee_lundi = datetime.datetime.strptime(
        "04/06/20 " + str(int(heure_etude_domicile_arrivee)) + ":" + str(int(heure_etude_domicile_arrivee % 1 * 60)),
        '%m/%d/%y %H:%M')

    timestamp_heure_domicile_etude_depart_mardi = datetime.datetime.strptime(
        "04/07/20 " + str(int(heure_domicile_etude_depart)) + ":" + str(int(heure_domicile_etude_depart % 1 * 60)),
        '%m/%d/%y %H:%M')
    timestamp_heure_domicile_etude_arrivee_mardi = datetime.datetime.strptime(
        "04/07/20 " + str(int(heure_domicile_etude_arrivee)) + ":" + str(int(heure_domicile_etude_arrivee % 1 * 60)),
        '%m/%d/%y %H:%M')
    timestamp_heure_etude_domicile_depart_mardi = datetime.datetime.strptime(
        "04/07/20 " + str(int(heure_etude_domicile_depart)) + ":" + str(int(heure_etude_domicile_depart % 1 * 60)),
        '%m/%d/%y %H:%M')
    timestamp_heure_etude_domicile_arrivee_mardi = datetime.datetime.strptime(
        "04/07/20 " + str(int(heure_etude_domicile_arrivee)) + ":" + str(int(heure_etude_domicile_arrivee % 1 * 60)),
        '%m/%d/%y %H:%M')

    timestamp_heure_domicile_etude_depart_mercredi = datetime.datetime.strptime(
        "04/08/20 " + str(int(heure_domicile_etude_depart)) + ":" + str(int(heure_domicile_etude_depart % 1 * 60)),
        '%m/%d/%y %H:%M')
    timestamp_heure_domicile_etude_arrivee_mercredi = datetime.datetime.strptime(
        "04/08/20 " + str(int(heure_domicile_etude_arrivee)) + ":" + str(int(heure_domicile_etude_arrivee % 1 * 60)),
        '%m/%d/%y %H:%M')
    timestamp_heure_etude_domicile_depart_mercredi = datetime.datetime.strptime(
        "04/08/20 " + str(int(heure_etude_domicile_depart)) + ":" + str(int(heure_etude_domicile_depart % 1 * 60)),
        '%m/%d/%y %H:%M')
    timestamp_heure_etude_domicile_arrivee_mercredi = datetime.datetime.strptime(
        "04/08/20 " + str(int(heure_etude_domicile_arrivee)) + ":" + str(int(heure_etude_domicile_arrivee % 1 * 60)),
        '%m/%d/%y %H:%M')

    timestamp_heure_domicile_etude_depart_jeudi = datetime.datetime.strptime(
        "04/09/20 " + str(int(heure_domicile_etude_depart)) + ":" + str(int(heure_domicile_etude_depart % 1 * 60)),
        '%m/%d/%y %H:%M')
    timestamp_heure_domicile_etude_arrivee_jeudi = datetime.datetime.strptime(
        "04/09/20 " + str(int(heure_domicile_etude_arrivee)) + ":" + str(int(heure_domicile_etude_arrivee % 1 * 60)),
        '%m/%d/%y %H:%M')
    timestamp_heure_etude_domicile_depart_jeudi = datetime.datetime.strptime(
        "04/09/20 " + str(int(heure_etude_domicile_depart)) + ":" + str(int(heure_etude_domicile_depart % 1 * 60)),
        '%m/%d/%y %H:%M')
    timestamp_heure_etude_domicile_arrivee_jeudi = datetime.datetime.strptime(
        "04/09/20 " + str(int(heure_etude_domicile_arrivee)) + ":" + str(int(heure_etude_domicile_arrivee % 1 * 60)),
        '%m/%d/%y %H:%M')

    timestamp_heure_domicile_etude_depart_vendredi = datetime.datetime.strptime(
        "04/10/20 " + str(int(heure_domicile_etude_depart)) + ":" + str(int(heure_domicile_etude_depart % 1 * 60)),
        '%m/%d/%y %H:%M')
    timestamp_heure_domicile_etude_arrivee_vendredi = datetime.datetime.strptime(
        "04/10/20 " + str(int(heure_domicile_etude_arrivee)) + ":" + str(int(heure_domicile_etude_arrivee % 1 * 60)),
        '%m/%d/%y %H:%M')
    timestamp_heure_etude_domicile_depart_vendredi = datetime.datetime.strptime(
        "04/10/20 " + str(int(heure_etude_domicile_depart)) + ":" + str(int(heure_etude_domicile_depart % 1 * 60)),
        '%m/%d/%y %H:%M')
    timestamp_heure_etude_domicile_arrivee_vendredi = datetime.datetime.strptime(
        "04/10/20 " + str(int(heure_etude_domicile_arrivee)) + ":" + str(int(heure_etude_domicile_arrivee % 1 * 60)),
        '%m/%d/%y %H:%M')

    timestamp_heure_1_depart = datetime.datetime.strptime(
        "04/11/20 " + str(int(heure_domicile_parent_depart)) + ":" + str(int(heure_domicile_parent_depart % 1 * 60)),
        '%m/%d/%y %H:%M')
    timestamp_heure_1_arrivee = datetime.datetime.strptime(
        "04/11/20 " + str(int(heure_domicile_parent_arrivee)) + ":" + str(int(heure_domicile_parent_arrivee % 1 * 60)),
        '%m/%d/%y %H:%M')
    timestamp_heure_2_depart = datetime.datetime.strptime(
        "04/12/20 " + str(int(heure_parent_domicile_depart)) + ":" + str(int(heure_parent_domicile_depart % 1 * 60)),
        '%m/%d/%y %H:%M')
    timestamp_heure_2_arrivee = datetime.datetime.strptime(
        "04/12/20 " + str(int(heure_parent_domicile_arrivee)) + ":" + str(int(heure_parent_domicile_arrivee % 1 * 60)),
        '%m/%d/%y %H:%M')

    allez_travail_lundi_feature = retour_travail_lundi_feature= allez_travail_mardi_feature= retour_travail_mardi_feature= \
    allez_travail_mercredi_feature=retour_travail_mercredi_feature= allez_travail_jeudi_feature= retour_travail_jeudi_feature= \
    allez_travail_vendredi_feature= retour_travail_vendredi_feature=allez_travail_samedi_feature=retour_travail_samedi_feature=\
        allez_travail_dimanche_feature=retour_travail_dimanche_feature= ""
    properties_aller_travail = {'name': "allez", 'type_trip': "domicile_travail", 'sexe': sexe, 'filiere': filiere,
                                'boursier': boursier, 'revenu_fiscal': revenu_fiscal, 'situation': situation,
                                'region_domicile': region_domicile, 'region_parent': region_parent}
    properties_retour_travail = {'name': "retour", 'type_trip': "travail_domicile", 'sexe': sexe, 'filiere': filiere,
                                 'boursier': boursier, 'revenu_fiscal': revenu_fiscal, 'situation': situation,
                                 'region_domicile': region_domicile, 'region_parent': region_parent}




    if (travail_semaine_weekend == "soir"):

        timestamp_heure_domicile_travail_depart_lundi = datetime.datetime.strptime(
            "04/06/20 " + str(int(heure_depart_domicile_travail)) + ":" + str(
                int(heure_depart_domicile_travail % 1 * 60)),
            '%m/%d/%y %H:%M')

        timestamp_heure_domicile_travail_arrivee_lundi = datetime.datetime.strptime(
            "04/06/20 " + str(int(heure_debut_travail)) + ":" + str(
                int(heure_debut_travail % 1 * 60)),
            '%m/%d/%y %H:%M')

        timestamp_heure_travail_domicile_depart_lundi = datetime.datetime.strptime(
            "04/06/20 " + str(int(heure_fin_travail)) + ":" + str(
                int(heure_fin_travail % 1 * 60)),
            '%m/%d/%y %H:%M')

        timestamp_heure_travail_domicile_arrivee_lundi = datetime.datetime.strptime(
            "04/06/20 " + str(int(heure_arrivee_domicile_travail)) + ":" + str(
                int(heure_arrivee_domicile_travail % 1 * 60)),
            '%m/%d/%y %H:%M')

        timestamp_heure_domicile_travail_depart_mardi = datetime.datetime.strptime(
            "04/07/20 " + str(int(heure_depart_domicile_travail)) + ":" + str(
                int(heure_depart_domicile_travail % 1 * 60)),
            '%m/%d/%y %H:%M')

        timestamp_heure_domicile_travail_arrivee_mardi = datetime.datetime.strptime(
            "04/07/20 " + str(int(heure_debut_travail)) + ":" + str(
                int(heure_debut_travail % 1 * 60)),
            '%m/%d/%y %H:%M')

        timestamp_heure_travail_domicile_depart_mardi = datetime.datetime.strptime(
            "04/07/20 " + str(int(heure_fin_travail)) + ":" + str(
                int(heure_fin_travail % 1 * 60)),
            '%m/%d/%y %H:%M')

        timestamp_heure_travail_domicile_arrivee_mardi = datetime.datetime.strptime(
            "04/07/20 " + str(int(heure_arrivee_domicile_travail)) + ":" + str(
                int(heure_arrivee_domicile_travail % 1 * 60)),
            '%m/%d/%y %H:%M')

        timestamp_heure_domicile_travail_depart_mercredi = datetime.datetime.strptime(
            "04/08/20 " + str(int(heure_depart_domicile_travail)) + ":" + str(
                int(heure_depart_domicile_travail % 1 * 60)),
            '%m/%d/%y %H:%M')

        timestamp_heure_domicile_travail_arrivee_mercredi = datetime.datetime.strptime(
            "04/08/20 " + str(int(heure_debut_travail)) + ":" + str(
                int(heure_debut_travail % 1 * 60)),
            '%m/%d/%y %H:%M')

        timestamp_heure_travail_domicile_depart_mercredi = datetime.datetime.strptime(
            "04/08/20 " + str(int(heure_fin_travail)) + ":" + str(
                int(heure_fin_travail % 1 * 60)),
            '%m/%d/%y %H:%M')

        timestamp_heure_travail_domicile_arrivee_mercredi = datetime.datetime.strptime(
            "04/08/20 " + str(int(heure_arrivee_domicile_travail)) + ":" + str(
                int(heure_arrivee_domicile_travail % 1 * 60)),
            '%m/%d/%y %H:%M')

        timestamp_heure_domicile_travail_depart_jeudi = datetime.datetime.strptime(
            "04/09/20 " + str(int(heure_depart_domicile_travail)) + ":" + str(
                int(heure_depart_domicile_travail % 1 * 60)),
            '%m/%d/%y %H:%M')

        timestamp_heure_domicile_travail_arrivee_jeudi = datetime.datetime.strptime(
            "04/09/20 " + str(int(heure_debut_travail)) + ":" + str(
                int(heure_debut_travail % 1 * 60)),
            '%m/%d/%y %H:%M')

        timestamp_heure_travail_domicile_depart_jeudi = datetime.datetime.strptime(
            "04/09/20 " + str(int(heure_fin_travail)) + ":" + str(
                int(heure_fin_travail % 1 * 60)),
            '%m/%d/%y %H:%M')

        timestamp_heure_travail_domicile_arrivee_jeudi = datetime.datetime.strptime(
            "04/09/20 " + str(int(heure_arrivee_domicile_travail)) + ":" + str(
                int(heure_arrivee_domicile_travail % 1 * 60)),
            '%m/%d/%y %H:%M')

        timestamp_heure_domicile_travail_depart_vendredi = datetime.datetime.strptime(
            "04/10/20 " + str(int(heure_depart_domicile_travail)) + ":" + str(
                int(heure_depart_domicile_travail % 1 * 60)),
            '%m/%d/%y %H:%M')

        timestamp_heure_domicile_travail_arrivee_vendredi = datetime.datetime.strptime(
            "04/10/20 " + str(int(heure_debut_travail)) + ":" + str(
                int(heure_debut_travail % 1 * 60)),
            '%m/%d/%y %H:%M')

        timestamp_heure_travail_domicile_depart_vendredi = datetime.datetime.strptime(
            "04/10/20 " + str(int(heure_fin_travail)) + ":" + str(
                int(heure_fin_travail % 1 * 60)),
            '%m/%d/%y %H:%M')

        timestamp_heure_travail_domicile_arrivee_vendredi = datetime.datetime.strptime(
            "04/10/20 " + str(int(heure_arrivee_domicile_travail)) + ":" + str(
                int(heure_arrivee_domicile_travail % 1 * 60)),
            '%m/%d/%y %H:%M')



        allez_travail_lundi = geojson.LineString(
            [[long_domicile, lat_domicile, 0, datetime.datetime.timestamp(timestamp_heure_domicile_travail_depart_lundi) + 7200],
             [long_travail, lat_travail, 0,
              datetime.datetime.timestamp(timestamp_heure_domicile_travail_arrivee_lundi) + 7200],
             [long_travail + 0.0000000000000000001, lat_travail, 0,
              datetime.datetime.timestamp(timestamp_heure_domicile_travail_arrivee_lundi) + 7200.00000000000001]])

        retour_travail_lundi = geojson.LineString(
            [[long_travail, lat_travail, 0, datetime.datetime.timestamp(timestamp_heure_travail_domicile_depart_lundi) + 7200],
             [long_domicile, lat_domicile, 0,
              datetime.datetime.timestamp(timestamp_heure_travail_domicile_arrivee_lundi) + 7200],
             [long_domicile + 0.0000000000000000001, lat_domicile, 0,
              datetime.datetime.timestamp(timestamp_heure_travail_domicile_arrivee_lundi) + 7200.00000000000001]])

        allez_travail_mardi = geojson.LineString(
            [[long_domicile, lat_domicile, 0, datetime.datetime.timestamp(timestamp_heure_domicile_travail_depart_mardi) + 7200],
             [long_travail, lat_travail, 0,
              datetime.datetime.timestamp(timestamp_heure_domicile_travail_arrivee_mardi) + 7200],
             [long_travail + 0.0000000000000000001, lat_travail, 0,
              datetime.datetime.timestamp(timestamp_heure_domicile_travail_arrivee_mardi) + 7200.00000000000001]])

        retour_travail_mardi = geojson.LineString(
            [[long_travail, lat_travail, 0, datetime.datetime.timestamp(timestamp_heure_travail_domicile_depart_mardi) + 7200],
             [long_domicile, lat_domicile, 0,
              datetime.datetime.timestamp(timestamp_heure_travail_domicile_arrivee_mardi) + 7200],
             [long_domicile + 0.0000000000000000001, lat_domicile, 0,
              datetime.datetime.timestamp(timestamp_heure_travail_domicile_arrivee_mardi) + 7200.00000000000001]])

        allez_travail_mercredi = geojson.LineString(
            [[long_domicile, lat_domicile, 0, datetime.datetime.timestamp(timestamp_heure_domicile_travail_depart_mercredi) + 7200],
             [long_travail, lat_travail, 0,
              datetime.datetime.timestamp(timestamp_heure_domicile_travail_arrivee_mercredi) + 7200],
             [long_travail + 0.0000000000000000001, lat_travail, 0,
              datetime.datetime.timestamp(timestamp_heure_domicile_travail_arrivee_mercredi) + 7200.00000000000001]])

        retour_travail_mercredi = geojson.LineString(
            [[long_travail, lat_travail, 0, datetime.datetime.timestamp(timestamp_heure_travail_domicile_depart_mercredi) + 7200],
             [long_domicile, lat_domicile, 0,
              datetime.datetime.timestamp(timestamp_heure_travail_domicile_arrivee_mercredi) + 7200],
             [long_domicile + 0.0000000000000000001, lat_domicile, 0,
              datetime.datetime.timestamp(timestamp_heure_travail_domicile_arrivee_mercredi) + 7200.00000000000001]])

        allez_travail_jeudi = geojson.LineString(
            [[long_domicile, lat_domicile, 0, datetime.datetime.timestamp(timestamp_heure_domicile_travail_depart_lundi) + 7200],
             [long_travail, lat_travail, 0,
              datetime.datetime.timestamp(timestamp_heure_domicile_travail_arrivee_jeudi) + 7200],
             [long_travail + 0.0000000000000000001, lat_travail, 0,
              datetime.datetime.timestamp(timestamp_heure_domicile_travail_arrivee_jeudi) + 7200.00000000000001]])

        retour_travail_jeudi = geojson.LineString(
            [[long_travail, lat_travail, 0, datetime.datetime.timestamp(timestamp_heure_travail_domicile_depart_jeudi) + 7200],
             [long_domicile, lat_domicile, 0,
              datetime.datetime.timestamp(timestamp_heure_travail_domicile_arrivee_jeudi) + 7200],
             [long_domicile + 0.0000000000000000001, lat_domicile, 0,
              datetime.datetime.timestamp(timestamp_heure_travail_domicile_arrivee_jeudi) + 7200.00000000000001]])

        allez_travail_vendredi = geojson.LineString(
            [[long_domicile, lat_domicile, 0, datetime.datetime.timestamp(timestamp_heure_domicile_travail_depart_vendredi) + 7200],
             [long_travail, lat_travail, 0,
              datetime.datetime.timestamp(timestamp_heure_domicile_travail_arrivee_vendredi) + 7200],
             [long_travail + 0.0000000000000000001, lat_travail, 0,
              datetime.datetime.timestamp(timestamp_heure_domicile_travail_arrivee_vendredi) + 7200.00000000000001]])

        retour_travail_vendredi = geojson.LineString(
            [[long_travail, lat_travail, 0, datetime.datetime.timestamp(timestamp_heure_travail_domicile_depart_vendredi) + 7200],
             [long_domicile, lat_domicile, 0,
              datetime.datetime.timestamp(timestamp_heure_travail_domicile_arrivee_vendredi) + 7200],
             [long_domicile + 0.0000000000000000001, lat_domicile, 0,
              datetime.datetime.timestamp(timestamp_heure_travail_domicile_arrivee_vendredi) + 7200.00000000000001]])



        allez_travail_lundi_feature = geojson.Feature(geometry=allez_travail_lundi, properties=properties_aller_travail)
        retour_travail_lundi_feature = geojson.Feature(geometry=retour_travail_lundi, properties=properties_retour_travail)

        allez_travail_mardi_feature = geojson.Feature(geometry=allez_travail_mardi, properties=properties_aller_travail)
        retour_travail_mardi_feature = geojson.Feature(geometry=retour_travail_mardi, properties=properties_retour_travail)

        allez_travail_mercredi_feature = geojson.Feature(geometry=allez_travail_mercredi, properties=properties_aller_travail)
        retour_travail_mercredi_feature = geojson.Feature(geometry=retour_travail_mercredi, properties=properties_retour_travail)

        allez_travail_jeudi_feature = geojson.Feature(geometry=allez_travail_jeudi, properties=properties_aller_travail)
        retour_travail_jeudi_feature = geojson.Feature(geometry=retour_travail_jeudi, properties=properties_retour_travail)

        allez_travail_vendredi_feature = geojson.Feature(geometry=allez_travail_vendredi, properties=properties_aller_travail)
        retour_travail_vendredi_feature = geojson.Feature(geometry=retour_travail_vendredi, properties=properties_retour_travail)



    elif(travail_semaine_weekend == "week-end"):

        timestamp_heure_domicile_travail_depart_samedi = datetime.datetime.strptime(
            "04/11/20 " + str(int(heure_depart_domicile_travail)) + ":" + str(
                int(heure_depart_domicile_travail % 1 * 60)),
            '%m/%d/%y %H:%M')

        timestamp_heure_domicile_travail_arrivee_samedi = datetime.datetime.strptime(
            "04/11/20 " + str(int(heure_debut_travail)) + ":" + str(
                int(heure_debut_travail % 1 * 60)),
            '%m/%d/%y %H:%M')

        timestamp_heure_travail_domicile_depart_samedi = datetime.datetime.strptime(
            "04/11/20 " + str(int(heure_fin_travail)) + ":" + str(
                int(heure_fin_travail % 1 * 60)),
            '%m/%d/%y %H:%M')

        timestamp_heure_travail_domicile_arrivee_samedi = datetime.datetime.strptime(
            "04/11/20 " + str(int(heure_arrivee_domicile_travail)) + ":" + str(
                int(heure_arrivee_domicile_travail % 1 * 60)),
            '%m/%d/%y %H:%M')

        timestamp_heure_domicile_travail_depart_dimanche = datetime.datetime.strptime(
            "04/12/20 " + str(int(heure_depart_domicile_travail)) + ":" + str(
                int(heure_depart_domicile_travail % 1 * 60)),
            '%m/%d/%y %H:%M')

        timestamp_heure_domicile_travail_arrivee_dimanche = datetime.datetime.strptime(
            "04/12/20 " + str(int(heure_debut_travail)) + ":" + str(
                int(heure_debut_travail % 1 * 60)),
            '%m/%d/%y %H:%M')

        timestamp_heure_travail_domicile_depart_dimanche = datetime.datetime.strptime(
            "04/12/20 " + str(int(heure_fin_travail)) + ":" + str(
                int(heure_fin_travail % 1 * 60)),
            '%m/%d/%y %H:%M')

        timestamp_heure_travail_domicile_arrivee_dimanche = datetime.datetime.strptime(
            "04/12/20 " + str(int(heure_arrivee_domicile_travail)) + ":" + str(
                int(heure_arrivee_domicile_travail % 1 * 60)),
            '%m/%d/%y %H:%M')

        allez_travail_samedi = geojson.LineString(
            [[long_domicile, lat_domicile, 0,
              datetime.datetime.timestamp(timestamp_heure_domicile_travail_depart_samedi) + 7200],
             [long_travail, lat_travail, 0,
              datetime.datetime.timestamp(timestamp_heure_domicile_travail_arrivee_samedi) + 7200],
             [long_travail + 0.0000000000000000001, lat_travail, 0,
              datetime.datetime.timestamp(timestamp_heure_domicile_travail_arrivee_samedi) + 7200.00000000000001]])

        retour_travail_samedi = geojson.LineString(
            [[long_travail, lat_travail, 0,
              datetime.datetime.timestamp(timestamp_heure_travail_domicile_depart_samedi) + 7200],
             [long_domicile, lat_domicile, 0,
              datetime.datetime.timestamp(timestamp_heure_travail_domicile_arrivee_samedi) + 7200],
             [long_domicile + 0.0000000000000000001, lat_domicile, 0,
              datetime.datetime.timestamp(timestamp_heure_travail_domicile_arrivee_samedi) + 7200.00000000000001]])

        allez_travail_dimanche = geojson.LineString(
            [[long_domicile, lat_domicile, 0,
              datetime.datetime.timestamp(timestamp_heure_domicile_travail_depart_dimanche) + 7200],
             [long_travail, lat_travail, 0,
              datetime.datetime.timestamp(timestamp_heure_domicile_travail_arrivee_dimanche) + 7200],
             [long_travail + 0.0000000000000000001, lat_travail, 0,
              datetime.datetime.timestamp(timestamp_heure_domicile_travail_arrivee_dimanche) + 7200.00000000000001]])

        retour_travail_dimanche = geojson.LineString(
            [[long_travail, lat_travail, 0,
              datetime.datetime.timestamp(timestamp_heure_travail_domicile_depart_dimanche) + 7200],
             [long_domicile, lat_domicile, 0,
              datetime.datetime.timestamp(timestamp_heure_travail_domicile_arrivee_dimanche) + 7200],
             [long_domicile + 0.0000000000000000001, lat_domicile, 0,
              datetime.datetime.timestamp(timestamp_heure_travail_domicile_arrivee_dimanche) + 7200.00000000000001]])

        allez_travail_samedi_feature = geojson.Feature(geometry=allez_travail_samedi, properties=properties_aller_travail)
        retour_travail_samedi_feature = geojson.Feature(geometry=retour_travail_samedi,
                                                       properties=properties_retour_travail)

        allez_travail_dimanche_feature = geojson.Feature(geometry=allez_travail_dimanche, properties=properties_aller_travail)
        retour_travail_dimanche_feature = geojson.Feature(geometry=retour_travail_dimanche,
                                                       properties=properties_retour_travail)


    ############### CREATION DES LIGNES DE DONNEES A INSERER DANS LE GEOJSON #################


    allez_parent = geojson.LineString([[long_domicile, lat_domicile, 0,datetime.datetime.timestamp(timestamp_heure_1_depart)+7200],
                           [long_parent, lat_parent, 0,datetime.datetime.timestamp(timestamp_heure_1_arrivee)+7200 ],
                                [long_parent+0.000001, lat_parent+0.000001, 0, datetime.datetime.timestamp(timestamp_heure_1_arrivee)+7200.0001]])

    retour_parent = geojson.LineString([[long_parent, lat_parent, 0,datetime.datetime.timestamp(timestamp_heure_2_depart)+7200],
                           [long_domicile, lat_domicile, 0,datetime.datetime.timestamp(timestamp_heure_2_arrivee)+7200 ],
                                 [long_domicile+0.000001, lat_domicile+0.000001, 0, datetime.datetime.timestamp(timestamp_heure_2_arrivee)+7200.0001]])

    allez_etude_lundi = geojson.LineString([[long_domicile, lat_domicile, 0,datetime.datetime.timestamp(timestamp_heure_domicile_etude_depart_lundi)+7200],
                           [long_etude, lat_etude, 0,datetime.datetime.timestamp(timestamp_heure_domicile_etude_arrivee_lundi)+7200 ],
                                [long_etude+0.00000000000000000001, lat_etude, 0, datetime.datetime.timestamp(timestamp_heure_domicile_etude_arrivee_lundi)+7200.0000000000001]])

    retour_etude_lundi = geojson.LineString([[long_etude, lat_etude, 0,datetime.datetime.timestamp(timestamp_heure_etude_domicile_depart_lundi)+7200],
                           [long_domicile, lat_domicile, 0,datetime.datetime.timestamp(timestamp_heure_etude_domicile_arrivee_lundi)+7200 ],
                                 [long_domicile+0.0000000000000000001, lat_domicile, 0, datetime.datetime.timestamp(timestamp_heure_etude_domicile_arrivee_lundi)+7200.00000000000001]])

    allez_etude_mardi = geojson.LineString([[long_domicile, lat_domicile, 0,datetime.datetime.timestamp(timestamp_heure_domicile_etude_depart_mardi)+7200],
                           [long_etude, lat_etude, 0,datetime.datetime.timestamp(timestamp_heure_domicile_etude_arrivee_mardi)+7200 ],
                                [long_etude+0.000001, lat_etude+0.000001, 0, datetime.datetime.timestamp(timestamp_heure_domicile_etude_arrivee_mardi)+7200.0001]])

    retour_etude_mardi = geojson.LineString([[long_etude, lat_etude, 0,datetime.datetime.timestamp(timestamp_heure_etude_domicile_depart_mardi)+7200],
                           [long_domicile, lat_domicile, 0,datetime.datetime.timestamp(timestamp_heure_etude_domicile_arrivee_mardi)+7200 ],
                                 [long_domicile+0.000001, lat_domicile+0.000001, 0, datetime.datetime.timestamp(timestamp_heure_etude_domicile_arrivee_mardi)+7200.0001]])

    allez_etude_mercredi = geojson.LineString([[long_domicile, lat_domicile, 0,datetime.datetime.timestamp(timestamp_heure_domicile_etude_depart_mercredi)+7200],
                           [long_etude, lat_etude, 0,datetime.datetime.timestamp(timestamp_heure_domicile_etude_arrivee_mercredi)+7200 ],
                                [long_etude+0.000001, lat_etude+0.000001, 0, datetime.datetime.timestamp(timestamp_heure_domicile_etude_arrivee_mercredi)+7200.0001]])

    retour_etude_mercredi = geojson.LineString([[long_etude, lat_etude, 0,datetime.datetime.timestamp(timestamp_heure_etude_domicile_depart_mercredi)+7200],
                           [long_domicile, lat_domicile, 0,datetime.datetime.timestamp(timestamp_heure_etude_domicile_arrivee_mercredi)+7200 ],
                                 [long_domicile+0.000001, lat_domicile+0.000001, 0, datetime.datetime.timestamp(timestamp_heure_etude_domicile_arrivee_mercredi)+7200.0001]])

    allez_etude_jeudi = geojson.LineString([[long_domicile, lat_domicile, 0,datetime.datetime.timestamp(timestamp_heure_domicile_etude_depart_jeudi)+7200],
                           [long_etude, lat_etude, 0,datetime.datetime.timestamp(timestamp_heure_domicile_etude_arrivee_jeudi)+7200 ],
                                [long_etude+0.000001, lat_etude+0.000001, 0, datetime.datetime.timestamp(timestamp_heure_domicile_etude_arrivee_jeudi)+7200.0001]])

    retour_etude_jeudi = geojson.LineString([[long_etude, lat_etude, 0,datetime.datetime.timestamp(timestamp_heure_etude_domicile_depart_jeudi)+7200],
                           [long_domicile, lat_domicile, 0,datetime.datetime.timestamp(timestamp_heure_etude_domicile_arrivee_jeudi)+7200 ],
                                 [long_domicile+0.000001, lat_domicile+0.000001, 0, datetime.datetime.timestamp(timestamp_heure_etude_domicile_arrivee_jeudi)+7200.0001]])

    allez_etude_vendredi = geojson.LineString([[long_domicile, lat_domicile, 0,datetime.datetime.timestamp(timestamp_heure_domicile_etude_depart_vendredi)+7200],
                           [long_etude, lat_etude, 0,datetime.datetime.timestamp(timestamp_heure_domicile_etude_arrivee_vendredi)+7200 ],
                                [long_etude+0.000001, lat_etude+0.000001, 0, datetime.datetime.timestamp(timestamp_heure_domicile_etude_arrivee_vendredi)+7200.0001]])

    retour_etude_vendredi = geojson.LineString([[long_etude, lat_etude, 0,datetime.datetime.timestamp(timestamp_heure_etude_domicile_depart_vendredi)+7200],
                           [long_domicile, lat_domicile, 0,datetime.datetime.timestamp(timestamp_heure_etude_domicile_arrivee_vendredi)+7200 ],
                                 [long_domicile+0.000001, lat_domicile+0.000001, 0, datetime.datetime.timestamp(timestamp_heure_etude_domicile_arrivee_vendredi)+7200.0001]])





    ######### PROPERTIES DE NOS TRIPS ###########


    properties_aller_parent = {'name': "allez", 'type_trip': "parent_domicile", 'sexe': sexe, 'filiere': filiere,
                               'boursier': boursier, 'revenu_fiscal': revenu_fiscal, 'situation': situation,
                               'region_domicile': region_domicile, 'region_parent': region_parent}
    properties_retour_parent = {'name': "retour", 'type_trip': "domicile_parent", 'sexe': sexe, 'filiere': filiere,
                                'boursier': boursier, 'revenu_fiscal': revenu_fiscal, 'situation': situation,
                                'region_domicile': region_domicile, 'region_parent': region_parent}


    properties_aller_etude = {'name': "allez", 'type_trip': "domicile_etude", 'sexe': sexe, 'filiere': filiere,
                              'boursier': boursier, 'revenu_fiscal': revenu_fiscal, 'situation': situation,
                              'region_domicile': region_domicile, 'region_parent': region_parent}
    properties_retour_etude = {'name': "retour", 'type_trip': "etude_domicile", 'sexe': sexe, 'filiere': filiere,
                               'boursier': boursier, 'revenu_fiscal': revenu_fiscal, 'situation': situation,
                               'region_domicile': region_domicile, 'region_parent': region_parent}





    ######### CREATION DES FEATURES A INSERER DANS LA FEATURE COLLECTION ###########


    allez_parent_feature = geojson.Feature(geometry=allez_parent, properties=properties_aller_parent)
    retour_parent_feature = geojson.Feature(geometry=retour_parent, properties=properties_retour_parent)


    allez_etude_lundi_feature = geojson.Feature(geometry=allez_etude_lundi, properties=properties_aller_etude)
    retour_etude_lundi_feature = geojson.Feature(geometry=retour_etude_lundi, properties=properties_retour_etude)

    allez_etude_mardi_feature = geojson.Feature(geometry=allez_etude_mardi, properties=properties_aller_etude)
    retour_etude__mardi_feature = geojson.Feature(geometry=retour_etude_mardi, properties=properties_retour_etude)

    allez_etude_mercredi_feature = geojson.Feature(geometry=allez_etude_mercredi, properties=properties_aller_etude)
    retour_etude_mercredi_feature = geojson.Feature(geometry=retour_etude_mercredi, properties=properties_retour_etude)

    allez_etude_jeudi_feature = geojson.Feature(geometry=allez_etude_jeudi, properties=properties_aller_etude)
    retour_etude_jeudi_feature = geojson.Feature(geometry=retour_etude_jeudi, properties=properties_retour_etude)

    allez_etude_vendredi_feature = geojson.Feature(geometry=allez_etude_vendredi, properties=properties_aller_etude)
    retour_etude_vendredi_feature = geojson.Feature(geometry=retour_etude_vendredi, properties=properties_retour_etude)



    return allez_parent_feature, retour_parent_feature, allez_etude_lundi_feature, retour_etude_lundi_feature, allez_etude_mardi_feature, retour_etude__mardi_feature, \
           allez_etude_mercredi_feature, retour_etude_mercredi_feature, allez_etude_jeudi_feature, retour_etude_jeudi_feature, allez_etude_vendredi_feature, retour_etude_vendredi_feature, \
           allez_travail_lundi_feature, retour_travail_lundi_feature, allez_travail_mardi_feature, retour_travail_mardi_feature,allez_travail_mercredi_feature, \
           retour_travail_mercredi_feature, allez_travail_jeudi_feature, retour_travail_jeudi_feature, allez_travail_vendredi_feature, retour_travail_vendredi_feature,\
           allez_travail_samedi_feature, retour_travail_samedi_feature, allez_travail_dimanche_feature, retour_travail_dimanche_feature,


def creer_donnees_hexbin(nom_fichier_hexbin, travail_semaine_weekend, lat_domicile, long_domicile, lat_etude, long_etude,sexe, lat_travail, long_travail, filiere, boursier, revenu_fiscal, situation,heure_domicile_etude_depart,heure_etude_domicile_arrivee,region_domicile,region_parent,heure_depart_domicile_travail, heure_arrivee_domicile_travail):


    with open(nom_fichier_hexbin, 'a', newline='') as csvfile:

        fieldnames = ['lat', 'lng', 'date', 'type', 'sexe', 'filiere', 'boursier', 'revenu_fiscal', 'situation','region_domicile','region_parent']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        heure_debut = 4
        while (heure_debut < heure_domicile_etude_depart):
            timestamp = datetime.datetime.strptime(
                "04/06/20 " + str(int(heure_debut)) + ":" + str(int(heure_debut % 1 * 60)),
                '%m/%d/%y %H:%M')
            writer.writerow({'lat': lat_domicile, 'lng': long_domicile, 'date': timestamp,
                             'type': 'domicile',
                             'sexe': sexe, 'filiere': filiere, 'boursier': boursier, 'revenu_fiscal': revenu_fiscal,
                             'situation': situation,'region_domicile': region_domicile,'region_parent':region_parent})

            heure_debut += 1

        while (heure_debut < heure_etude_domicile_arrivee):
            timestamp = datetime.datetime.strptime(
                "04/06/20 " + str(int(heure_debut)) + ":" + str(int(heure_debut % 1 * 60)),
                '%m/%d/%y %H:%M')
            writer.writerow({'lat': lat_etude, 'lng': long_etude, 'date': timestamp,
                         'type': 'etude',
                         'sexe': sexe, 'filiere': filiere, 'boursier': boursier, 'revenu_fiscal': revenu_fiscal,
                         'situation': situation,'region_domicile': region_domicile,'region_parent':region_parent})

            heure_debut += 1
        if (travail_semaine_weekend == "soir"):
            while(heure_debut < heure_depart_domicile_travail):
                timestamp = datetime.datetime.strptime(
                    "04/06/20 " + str(int(heure_debut)) + ":" + str(int(heure_debut % 1 * 60)),
                    '%m/%d/%y %H:%M')
                writer.writerow({'lat': lat_domicile, 'lng': long_domicile, 'date': timestamp,
                                 'type': 'travail',
                                 'sexe': sexe, 'filiere': filiere, 'boursier': boursier, 'revenu_fiscal': revenu_fiscal,
                                 'situation': situation, 'region_domicile': region_domicile,
                                 'region_parent': region_parent})
                heure_debut += 1

            while (heure_debut < heure_arrivee_domicile_travail):
                timestamp = datetime.datetime.strptime(
                    "04/06/20 " + str(int(heure_debut)) + ":" + str(int(heure_debut % 1 * 60)),
                    '%m/%d/%y %H:%M')
                writer.writerow({'lat': lat_travail, 'lng': long_travail, 'date': timestamp,
                                 'type': 'domicile',
                                 'sexe': sexe, 'filiere': filiere, 'boursier': boursier, 'revenu_fiscal': revenu_fiscal,
                                 'situation': situation, 'region_domicile': region_domicile,
                                 'region_parent': region_parent})
                heure_debut += 1

        while (heure_debut < 24):
            timestamp = datetime.datetime.strptime(
                "04/06/20 " + str(int(heure_debut)) + ":" + str(int(heure_debut % 1 * 60)),
                '%m/%d/%y %H:%M')
            writer.writerow({'lat': lat_domicile, 'lng': long_domicile, 'date': timestamp,
                             'type': 'domicile',
                             'sexe': sexe, 'filiere': filiere, 'boursier': boursier, 'revenu_fiscal': revenu_fiscal,
                             'situation': situation,'region_domicile': region_domicile,'region_parent':region_parent})

            heure_debut += 1

    """
    timestamp_heure_domicile_etude_depart_lundi = datetime.datetime.strptime(
        "04/06/20 " + str(int(heure_domicile_etude_depart)) + ":" + str(int(heure_domicile_etude_depart % 1 * 60)), '%m/%d/%y %H:%M')
    timestamp_heure_domicile_etude_arrivee_lundi = datetime.datetime.strptime(
        "04/06/20 " + str(int(heure_domicile_etude_arrivee)) + ":" + str(int(heure_domicile_etude_arrivee % 1 * 60)), '%m/%d/%y %H:%M')
    timestamp_heure_etude_domicile_depart_lundi = datetime.datetime.strptime(
        "04/06/20 " + str(int(heure_etude_domicile_depart)) + ":" + str(int(heure_etude_domicile_depart % 1 * 60)), '%m/%d/%y %H:%M')
    timestamp_heure_etude_domicile_arrivee_lundi = datetime.datetime.strptime(
        "04/06/20 " + str(int(heure_etude_domicile_arrivee)) + ":" + str(int(heure_etude_domicile_arrivee % 1 * 60)), '%m/%d/%y %H:%M')

    with open(nom_fichier_hexbin, 'a', newline='') as csvfile:

        fieldnames = ['lat', 'lng','date','type','sexe', 'filiere', 'boursier','revenu_fiscal','situation']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writerow({'lat': lat_domicile, 'lng' : long_domicile,'date':timestamp_heure_domicile_etude_depart_lundi,'type':'etude',
                         'sexe' : sexe, 'filiere' : filiere, 'boursier' : boursier, 'revenu_fiscal' : revenu_fiscal, 'situation' : situation})

        writer.writerow({'lat': lat_etude, 'lng': long_etude, 'date': timestamp_heure_domicile_etude_arrivee_lundi,
                         'type': 'etude',
                         'sexe': sexe, 'filiere': filiere, 'boursier': boursier, 'revenu_fiscal': revenu_fiscal,
                         'situation': situation})

        writer.writerow({'lat': lat_etude, 'lng': long_etude, 'date': timestamp_heure_etude_domicile_depart_lundi,
                         'type': 'etude',
                         'sexe': sexe, 'filiere': filiere, 'boursier': boursier, 'revenu_fiscal': revenu_fiscal,
                         'situation': situation})

        writer.writerow({'lat': lat_domicile, 'lng': long_domicile, 'date': timestamp_heure_etude_domicile_arrivee_lundi,
                         'type': 'etude',
                         'sexe': sexe, 'filiere': filiere, 'boursier': boursier, 'revenu_fiscal': revenu_fiscal,
                         'situation': situation})

        
        if (lat_parent is not None and visite_parent ==True):
            writer.writerow({'depart_lat': lat_domicile, 'depart_lng' : long_domicile, 'arrivee_lat': lat_parent,'arrivee_lng' : long_parent,'type':'parent',
                             'sexe': sexe, 'filiere': filiere, 'boursier': boursier, 'revenu_fiscal': revenu_fiscal,
                             'situation': situation})

        if(lat_travail is not None):
            writer.writerow({'depart_lat': lat_domicile, 'depart_lng' : long_domicile, 'arrivee_lat': lat_travail,'arrivee_lng' : long_travail, 'type':'travail',
                             'sexe': sexe, 'filiere': filiere, 'boursier': boursier, 'revenu_fiscal': revenu_fiscal,
                             'situation': situation})

        """






def Emploi_Temps (nom_fichier_arc,nom_fichier_hexbin, lat_domicile, long_domicile, lat_etude, long_etude, lat_parent, long_parent, lat_travail, long_travail,sexe, filiere, boursier, revenu_fiscal, situation,region_domicile,region_parent):
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
    travail_semaine_weekend="non"
    heure_depart_domicile_parent = heure_arrivee_parent = heure_depart_parent = heure_arrivee_domicile_parent = 0
    visite_parent = False
    random_parent = randrange(10)
    heure_depart_domicile_travail = 0
    heure_debut_travail = 0
    heure_fin_travail = 0
    heure_arrivee_domicile_travail = 0
    if (random_parent<=6 and lat_parent is not None and lat_parent != lat_domicile and Calc_Distance(lat_domicile, long_domicile, lat_parent, long_parent)<650):
        visite_parent = True

    if (lat_travail is not None):
        heure_depart_domicile_travail, heure_debut_travail, heure_fin_travail, heure_arrivee_domicile_travail, travail_semaine_weekend = horaires_travail(
            heure_arrivee_domicile_cours, lat_domicile, long_domicile, lat_travail, long_travail, visite_parent)
        if (heure_depart_domicile_travail is None):
            travail = False
        else :
            travail = True

    else:
        travail = False

    if (visite_parent == True):
        heure_depart_domicile_parent, heure_arrivee_parent, heure_depart_parent, heure_arrivee_domicile_parent = horaires_parent(
            lat_domicile, long_domicile, lat_parent, long_parent)



    allez_feature, retour_feature, allez_etude_lundi, retour_etude_lundi, allez_etude_mardi, retour_etude_mardi, \
    allez_etude_mercredi, retour_etude_mercredi, allez_etude_jeudi, retour_etude_jeudi, allez_etude_vendredi, \
    retour_etude_vendredi, allez_travail_lundi_feature, retour_travail_lundi_feature, allez_travail_mardi_feature, retour_travail_mardi_feature, allez_travail_mercredi_feature, \
    retour_travail_mercredi_feature, allez_travail_jeudi_feature, retour_travail_jeudi_feature, allez_travail_vendredi_feature, retour_travail_vendredi_feature, \
    allez_travail_samedi_feature, retour_travail_samedi_feature, allez_travail_dimanche_feature, retour_travail_dimanche_feature = creer_donnees_trip(
        lat_domicile, long_domicile, lat_parent, long_parent, lat_etude, long_etude, lat_travail, long_travail,
        heure_depart_domicile_cours, heure_debut_cours, heure_fin_cours, heure_arrivee_domicile_cours,
        heure_depart_domicile_parent, heure_arrivee_parent, heure_depart_parent, heure_arrivee_domicile_parent,
        heure_depart_domicile_travail, heure_debut_travail,
        heure_fin_travail, heure_arrivee_domicile_travail, travail_semaine_weekend,
        sexe, filiere, boursier, revenu_fiscal, situation, region_domicile, region_parent)




    features.append(allez_etude_lundi)
    features.append(retour_etude_lundi)
    """
    features.append(allez_etude_mardi)
    features.append(retour_etude_mardi)
    features.append(allez_etude_mercredi)
    features.append(retour_etude_mercredi)
    features.append(allez_etude_jeudi)
    features.append(retour_etude_jeudi)
    features.append(allez_etude_vendredi)
    features.append(retour_etude_vendredi)
        
    """
    if(travail_semaine_weekend == "soir"):
        features.append(allez_travail_lundi_feature)
        features.append(retour_travail_lundi_feature)
    """
            features.append(allez_travail_mardi_feature)
            features.append(retour_travail_mardi_feature)

            features.append(allez_travail_mercredi_feature)
            features.append(retour_travail_mercredi_feature)

            features.append(allez_travail_jeudi_feature)
            features.append(retour_travail_jeudi_feature)

            features.append(allez_travail_vendredi_feature)
            features.append(retour_travail_vendredi_feature)
        
    elif(travail_semaine_weekend == "week-end"):

            features.append(allez_travail_samedi_feature)
            features.append(retour_travail_samedi_feature)

            features.append(allez_travail_dimanche_feature)
            features.append(retour_travail_dimanche_feature)

    if (visite_parent == True):
            features.append(allez_feature)
            features.append(retour_feature)
    """





    creer_donnees_arc(nom_fichier_arc, lat_domicile, long_domicile, lat_etude, long_etude, lat_parent, long_parent, lat_travail, long_travail,visite_parent,sexe, filiere, boursier, revenu_fiscal, situation,region_domicile,region_parent)

    creer_donnees_hexbin(nom_fichier_hexbin, travail_semaine_weekend, lat_domicile, long_domicile, lat_etude, long_etude,sexe, lat_travail, long_travail, filiere, boursier, revenu_fiscal, situation,heure_depart_domicile_cours,heure_arrivee_domicile_cours,region_domicile,region_parent,heure_depart_domicile_travail, heure_arrivee_domicile_travail)

if __name__ == "__main__":
    with open('metropole.geojson') as f:
        data = geojson.load(f)

    # construct point based on lon/lat returned by geocoder

    # check each polygon to see if it contains the point

    polygon = shape(data['geometry'])

    with open("data_stud_200k.geojson") as f:
        data = geojson.load(f)
    features = data['features'][0]["properties"]
    print(features)



    ############## PARAMETRES A MODIFIER ################

    nom_fichier_arc = 'test_arc.csv'

    nom_fichier_trip = 'test_trip.geojson'

    nom_fichier_hexbin = 'test_hexbin.csv'

####################################################

    features =[]

    with open(nom_fichier_arc, 'w', newline='') as csvfile:
        fieldnames = ['depart_lat', 'depart_lng', 'arrivee_lat', 'arrivee_lng','type','sexe', 'filiere', 'boursier','revenu_fiscal','situation','region_domicile','region_parent']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

    with open(nom_fichier_hexbin, 'w', newline='') as csvfile:
        fieldnames = ['lat', 'lng','date','type','sexe', 'filiere', 'boursier','revenu_fiscal','situation','region_domicile','region_parent']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
    i = 0

    for feature in data['features']:
        i+=1
        print(i)
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
        """
        if (lat_etude > 48.9 or lat_etude < 48.8 or long_etude > 2.65 or long_etude < 2.53):
            continue
        """

        if (Calc_Distance(lat_domicile, long_domicile, lat_etude, long_etude) > 20):
            continue

        point_domicile = Point(long_domicile, lat_domicile)

        if polygon.contains(point_domicile)==False:
            continue

        point_parent = Point(long_parent, lat_parent)


        if polygon.contains(point_parent) == False:
            continue


        sexe = feature['properties']['sexe']
        boursier = feature['properties']['bourse']
        situation = feature['properties']['situation']
        filiere = feature['properties']['discipline']
        try:
            revenu_fiscal = feature['properties']['revenu_fiscal'][0]
        except:
            revenu_fiscal = feature['properties']['revenu_fiscal']
        region_domicile = feature['properties']['region_domicile']
        region_parent = feature['properties']['region_parent']


##################################################

        Emploi_Temps(nom_fichier_arc, nom_fichier_hexbin, lat_domicile, long_domicile, lat_etude, long_etude, lat_parent, long_parent, lat_travail,
                     long_travail,sexe, filiere, boursier, revenu_fiscal, situation,region_domicile,region_parent)

    feature_collection = geojson.FeatureCollection(features)
    with open(nom_fichier_trip, 'w') as f:
        geojson.dump(feature_collection, f)




