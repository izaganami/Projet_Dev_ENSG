import math as m
import math
class Calc_Address:
    def __init__(self):
        print("calc address Created")
    def Calculate(self,long1,lat1,long2,lat2):
        R=6373
        lon1,lon2,lat1,lat2=math.radians(float(long1)),math.radians(float(long2)),math.radians(float(lat1)),math.radians(float(lat2))
        dlon=lon2-lon1
        dlat=abs(lat2-lat1)
        havers=math.sin(dlat/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin(dlon/2)**2
        c=2*math.atan2(math.sqrt(havers),math.sqrt(1-havers))
        return R*c

    def Calc_Distance(self,lat1, long1, lat2, long2):
        # approximate radius of earth in km
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

