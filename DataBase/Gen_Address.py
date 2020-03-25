import random
import socket
import urllib
import json

from geopy.exc import GeocoderTimedOut
from geopy.geocoders import Nominatim


def Gen_Address():
    try:
        geolocator = Nominatim(user_agent="Projet_Dev")
        long = random.uniform(42, 51)
        long = round(long, 10)

        lat = random.uniform(2, 8)
        lat = round(lat, 10)

        loc = "" + str(long) + "," + str(lat)
        location = geolocator.reverse(loc)
        return location
    except GeocoderTimedOut:
        return Gen_Address()

def Check_Address_in_Fr(Gen_Address):
    location=Gen_Address
    country_string=json.dumps(location.raw,ensure_ascii=True)
    if(country_string != {"error": "Unable to geocode"} ):
        country=json.loads(country_string)
        print(country["address"]["country"])
        return True
    return False

T=Gen_Address()
print(Check_Address_in_Fr(T))

