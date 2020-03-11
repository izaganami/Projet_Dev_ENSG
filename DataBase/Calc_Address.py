import math
class Calc_Address:
    def __init__(self):
        print("Created")
    def Calculate(self,long1,lat1,long2,lat2):
        R=6373
        lon1,lon2,lat1,lat2=math.radians(float(long1)),math.radians(float(long2)),math.radians(float(lat1)),math.radians(float(lat2))
        dlon=lon2-lon1
        dlat=abs(lat2-lat1)
        havers=math.sin(dlat/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin(dlon/2)**2
        c=2*math.atan2(math.sqrt(havers),math.sqrt(1-havers))
        return R*c


