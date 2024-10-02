
import math

def two_points_distance_calculation(coordinates_x, coordinates_y):
    xa = coordinates_x[0]
    ya = coordinates_x[1]
    xb = coordinates_y[0]
    yb = coordinates_y[1]

    distance_squared = (xa - xb)**2 + (ya - yb)**2

    return math.sqrt(distance_squared)

def find_max_distance(distances):
    pass