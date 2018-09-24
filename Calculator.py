from math import *
from numpy import *

#N = longitude of the ascending node (deg) OMEGA
#i = inclination to the ecliptic(plane of the Earth's orbit)
#w = argument of perihelion a = semi - major axis in Earth radii
#e = eccentricity_ECI(0 = circle, 0 - 1 = ellipse, 1 = parabola)
#M = mean anomaly_ECI(0 at perihelion; increases uniformly_ECI with time)
#a given in earth radii for the moon

#d is the date
#Day_ECI 0.0 occurs at 2000 Jan 0.0 UT

#Paper with Math Here:
## https://downloads.rene-schwarz_ECI.com/download/M001-Keplerian_Orbit_Elements_to_Cartesian_State_Vectors.pdf

#Link to Math in Depth
#http://www.dtic.mil/dtic/tr/fulltex_ECIt/u2/1027338.pdf
#Skipped steps have numbers nex_ECIt to them, click them to understand or y_ECIou'll get lost

#Link to Accurate Code
## https://space.stackex_ECIchange.com/questions/19322/converting-orbital-elements-to-cartesian-state-vectors

#Freedom High School Latitude, Longitude
Latitude = radians(38.91471145625555)
Longitude = radians(-77.53544211387634)

#Moon Landing Latitude, Longitude, Radius
Latitude_Moon = radians(0.6875)
Longitude_Moon = radians(23.4333)
Radius_Moon = 0.272641658

Moon_x = Radius_Moon*sin(Latitude_Moon)*cos(Longitude_Moon)
Moon_y = Radius_Moon*sin(Latitude_Moon)*sin(Longitude_Moon)
Moon_z = Radius_Moon*cos(Latitude_Moon)
Moon_Lat_Long = array([Moon_x, Moon_y, Moon_z])

print("Moon X: {}".format(Moon_x))
print("Moon Y: {}".format(Moon_y))
print("Moon Z: {}".format(Moon_z))

def deg_normalizer(n):
    while n < 0 or n > 360:
        if n < 0:
            n += 360

        elif n > 360:
            n -= 360
    return n

d = -354112 #Apollo 11 Landing Date in 1969
seconds = d*24*60*60
print("Seconds: {}".format(seconds))

N = radians(deg_normalizer(125.1228 - (0.0529538083 * d)))
i = 5.1454
w = radians(deg_normalizer(318.0634 + 0.1643573223 * d))
a = 60.2666
e = 0.054900
M = radians(deg_normalizer(115.3654 + 13.0649929509 * d))

print("N: {}".format(N))
print("i: {}".format(i))
print("w: {}".format(w))
print("a: {}".format(a))
print("e: {}".format(e))
print("M: {}".format(M))

#My_ECI Code
def EA_calculator():
    EA = M + (e * sin(M) * (1.0 + cos(M)))
    for i in range(10):
        E = EA - (EA - e * sin(EA) - M) / (1 - e * cos(EA))
        EA = E
    return EA

EA = EA_calculator()

v = 2*atan2(sqrt(1+e)*sin(EA/2), sqrt(1-e)*cos(EA/2))

d = a*(1-e*cos(EA))
print("D: {}".format(d))

position_in_orbit = array([d*cos(v), d*sin(v), float(0)])+Moon_Lat_Long
print("Angular Position in Orbit Before Transformation: {}".format(position_in_orbit))

x_ECI = (position_in_orbit[0]*((cos(w)*cos(N))-(sin(w)*cos(i)*sin(N))))-(position_in_orbit[1]*((sin(w)*cos(N))+(cos(w)*cos(i)*sin(N))))
y_ECI = position_in_orbit[0]*((cos(w)*sin(N))+(sin(w)*cos(i)*cos(N)))+(position_in_orbit[1]*((cos(w)*cos(i)*cos(N))-(sin(w)*sin(N))))
z_ECI = (position_in_orbit[0]*(sin(w)*sin(i)))+((position_in_orbit[1]*((cos(w)*sin(i)))))

radius_ECI = sqrt(x_ECI*x_ECI+y_ECI*y_ECI+z_ECI*z_ECI)
position_ECI = array([x_ECI,y_ECI,z_ECI])

print("Position Vector ECI: {}".format(position_ECI))
print("Radius ECI: {}".format(radius_ECI))

x_ECEF = x_ECI*(cos(Longitude)*cos(Latitude))
y_ECEF = y_ECI*(cos(Longitude)*sin(Latitude))
z_ECEF = z_ECI*(sin(Longitude))

radius_ECEF = sqrt(x_ECEF*x_ECEF+y_ECI*y_ECI+z_ECI*z_ECI)*6731
position_ECEF = 1000*6371*array([x_ECEF, y_ECEF, z_ECEF])

print("Position Vector Earth Radii ECEF Earth to ECI Moon: {}".format(position_ECEF))
print("Radius ECEF Earth to ECI Moon: {}".format(radius_ECEF))
print("Position Vector km ECEF Earth to ECI Moon: {}".format(position_ECEF))

time_in_meter = seconds*3*10**8
print("Time in Second Meters: {}".format(time_in_meter))

distance = ((position_ECEF.dot(position_ECEF)*1000)-(time_in_meter**2))
print("Distance in Space-Time: {}".format(distance**0.5))
