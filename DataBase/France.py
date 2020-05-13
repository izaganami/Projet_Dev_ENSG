"""
Cette fonction permet de savoir dans quelle région se trouve un point
"""

## Modules ##
import geojson
from shapely.geometry import shape, Point


def find_region(lat, long):
    """

    :param lat: latitude du point
    :param long: longitude du point
    :return: string du nom de la région ou "Outre-Mer"
    """
    with open('Data_proj/regions.geojson') as f:
        data = geojson.load(f)

    # construct point based on lon/lat returned by geocoder
        point = Point(long, lat)

    # check each polygon to see if it contains the point

        for feature in data['features']:
            polygon = shape(feature['geometry'])

            if polygon.contains(point):
                return feature['properties']['nom']
            else :
                continue
        return"Outre-Mer"