## Modules ##
import random
import socket
import urllib
import json
from itertools import count
from geopy.exc import GeocoderTimedOut
from geopy.geocoders import Nominatim



class Gen_Address:
    def __init__(self):
        print("Création Adresse")

    def Gen_Address(self):
        """

        :return: une adresse
        """
        try:
            geolocator = Nominatim(user_agent="Projet_Dev")
            lat = random.uniform(41.36, 51.1)
            lat = round(lat, 10)

            long = random.uniform(-4.9, 9.6)
            long = round(long, 10)

            loc = "" + str(lat) + "," + str(long)
            location = geolocator.reverse(loc)
            country_string = json.dumps(location.raw, ensure_ascii=True)
            country = json.loads(country_string)
            return location
        except (GeocoderTimedOut,AttributeError,KeyError):
            return Gen_Address()

    def Check_Address_in_Fr(self,Gen_Address):
        """

        :param Gen_Address: l'adresse à récupérer
        :return: True si l'adresse est en France, False sinon
        """
        try:
            location = Gen_Address
            country_string = json.dumps(location.raw, ensure_ascii=True)
            if (country_string != {"error": "Unable to geocode"}):
                country = json.loads(country_string)
                if (country["address"]["country"] == "France"):
                    return True
            return False
        except (AttributeError,KeyError):
            return False


    def Gen_Address_local(self):
        """

        :return: [latitude, longitude] d'un point dans un carré englobant la France et la Corse
        """
        lat = random.uniform(41.36, 51.1)
        lat = round(lat, 10)

        long = random.uniform(-4.9, 9.6)
        long = round(long, 10)
        return [lat,long]


    def Gen_Address_Within_Distane(self,lat0,long0):
        """

        :param lat0: latitude du point autour duquel au veut faire un nouveau point
        :param long0: longitude du point autour duquel au veut faire un nouveau point
        :return: [latitude, longitude] du nouveau point
        """

        test=8
        #tant qu'on ne trouve pas une valeur de distance inférieure à 7km, on ne crée pas notre point
        while test>7:
            #on utilise la fonction expovariate du module random afin d'avoir une concentration des étudiant proche des
            # lieux d'étude puis diminuant quand on progresse
            #on calcule ici un rayon dans lequel se trouvera notre point
            test = random.expovariate(1)*1.8


        #on calcule une latitude aléatoire dans notre rayon
        lat = random.uniform(lat0 - 0.00900009 * test, lat0 + 0.00900009 * test)
        #puis une longitude en fonction de la latitude
        long = random.uniform(
            long0 - (0.016657508 * test - abs((0.016657508 / 0.00900009) * (lat0 - lat)) - 0.0012076332744266403 / 2),
            long0 + (0.016657508 * test - abs((0.016657508 / 0.00900009) * (lat0 - lat))) + 0.0012076332744266403 / 2)

        return [lat,long]





