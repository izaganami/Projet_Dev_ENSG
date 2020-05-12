"""
Cette fonction permet de calculer la distance entre 2 adresses
"""

## Modules ##
import math as m
import math



class Calc_Address:
    def __init__(self):
        print("Calc_Adress")

    def Calc_Distance(self,lat1, long1, lat2, long2):
        """
        Calcule la distance entre 2 points
        :param lat1: latitude du point1
        :param long1: longitude du point 1
        :param lat2: latitude du point 2
        :param long2: longitude du point 2
        :return: distance entre le point 1 et le point 2
        """
        # rayon approximé de la Terre
        R = 6373.0

        lat1 = m.radians(lat1)
        long1 = m.radians(long1)
        lat2 = m.radians(lat2)
        long2 = m.radians(long2)

        dlon = long2 - long1
        dlat = lat2 - lat1

        a = m.sin(dlat / 2) ** 2 + m.cos(lat1) * m.cos(lat2) * m.sin(dlon / 2) ** 2
        c = 2 * m.atan2(m.sqrt(a), m.sqrt(1 - a))

        distance = R * c

        return distance

