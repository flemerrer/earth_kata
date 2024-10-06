
import math

# earth_diameter = 12742 km

def find_antipodal_point(coordinates):

    latitude = coordinates[0]

    if coordinates[1] > 0:
        longitude = 180 - coordinates[1]
    else:
        longitude = 180 - abs(coordinates[1])
        longitude = -longitude

    return -latitude, -longitude

def get_altitude(coordinates):
    pass


def two_points_distance_calculation(coordinates_a, coordinates_b, earth_diameter = 12742):

    altitude_difference = coordinates_a[2] + coordinates_b[2]

    return earth_diameter + altitude_difference


def find_max_distance(distances):
    max_distance = 0
    for elem in distances:
        if elem > max_distance:
            max_distance = elem
    return max_distance

    #todo:
    # solve: how do I check that a line pass through the 0;0 point ?
    # refactor functions and tests in order to accept 3D coordinates
    # create or import dataset for reference points across the globe
    # look for existing dataset that might give a diametrically opposite point on earth for any given coordinate

