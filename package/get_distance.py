import json, requests

from package.models import Couple, Location


def get_points_dict_as_list(dictionary):
    return list(dictionary.values())


def get_points_list_from_file(path='points_list.json'):
    with open(path) as file:
        return json.load(file)


# def find_antipodal_points(locations_list):
#     antipodal_points_list = []
#
#     for location in locations_list:
#         coordinates = find_antipodal_point(location)
#         name = ''
#         if location.name is not None:
#             name = location.name
#         antipodal_points_list.append(Location(coordinates.latitude, coordinates.longitude, 0, name))
#
#     return antipodal_points_list


#todo: use reverse geocoding to get the name of the found coordinates
def create_point_and_antipodal_couples(locations_list):
    couples_list = []

    for location in locations_list:
        antipodal = find_antipodal_point(location)
        couple = Couple(location, antipodal)
        if location.name is None:
            couple.name = f'{couple.point.get_coordinates} to {couple.antipodal_point.get_coordinates()} ditance'
        else:
            couple.name = f'{location.name} to its antipodal point distance'
        couples_list.append(couple)

    return couples_list


def find_antipodal_point(location):
    if location.longitude > 0:
        longitude = 180 - location.longitude
    else:
        longitude = 180 - abs(location.longitude)
        longitude = -longitude

    return Location(-location.latitude, -longitude)


def get_elevation(location):
    response = requests.get(
        f'https://api.open-elevation.com/api/v1/lookup?locations={location.latitude},{location.longitude}').json()

    return response['results'][0]['elevation']


#todo: add exception handling ?
def import_equatorial_points():
    URL = 'https://api.open-elevation.com/api/v1/lookup?locations='
    parameters = ''

    for i in range(0, 179):
        parameters += f'0,{i}|'
    parameters += '0,180'

    equator_points = requests.get(f'{URL}{parameters}').json()

    with open("../points_list.json", "w") as outfile:
        json.dump(equator_points, outfile)

    return True

def find_max_distance(couples_list):
    max_distance = 0
    i = -1

    for couple in couples_list:
        distance = couple.return_distance()
        if distance > max_distance:
            max_distance = couple.return_distance()
            i = couples_list.index(couple)

    return couples_list[i]
