import math
a = 6378137.0
c = 6356752.314245
e = math.sqrt(1 - (c**2 / a**2))
s = (2*math.pi*a**2)*(1 + ((1 - e**2) / e)*math.atanh(e))

print(s)
r = 6371000.0
s = 4*math.pi*r**2
print(s)
