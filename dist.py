# ------------------------------------------------------------------------------
# This library contains an algorithm for calculating the distance between
# two locations on the earth's surface specified by latitude and longitude.
# ------------------------------------------------------------------------------

from math import acos, cos, sin, radians


# Radius of the earth in kilometers.
earth_radius = 6371


# A Pos instance represents a location on the earth's surface. Latitude and
# longitude should be specified in degrees.
class Pos:
    def __init__(self, latitude, longitude):
        self.lat = latitude
        self.long = longitude


# This function returns the 'great-circle' distance in kilometers between two
# Pos instances calculated using the spherical law of cosines.
# Ref: https://en.wikipedia.org/wiki/Great-circle_distance
def distance(pos1, pos2):
    lat1, long1 = radians(pos1.lat), radians(pos1.long)
    lat2, long2 = radians(pos2.lat), radians(pos2.long)

    delta = abs(long1 - long2)
    angle = acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(delta))

    return angle * earth_radius
