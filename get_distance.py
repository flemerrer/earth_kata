from operator import index
from random import random

import requests


class Location:
    def __init__(self, lati, long, name='', elev = 0):
        self.name = name
        self.coordinates = (lati, long)
        self.elevation = elev

    def set_elevation(self, elevation):
        self.elevation = elevation


capitals_coordinates= {
    'Paris': Location (49, 2, 'Paris'),
    'London': Location(51, -0, 'London'),
    'New York': Location(41, -74, 'New York'),
    'Mexico': Location(19, -99, 'Mexico'),
    'Rio de Janeiro': Location(-23, -43, 'Rio de Janeiro'),
    'Lima': Location(-12, -77, 'Lima'),
    'New Delhi': Location(28, 77, 'New Delhi'),
    'Beijin': Location(22, 113, 'Beijin'),
    'Canberra': Location(-35, 149, 'Canberra'),
}


def create_locations_list ():

    locations_list = []

    for elem in capitals_coordinates:
        # capitals_coordinates[elem].set_elevation(random()*10000)
        locations_list.append(capitals_coordinates[elem])
        print(vars(capitals_coordinates[elem]))

    return locations_list


def find_antipodal_points(locations_list):

    antipodal_points_list = []

    for location in locations_list:
        coordinates = find_antipodal_point(location.coordinates)
        antipodal_points_list.append(Location(coordinates[0], coordinates[1], f'Opposite of {location.name}'))

    return antipodal_points_list


def create_diameters_list(locations, antipodals):

    diameters = []

    for elem in locations:
        i = locations.index(elem)
        diameter = diameter_calculation(elem.elevation, antipodals[i].elevation)
        diameters.append((f'{elem.name} - {antipodals[i].name} Distance', diameter))

    return diameters

def find_antipodal_point(coordinates):
    latitude = coordinates[0]

    if coordinates[1] > 0:
        longitude = 180 - coordinates[1]
    else:
        longitude = 180 - abs(coordinates[1])
        longitude = -longitude

    return -latitude, -longitude


def get_elevation(coordinates):
    response = requests.get(
        f'https://api.open-elevation.com/api/v1/lookup?locations={coordinates[0]},{coordinates[1]}').json()

    return response['results'][0]['elevation']


# earth_diameter is about 12742 km
def diameter_calculation(elevation_a, elevation_b, earth_diameter=12742000):
    elevation_difference = elevation_a + elevation_b

    return earth_diameter + elevation_difference


def find_max_distance(distances):
    max_distance = 0
    for elem in distances:
        if elem > max_distance:
            max_distance = elem
    return max_distance

