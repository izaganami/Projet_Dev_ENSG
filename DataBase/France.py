import geojson

from shapely.geometry import shape, Point
# depending on your version, use: from shapely.geometry import shape, Point


def in_France(lat,long):
    # load GeoJSON file containing sectors
    with open('metropole.geojson') as f:
        data = geojson.load(f)

    # construct point based on lon/lat returned by geocoder
    point = Point(long, lat)

    # check each polygon to see if it contains the point

    polygon = shape(data['geometry'])
    if polygon.contains(point):
        return True
    else :
        return False