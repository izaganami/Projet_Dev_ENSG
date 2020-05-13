"""
PARTIE 2 DE LA CRÉATION DES DONNÉES

Ce fichier permet de créer tous les fichiers nécessaires pour la visualisation des données dans kepler.gl
On crée ainsi :
    - 1 fichier csv pour les arcs : permet de visualiser les lieux et tous les types de trajet
    - 2 fichiers geojson pour les trips (domicile-étude / domicile-travail) : permet de représenter les trajets dans le
    temps des étudiants sur une journée
    - 1 fichier csv pour les hexbins : permet de visualiser de façon dynamique le nombre d'étudiant dans un quadrillage

Le principe est de récupérer un à un chaque étudiant dans le fichier créé auparavant et de leur généré un emploi du
temps.
A partir de cet emploi du temps, on peut généré nos fichiers.

"""


#### MODULES ####

from math import sin, cos, sqrt, atan2, radians
from random import randrange
import math as m
import datetime
import geojson
import numpy as np
import random
import csv
from shapely.geometry import shape, Point


############ TEMPS DE TRAJET ###########

def Calc_Temps_Trajet(lat1, long1, lat2, long2):
    """
    Calcule le temps de trajet entre 2 lieux
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
    Calcule la distance entre 2 lieux
    :param lat1: latitude du lieu 1
    :param long1: longitude du lieu 1
    :param lat2: latitude du lieu 2
    :param long2: longitude du lieu 2
    :return: distance entre 2 positions
    """

    # rayon approché de la Terre en km
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
    Créer les trajets entre le domicile étudiant et le lieu d'étude
    :param lat_domicile: latitude du domicile de l'étudiant
    :param long_domicile: longitude du domicile de l'étudiant
    :param lat_etude: latitude du lieu d'étude
    :param long_etude: longitude du lieu d'étude
    :return: horaires auquel l'étudiant quitte son domicile,
    auquel il débute les cours,
    auquel il finit les cours,
    et auquel il est rentré chez lui
    """
    #int aléatoire entre 0 et 99 pour déterminer à quel heure commence un étudiant
    random_debut = randrange(99)


    #A partir d'ici, on détermine l'heure de début et la durée des cours
    #Les cours durent commence entre 8h et 12h30 avec une probabilité plus ou moins importante
    #Ils durent au moins 5 heures et finissent au maximum à 20h
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


    #On veut que nos durée correspondent à des horaires fixes (xxh00 ou xxh30)
    #On récupère l'int de la durée (ex : pour 5,42 ça sera 5)
    int_duree = int(random_duree);

    #On fait la différence entre notre durée en float et cette valeur
    dif = random_duree - float(int_duree);

    #On arrondit selon la différence
    if (dif < 0.25):
        random_duree = int_duree;
    elif ( dif < 0.75 ):
        random_duree = float(int_duree) + 0.5;

    else:
        random_duree = int_duree + 1;

    #un étudiant n'arrivant pas toujours pile à l'heure on ajoute un float aléatoire entre -0.25 (15 minutes d'avance)
    # et 0.05 (3 minutes de retard)
    random_ajout_erreur_debut = random.uniform(-0.25,0.05)

    #même chose pour la fin des cours
    random_ajout_erreur_fin = random.uniform(-0.05, 0.20)


    heure_fin_cours = random_duree + heure_debut_cours + random_ajout_erreur_fin

    heure_debut_cours =heure_debut_cours + random_ajout_erreur_debut

    temps_trajet = Calc_Temps_Trajet(lat_domicile, long_domicile, lat_etude, long_etude)

    heure_depart_domicile = heure_debut_cours - temps_trajet
    heure_arrivee_domicile = heure_fin_cours + temps_trajet


    return heure_depart_domicile, heure_debut_cours, heure_fin_cours, heure_arrivee_domicile




def travail_soir(heure_arrivee_minimale_travail,temps_domicile_travail):
    """
    Créer les trajets entre le domicile étudiant et le lieu de travail les soirs de semaine

    :param heure_arrivee_minimale_travail: heure d'arrivée la plus tôt à laquelle l'étudiant peut arriver à son travail
    :param temps_domicile_travail: temps de trajet entre le domicile de l'étudiant et son lieu de travail
    :return: heure à laquelle l'étudiant part travailler,
    à laquelle il arrive au travail,
    à laquelle il finit son travail,
    à laquelle il est de retour chez lui
    """

    #Le travail commence entre l'heure minimale à laquelle l'étudiant peut être sur son lieu de travail et 21h
    random_debut = randrange(m.ceil(heure_arrivee_minimale_travail),21,1)

    #L'étudiant travaille un certains nombre d'heures
    nombre_heures = randrange(0,21 - random_debut)

    #Auquel on ajoute au moins 2 heures
    random_demi_heure_1 = randrange(0,3)
    if (random_demi_heure_1 == 0):
        random_debut+=0.5

    random_demi_heure_2 = randrange(0,3)
    if(random_demi_heure_2 == 0 and random_demi_heure_1>0):
        nombre_heures+=2.5
    else:
        nombre_heures+=2


    #L'étudiant n'arrive pas pile à l'huere sur son lieu de travail et ne repart pile à l'heure de celui-ci
    random_ajout_erreur_debut = random.uniform(-0.20,0.02)
    random_ajout_erreur_fin = random.uniform(0, 0.20)

    heure_debut_travail = random_debut + random_ajout_erreur_debut
    heure_fin_travail = random_debut + nombre_heures + random_ajout_erreur_fin
    heure_depart_domicile = heure_debut_travail-temps_domicile_travail
    heure_arrivee_domicile = heure_fin_travail+temps_domicile_travail

    return heure_depart_domicile, heure_debut_travail, heure_fin_travail, heure_arrivee_domicile




def travail_weekend(temps_domicile_travail):
    """
    Créer les trajets entre le domicile étudiant et le lieu de travail le week-end

    :param temps_domicile_travail: temps de trajet entre le domicile de l'étudiant et son lieu de travail
    :return:heure à laquelle l'étudiant part travailler,
    à laquelle il arrive au travail,
    à laquelle il finit son travail,
    à laquelle il est de retour chez lui
    """

    #L'étudiant travaille entre 2 et 8h
    nombre_heures = randrange(6)

    #Il commence entre 8 et 21h selon son nombre d'heures
    heure_debut_travail = randrange(15-nombre_heures)+8

    #
    heure_fin_travail = heure_debut_travail+nombre_heures
    heure_depart_domicile = heure_debut_travail - temps_domicile_travail
    heure_arrivee_domicile = heure_fin_travail + temps_domicile_travail

    return heure_depart_domicile, heure_debut_travail, heure_fin_travail, heure_arrivee_domicile




def horaires_travail(heure_arrivee_domicile, lat_domicile, long_domicile, lat_travail, long_travail,visite_parent):
    """
    Créer les trajets entre le domicile étudiant et le lieu de travail (le soir en semaine ou le week-end)

    :param heure_arrivee_domicile: heure à laquelle l'étudiant rentre des cours
    :param lat_domicile: latitude du domicile étudiant
    :param long_domicile: longitude du domicile étudiant
    :param lat_travail: latitude du lieu de travail
    :param long_travail: longitude du lieu de travail
    :param visite_parent: boolean, True : l'étudiant rentre chez ses parents le week-end, False sinon
    :return: heure à laquelle l'étudiant part travailler,
    à laquelle il arrive au travail,
    à laquelle il finit son travail,
    à laquelle il est de retour chez lui
    """

    #permet desavoir si le travail s'effectue le soir ou le week-end
    random = randrange(2)

    #calcul du temps de trajet entre le domicile étudiant et le lieu de travail
    temps_domicile_travail = Calc_Temps_Trajet(lat_domicile, long_domicile, lat_travail,long_travail)

    #calcul de l'heure minimale d'arrivée sur le lieu de travail
    heure_arrivee_minimale_travail = heure_arrivee_domicile + temps_domicile_travail+0.25

    #si l'étudiant ne peut ni travailler le week-end, ni la semaine, on s'arrête là
    if (visite_parent == True and heure_arrivee_minimale_travail >= 20):
        return None,None,None,None,None

    #sinon l'étudiant peut travailler le soir en semaine...
    if (random == 0):
        #on vérifie qu'il puisse arriver sur place avant 20h, si oui, il travaille le soir
        if (heure_arrivee_minimale_travail < 20)  :
            heure_depart_domicile_travail, heure_debut_travail, heure_fin_travail, heure_arrivee_domicile_travail \
                = travail_soir(heure_arrivee_minimale_travail,temps_domicile_travail)
            travail_semaine_weekend = "soir"
            return heure_depart_domicile_travail, heure_debut_travail, heure_fin_travail, \
                   heure_arrivee_domicile_travail, travail_semaine_weekend

        #si non, il travaille le week-end
        else:
            heure_depart_domicile_travail, heure_debut_travail, heure_fin_travail, heure_arrivee_domicile_travail \
                = travail_weekend(temps_domicile_travail)
            travail_semaine_weekend = "week-end"
            return heure_depart_domicile_travail, heure_debut_travail, heure_fin_travail, \
                   heure_arrivee_domicile_travail, travail_semaine_weekend

    #... ou travailler le week-end
    else:
        #si il ne rend pas visite à ses parents le week-end, il peut travailler...
        if (visite_parent == False ):
            heure_depart_domicile_travail, heure_debut_travail, heure_fin_travail, heure_arrivee_domicile_travail \
                = travail_weekend(temps_domicile_travail)
            travail_semaine_weekend = "week-end"
            return heure_depart_domicile_travail, heure_debut_travail, heure_fin_travail, \
                   heure_arrivee_domicile_travail, travail_semaine_weekend
        #sinon il travaille le soir en semaine
        else:
            heure_depart_domicile_travail, heure_debut_travail, heure_fin_travail, heure_arrivee_domicile_travail \
                = travail_soir(heure_arrivee_minimale_travail,temps_domicile_travail)
            travail_semaine_weekend = "soir"
            return heure_depart_domicile_travail, heure_debut_travail, heure_fin_travail, \
                   heure_arrivee_domicile_travail, travail_semaine_weekend



def horaires_parent(lat_domicile, long_domicile, lat_parent, long_parent):
    """
    Créer les trajets entre le domicile étudiant et le domicile parental

    :param lat_domicile: latitude du domicile de l'étudiant
    :param long_domicile: longitude du domicile de l'étudiant
    :param lat_parent: latitude du domicile des parents
    :param long_parent: longitude du domicile des parents
    :return: heure de départ du domicile de l'étudiant pour se rendre chez ses parents,
    heure d'arrivée chez ses parents,
    heure de départ du domicile parental pour rentrer à son domicile étudiant
    heure d'arrivée à son domicile étudiant
    """

    #on calcule le temps de trajet entre les 2 domiciles
    temps_trajet = Calc_Temps_Trajet(lat_domicile, long_domicile, lat_parent, long_parent)

    #l'heure de départ du domicile étudiant le samedi matin est entre 7 et 11h
    heure_depart_domicile = random.uniform(7,11)

    #l'heure du retour au domicile étudiant le dimanche est entre 17h30 et 23h30
    heure_arrivee_domicile = random.uniform(17.5, 23.5)

    #on calcule l'heure d'arrivée chez les parents le samedi et l'heure du départ le dimanche de chez les parents
    heure_arrivee_parent = heure_depart_domicile + temps_trajet
    heure_depart_parent = heure_arrivee_domicile - temps_trajet

    return heure_depart_domicile,heure_arrivee_parent,heure_depart_parent,heure_arrivee_domicile




def creer_donnees_arc(nom_fichier_arc, lat_domicile, long_domicile, lat_etude, long_etude, lat_parent,
                          long_parent, lat_travail, long_travail, sexe, filiere, boursier, revenu_fiscal, type_emploi,
                          situation, residence,region_domicile, region_parent):
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
    :param boursier: l'étudiant est-il boursier : "oui" ou "non"
    :param revenu_fiscal: revenu fiscal du foyer parental de l'étudiant
    :param type_emploi: l'emploi de l'étudiant
    :param situation: marrié ou célibataire
    :param region_domicile: région où vit l'étudiant
    :param region_parent: région où vivent les parents de l'étudiant
    :return:
    """

    #on ouvre le fichier des arcs
    with open(nom_fichier_arc, 'a', newline='') as csvfile:

        #le nom des champs :
        fieldnames = ['depart_lat', 'depart_lng', 'arrivee_lat', 'arrivee_lng', 'type', 'sexe', 'filiere', 'boursier',
                      'revenu_fiscal', 'type_emploi','situation','residence', 'region_domicile', 'region_parent']

        #permet l'écriture des fichiers :
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        #arc domicile étudiant - leiu d'étude
        writer.writerow({'depart_lat': lat_domicile, 'depart_lng': long_domicile, 'arrivee_lat': lat_etude,
                         'arrivee_lng': long_etude, 'type': 'etude',
                         'sexe': sexe, 'filiere': filiere, 'boursier': boursier, 'revenu_fiscal': revenu_fiscal,
                         'type_emploi':type_emploi,
                         'situation': situation, 'residence':residence,'region_domicile': region_domicile,
                         'region_parent': region_parent})

        #arc lieu d'étude - domicile parental
        writer.writerow({'depart_lat': lat_etude, 'depart_lng': long_etude, 'arrivee_lat': lat_parent,
                             'arrivee_lng': long_parent, 'type': 'parent', 'sexe': sexe, 'filiere': filiere,
                             'boursier': boursier, 'revenu_fiscal': revenu_fiscal, 'type_emploi':type_emploi,
                             'situation': situation,'residence':residence,
                             'region_domicile': region_domicile, 'region_parent': region_parent})

        #arc facultatif domiicle étudiant - lieu de travail
        if (lat_travail is not None):
            writer.writerow({'depart_lat': lat_domicile, 'depart_lng': long_domicile, 'arrivee_lat': lat_travail,
                             'arrivee_lng': long_travail, 'type': 'travail', 'sexe': sexe, 'filiere': filiere,
                             'boursier': boursier, 'revenu_fiscal': revenu_fiscal, 'type_emploi':type_emploi,
                             'situation': situation,'residence':residence,
                             'region_domicile': region_domicile, 'region_parent': region_parent})


def creer_donnees_trip(lat_domicile, long_domicile, lat_etude, long_etude, lat_travail,
                           long_travail,
                           heure_domicile_etude_depart,
                           heure_domicile_etude_arrivee, heure_etude_domicile_depart, heure_etude_domicile_arrivee,
                           heure_depart_domicile_travail, heure_debut_travail,
                           heure_fin_travail, heure_arrivee_domicile_travail, travail_semaine_weekend,
                           sexe, filiere, boursier, revenu_fiscal, type_emploi, situation, residence,
                           region_domicile, region_parent):
    """
    Créer les données trips à intégrer dans des fichiers geojson

    :param lat_domicile: latitude du domicile étudiant
    :param long_domicile: longitude du domicile étudiant
    :param lat_etude: latitude du lieu d'étude
    :param long_etude: longitude du lieu d'étude
    :param lat_travail: latitude du lieu de travail
    :param long_travail: longitude du lieu de travail
    :param heure_domicile_etude_depart: heure du départ du domicile étudiant pour le lieu d'étude
    :param heure_domicile_etude_arrivee: heure d'arrivée sur le lieu d'étude
    :param heure_etude_domicile_depart: heure de fin des cours et du retour au domicile étudiant
    :param heure_etude_domicile_arrivee: heure d'arrivée au domicile étudiant après les cours
    :param heure_depart_domicile_travail: heure du départ du domicile étudiant pour le lieu de travail
    :param heure_debut_travail: heure d'arrivée sur le lieu de travail
    :param heure_fin_travail: heure de fin du travail et du retour au domicile étudiant
    :param heure_arrivee_domicile_travail: heure d'arrivée au domicile étudiant après le travail
    :param travail_semaine_weekend: string qui permet de savoir quand l'étudiant travaille : "soir" ou "week-end" ou ""
    :param sexe: sexe de l'étudiant
    :param filiere: filière de l'étudiant
    :param boursier: l'étudiant est-il boursier : "oui" ou "non"
    :param revenu_fiscal: revenu fiscal du foyer parental de l'étudiant
    :param type_emploi: l'emploi de l'étudiant
    :param situation: marrié ou célibataire
    :param residence: l'étudiant vit-il en résidence : "oui" ou "non"
    :param region_domicile: la région du domicile étudiant
    :param region_parent: la région du domicile parental
    :return: features pour le fichier geojson comportant les trips du domicile au lieu d'étude et du domicile au lieu de
    travail pour une journée
    """


    ###### Formatage des heures au format timestamp ######

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

    ###### Création des lignes de données à insérer dans le geojson ######

    allez_etude_lundi = geojson.LineString([[long_domicile, lat_domicile, 0,datetime.datetime.timestamp(timestamp_heure_domicile_etude_depart_lundi)+7200],
                           [long_etude, lat_etude, 0,datetime.datetime.timestamp(timestamp_heure_domicile_etude_arrivee_lundi)+7200 ],
                                [long_etude+0.00000000000000000001, lat_etude, 0, datetime.datetime.timestamp(timestamp_heure_domicile_etude_arrivee_lundi)+7200.0000000000001]])

    retour_etude_lundi = geojson.LineString([[long_etude, lat_etude, 0,datetime.datetime.timestamp(timestamp_heure_etude_domicile_depart_lundi)+7200],
                           [long_domicile, lat_domicile, 0,datetime.datetime.timestamp(timestamp_heure_etude_domicile_arrivee_lundi)+7200 ],
                                 [long_domicile+0.0000000000000000001, lat_domicile, 0, datetime.datetime.timestamp(timestamp_heure_etude_domicile_arrivee_lundi)+7200.00000000000001]])

    ###### Properties de nos trips ######

    properties_aller_etude = {'name': "allez", 'type_trip': "domicile_etude", 'sexe': sexe, 'filiere': filiere,
                              'boursier': boursier, 'revenu_fiscal': revenu_fiscal, 'type_emploi':type_emploi, 'situation': situation,'residence':residence,
                              'region_domicile': region_domicile, 'region_parent': region_parent}
    properties_retour_etude = {'name': "retour", 'type_trip': "etude_domicile", 'sexe': sexe, 'filiere': filiere,
                               'boursier': boursier, 'revenu_fiscal': revenu_fiscal,'type_emploi':type_emploi, 'situation': situation,'residence':residence,
                               'region_domicile': region_domicile, 'region_parent': region_parent}

    ###### Création des features à insérer dans la Feature Collection ######


    allez_etude_lundi_feature = geojson.Feature(geometry=allez_etude_lundi, properties=properties_aller_etude)
    retour_etude_lundi_feature = geojson.Feature(geometry=retour_etude_lundi, properties=properties_retour_etude)






    ##### Features allez-retour sur le lieu de travail (facultatif) ######

    allez_travail_lundi_feature = retour_travail_lundi_feature = ""


    if (travail_semaine_weekend == "soir"):

        ###### Formatage des heures au format timestamp ######

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

        ###### Création des lignes de données à insérer dans le geojson ######

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

        ###### Properties de nos trips ######

        properties_aller_travail = {'name': "allez", 'type_trip': "domicile_travail", 'sexe': sexe, 'filiere': filiere,
                                    'boursier': boursier, 'revenu_fiscal': revenu_fiscal, 'type_emploi': type_emploi,
                                    'situation': situation, 'residence': residence,
                                    'region_domicile': region_domicile, 'region_parent': region_parent}
        properties_retour_travail = {'name': "retour", 'type_trip': "travail_domicile", 'sexe': sexe,
                                     'filiere': filiere,
                                     'boursier': boursier, 'revenu_fiscal': revenu_fiscal, 'type_emploi': type_emploi,
                                     'situation': situation, 'residence': residence,
                                     'region_domicile': region_domicile, 'region_parent': region_parent}

        ###### Création des features à insérer dans la Feature Collection ######

        allez_travail_lundi_feature = geojson.Feature(geometry = allez_travail_lundi,
                                                      properties = properties_aller_travail)
        retour_travail_lundi_feature = geojson.Feature(geometry=retour_travail_lundi,
                                                       properties = properties_retour_travail)



    return allez_etude_lundi_feature, retour_etude_lundi_feature, \
           allez_travail_lundi_feature, retour_travail_lundi_feature






def creer_donnees_hexbin(nom_fichier_hexbin,
                         travail_semaine_weekend, lat_domicile, long_domicile, lat_etude, long_etude,sexe,
                         lat_travail, long_travail, filiere, boursier, revenu_fiscal, type_emploi, situation,
                         heure_domicile_etude_depart, heure_etude_domicile_arrivee, residence,region_domicile,
                         region_parent, heure_depart_domicile_travail, heure_arrivee_domicile_travail):
    """
    Créer les données hexbin à intégrer dans un fichier csv

    :param nom_fichier_hexbin: nom du fichier csv dans lequel on stocke nos données
    :param travail_semaine_weekend: string qui permet de savoir quand l'étudiant travaille : "soir" ou "week-end" ou ""
    :param lat_domicile: latitude du domicile étudiant
    :param long_domicile: longitude du domicile étudiant
    :param lat_etude: latitude du lieu d'étude
    :param long_etude: longitude du lieu d'étude
    :param sexe: sexe de l'étudiant
    :param lat_travail: latitude du lieu de travail
    :param long_travail: longitude du lieu de travail
    :param filiere: filière de l'étudiant
    :param boursier: l'étudiant est-il boursier : "oui" ou "non"
    :param revenu_fiscal: revenu fiscal du foyer parental de l'étudiant
    :param type_emploi: le métier de l'étudiant
    :param situation: marrié ou célibataire
    :param heure_domicile_etude_depart: heure de départ du domicile étudiant pour le lieu d'étude
    :param heure_etude_domicile_arrivee: heure d'arrivée sur le lieu d'étude
    :param residence: l'étudiant vit t'il en résidence : "oui" ou "non"
    :param region_domicile: la région du domicile étudiant
    :param region_parent: la région du domicile parental
    :param heure_depart_domicile_travail: heure de départ du domicile étudiant pour le lieu de travail
    :param heure_arrivee_domicile_travail: heure d'arrivée sur le lieu de travail
    :return:
    """

    #ouverture du fichier hexbin
    with open(nom_fichier_hexbin, 'a', newline='') as csvfile:

        #Valeurs de champs
        fieldnames = ['lat', 'lng', 'date', 'type', 'sexe', 'filiere', 'boursier', 'revenu_fiscal', 'type_emploi',
                      'situation','residence','region_domicile','region_parent']

        #permet d'écrire dans le fichier
        writer_domicile = csv.DictWriter(csvfile, fieldnames=fieldnames)

        #on commence à 4h du matin et on avance heure par heure jusqu'à 24h
        heure_debut = 4

        #tant que l'étudiant ne va pas à l'école, il est à son domicile
        while (heure_debut < heure_domicile_etude_depart):

            #formatage de l'heure au format timestamp
            timestamp = datetime.datetime.strptime(
                        "04/06/20 " + str(int(heure_debut)) + ":" + str(int(heure_debut % 1 * 60)),
                        '%m/%d/%y %H:%M')

            #on écrit dans le fichier des hexbins l'heure et où l'étudiant se trouve
            writer_domicile.writerow({'lat': lat_domicile, 'lng': long_domicile, 'date': timestamp,
                                     'type': 'domicile',
                                     'sexe': sexe, 'filiere': filiere, 'boursier': boursier, 'revenu_fiscal': revenu_fiscal, 'type_emploi':type_emploi,
                                     'situation': situation,'residence':residence,'region_domicile': region_domicile,'region_parent':region_parent})
            heure_debut += 1

        #tant que l'étudiant est sur son lieu d'étude
        while (heure_debut < heure_etude_domicile_arrivee):
            timestamp = datetime.datetime.strptime(
                        "04/06/20 " + str(int(heure_debut)) + ":" + str(int(heure_debut % 1 * 60)),
                        '%m/%d/%y %H:%M')

            writer_domicile.writerow({'lat': lat_etude, 'lng': long_etude, 'date': timestamp,
                                 'type': 'etude',
                                 'sexe': sexe, 'filiere': filiere, 'boursier': boursier, 'revenu_fiscal': revenu_fiscal,'type_emploi':type_emploi,
                                 'situation': situation,'residence':residence,'region_domicile': region_domicile,'region_parent':region_parent})

            heure_debut += 1

        #si l'étudiant travaille le soir en semaine
        if (travail_semaine_weekend == "soir"):

                #tant que l'étudiant n'est pas parti travailler, il est à son domicile
                while(heure_debut < heure_depart_domicile_travail):
                    timestamp = datetime.datetime.strptime(
                            "04/06/20 " + str(int(heure_debut)) + ":" + str(int(heure_debut % 1 * 60)),
                            '%m/%d/%y %H:%M')

                    writer_domicile.writerow({'lat': lat_domicile, 'lng': long_domicile, 'date': timestamp,
                                         'type': 'domicile',
                                                  'sexe': sexe, 'filiere': filiere, 'boursier': boursier,
                                                  'revenu_fiscal': revenu_fiscal, 'type_emploi': type_emploi,
                                                  'situation': situation, 'residence': residence,
                                                  'region_domicile': region_domicile, 'region_parent': region_parent})
                    heure_debut += 1

                #l'étudiant est sur son lieu de travail
                while (heure_debut < heure_arrivee_domicile_travail):
                    timestamp = datetime.datetime.strptime(
                            "04/06/20 " + str(int(heure_debut)) + ":" + str(int(heure_debut % 1 * 60)),
                            '%m/%d/%y %H:%M')

                    writer_domicile.writerow({'lat': lat_travail, 'lng': long_travail, 'date': timestamp,
                                                  'type': 'travail',
                                                  'sexe': sexe, 'filiere': filiere, 'boursier': boursier,
                                                  'revenu_fiscal': revenu_fiscal,'type_emploi':type_emploi,
                                                  'situation': situation,'residence':residence,
                                                  'region_domicile': region_domicile, 'region_parent': region_parent})
                    heure_debut += 1

        #l'étudiant est chez lui jusqu'à la fin de la journée
        while (heure_debut < 24):
                timestamp = datetime.datetime.strptime(
                        "04/06/20 " + str(int(heure_debut)) + ":" + str(int(heure_debut % 1 * 60)),
                        '%m/%d/%y %H:%M')
                writer_domicile.writerow({'lat': lat_domicile, 'lng': long_domicile, 'date': timestamp,
                                     'type': 'domicile',
                                              'sexe': sexe, 'filiere': filiere, 'boursier': boursier,
                                              'revenu_fiscal': revenu_fiscal,'type_emploi':type_emploi,
                                              'situation': situation,'residence':residence,
                                              'region_domicile': region_domicile,'region_parent':region_parent})

                heure_debut += 1




def Emploi_Temps (nom_fichier_arc,nom_fichier_hexbin,
                  lat_domicile, long_domicile, lat_etude, long_etude, lat_parent, long_parent, lat_travail, long_travail,
                  sexe, filiere, boursier, revenu_fiscal, type_emploi, situation,residence,region_domicile,region_parent):
    """
    Fonction principale, permet de créer les emplois du temps des étudiants

    :param nom_fichier_arc: nom du fichier avec les arcs
    :param nom_fichier_hexbin:
    :param lat_domicile: latitude du domicile de l'étudiant
    :param long_domicile: longitude du domicile de l'étudiant
    :param lat_etude: latitude du lieu d'étude
    :param long_etude: longitude du lieu d'étude
    :param lat_parent: latitude du domicile parental
    :param long_parent: longitude du domicile parental
    :param lat_travail: latitude du lieu de travail
    :param long_travail: longitude du lieu de travail
    :param sexe: sexe de l'étudiant
    :param filiere: filière de l'étudiant
    :param boursier: l'étudiant est-il boursier : "oui" ou "non"
    :param revenu_fiscal: revenu fiscal du foyer parental de l'étudiant
    :param type_emploi: le métier de l'étudiant
    :param situation: marrié ou célibataire
    :param residence: l'étudiant vit t'il en résidence : "oui" ou "non"
    :param region_domicile: la région du domicile étudiant
    :param region_parent: la région du domicile parental
    :return:
    """

    #on intialise des variables
    travail_semaine_weekend = "non"
    heure_depart_domicile_parent = heure_arrivee_parent = heure_depart_parent = heure_arrivee_domicile_parent = 0
    heure_depart_domicile_travail = heure_debut_travail = heure_fin_travail = heure_arrivee_domicile_travail = 0
    visite_parent = False


    #on calcule le trajet entre le domicile étudiant et le lieu d'étude
    heure_depart_domicile_cours, heure_debut_cours, heure_fin_cours, heure_arrivee_domicile_cours = horaires_cours(
        lat_domicile, long_domicile, lat_etude, long_etude)



    random_parent = randrange(10)

    #si l'étudiant rentre chez ses parents...
    if (random_parent<=6 and lat_parent is not None and lat_parent != lat_domicile
            and Calc_Distance(lat_domicile, long_domicile, lat_parent, long_parent)<650):
        visite_parent = True

    #si l'étudiant travail...
    if (lat_travail is not None):
        heure_depart_domicile_travail, heure_debut_travail, heure_fin_travail, heure_arrivee_domicile_travail, \
        travail_semaine_weekend = horaires_travail(
            heure_arrivee_domicile_cours, lat_domicile, long_domicile, lat_travail, long_travail, visite_parent)

    #si l'étudiant rentre chez ses parents...
    if (visite_parent == True):

        #...on calcule le trajet effectué : cette partie n'est pas utile pour les données que nous avons voulu
        # représentées dans kepler.gl mais peuvent être utiles à l'avenir
        heure_depart_domicile_parent, heure_arrivee_parent, heure_depart_parent, heure_arrivee_domicile_parent = horaires_parent(
            lat_domicile, long_domicile, lat_parent, long_parent)

    #on crée nos feature à ajouter à notre Feature Collection
    allez_etude_lundi, retour_etude_lundi, allez_travail_lundi_feature, retour_travail_lundi_feature, \
        = creer_donnees_trip(
        lat_domicile, long_domicile, lat_etude, long_etude, lat_travail, long_travail,
        heure_depart_domicile_cours, heure_debut_cours, heure_fin_cours, heure_arrivee_domicile_cours,
        heure_depart_domicile_travail, heure_debut_travail,
        heure_fin_travail, heure_arrivee_domicile_travail, travail_semaine_weekend,
        sexe, filiere, boursier, revenu_fiscal, type_emploi, situation,residence, region_domicile, region_parent)



    #on met nos features dans une liste
    features_etude.append(allez_etude_lundi)
    features_etude.append(retour_etude_lundi)

    #on ajoute les features travail si besoin
    if(travail_semaine_weekend == "soir"):
        features_travail.append(allez_travail_lundi_feature)
        features_travail.append(retour_travail_lundi_feature)

    #on crée nos données arc
    creer_donnees_arc(nom_fichier_arc, lat_domicile, long_domicile, lat_etude, long_etude, lat_parent, long_parent,
                      lat_travail, long_travail,sexe, filiere, boursier, revenu_fiscal, type_emploi,
                      situation,residence,region_domicile,region_parent)

    #on crée nos données hexbins
    creer_donnees_hexbin(nom_fichier_hexbin,
                         travail_semaine_weekend, lat_domicile, long_domicile, lat_etude, long_etude,sexe, lat_travail,
                         long_travail, filiere, boursier, revenu_fiscal, type_emploi, situation,
                         heure_depart_domicile_cours, heure_arrivee_domicile_cours,residence,region_domicile,
                         region_parent,heure_depart_domicile_travail, heure_arrivee_domicile_travail)




if __name__ == "__main__":


    ############## PARAMETRES A MODIFIER ################

    nom_fichier_data = "data_stud_200k.geojson"

    nom_fichier_arc = 'arc_200k.csv'

    nom_fichier_trip_etude = 'trip_etude_200k.geojson'
    nom_fichier_trip_travail = 'trip_travail_200k.geojson'

    nom_fichier_hexbin = 'hexbin_200k.csv'

    ######################################################



    with open(nom_fichier_data) as f:
        data = geojson.load(f)
    features = data['features'][0]["properties"]
    print(features)

    features_etude = []
    features_travail = []

    with open(nom_fichier_arc, 'w', newline='') as csvfile:
        fieldnames = ['depart_lat', 'depart_lng', 'arrivee_lat', 'arrivee_lng','type','sexe', 'filiere', 'boursier',
                      'revenu_fiscal','type_emploi','situation','residence','region_domicile','region_parent']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

    with open(nom_fichier_hexbin, 'w', newline='') as csvfile:
        fieldnames = ['lat', 'lng','date','type','sexe', 'filiere', 'boursier','revenu_fiscal','type_emploi','situation',
                      'residence','region_domicile','region_parent']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()


    i = 0
    #Pour chaque étudiant de notre fichier geojson
    for feature in data['features']:

    ############## RECUPERATION DES DONNEES ################

        #Si l'étudiant travaille
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


        #On retire les valeurs abhérentes
        if (Calc_Distance(lat_domicile, long_domicile, lat_etude, long_etude) > 20):
            continue


        sexe = feature['properties']['sexe']

        boursier = feature['properties']['bourse']

        situation = feature['properties']['situation']

        filiere = feature['properties']['discipline']

        type_emploi = feature['properties']['type_emploi']

        revenu_fiscal = feature['properties']['revenu_fiscal']

        residence = feature['properties']['residence']

        region_domicile = feature['properties']['region_domicile']

        region_parent = feature['properties']['region_parent']

        #########################################################

        i+=1
        print(i)

        #Fonction principale du programme
        Emploi_Temps(nom_fichier_arc, nom_fichier_hexbin,
                     lat_domicile, long_domicile, lat_etude, long_etude, lat_parent, long_parent, lat_travail,
                     long_travail,sexe, filiere, boursier, revenu_fiscal, type_emploi, situation,residence,
                     region_domicile,region_parent)

    #On ajoute nos 2 features à notre Feature Collection
    feature_collection_etude = geojson.FeatureCollection(features_etude)
    with open(nom_fichier_trip_etude, 'w') as f:
        geojson.dump(feature_collection_etude, f)

    feature_collection_travail = geojson.FeatureCollection(features_travail)
    with open(nom_fichier_trip_travail, 'w') as f:
        geojson.dump(feature_collection_travail, f)




