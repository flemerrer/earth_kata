
import math

def two_points_distance_calculation(coordinates_x, coordinates_y):
    xa = coordinates_x[0]
    ya = coordinates_x[1]
    xb = coordinates_y[0]
    yb = coordinates_y[1]

    distance_squared = (xa - xb)**2 + (ya - yb)**2

    return math.sqrt(distance_squared)

def find_max_distance(distances):
    max_distance = 0
    for elem in distances:
        if elem > max_distance:
            max_distance = elem
    return max_distance

    #todo :refactor functions and tests in order to accept 3D coordinates
    # create or import dataset for reference points across the globe
    # look for existing dataset that might give a diametrically opposite point on earth for any given coordinate
    # solve : how do I check that 2 coordinates are on the same diameter ? they must pass through 0 ; how to check for that ?
