from math import *
from numpy import *

#N = longitude of the ascending node (deg) OMEGA
#i = inclination to the ecliptic(plane of the Earth's orbit)
#w = argument of perihelion a = semi - major axis, or mean distance from Sun
#e = eccentricity(0 = circle, 0 - 1 = ellipse, 1 = parabola)
#M = mean anomaly(0 at perihelion; increases uniformly with time)
#a given in earth radii for the moon

#d is the date
#Day 0.0 occurs at 2000 Jan 0.0 UT

def deg_normalizer(n):
    while n < 0 or n > 360:
        if n < 0:
            n += 360

        elif n > 360:
            n -= 360
    return n

d = -354112


N = radians(deg_normalizer(125.1228 - (0.0529538083 * d)))
i = 5.1454
w = radians(deg_normalizer(318.0634 + 0.1643573223 * d))
a = 60.2666
e = 0.054900
M = radians(deg_normalizer(115.3654 + 13.0649929509 * d))


#My Code
def EA_calculator():
    EA = M + (e * sin(M) * (1.0 + cos(M)))
    for i in range(10):
        E = EA - (EA - e * sin(EA) - M) / (1 - e * cos(EA))
        EA = E
    return EA

EA = EA_calculator()

v = 2*atan2(sqrt(1+e)*sin(EA/2), sqrt(1-e)*cos(EA/2))

d = a*(1-e*cos(EA))

position_in_orbit = array([d*cos(v), d*sin(v), float(0)]).T
print("Angular Position in Orbit Before Transformation: {}".format(position_in_orbit))
x = (position_in_orbit[0]*((cos(w)*cos(N))-(sin(w)*cos(i)*sin(N))))-(position_in_orbit[1]*((sin(w)*cos(N))+(cos(w)*cos(i)*sin(N))))
y =
z =


#-----------------------------------
#Online Code
xv = a * ( cos(EA) - e )
yv = a * ( sqrt(1.0 - e*e) * sin(EA) )

v = atan2( yv, xv )
r = sqrt( xv*xv + yv*yv )

xh = r * ( cos(N) * cos(v+w) - sin(N) * sin(v+w) * cos(i) )
yh = r * ( sin(N) * cos(v+w) + cos(N) * sin(v+w) * cos(i) )
zh = r * ( sin(v+w) * sin(i) )

print("N: {}".format(N))
print("i: {}".format(i))
print("w: {}".format(w))
print("a: {}".format(a))
print("e: {}".format(e))
print("M: {}".format(M))

print("xE: {}".format(xh))
print("yE: {}".format(yh))
print("zE: {}".format(zh))