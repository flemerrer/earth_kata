import json, requests

from package.models import Couple, Location


def get_points_list_from_dict(dictionary):
    return list(dictionary.values())


def get_points_list_from_result_list(dictionary):
    locations_list = []

    for elem in list(dictionary.values())[0]:
        locations_list.append(Location(elem['latitude'], elem['longitude'], elem['elevation'], elem['name']))

    return locations_list

def load_json(path):
    with open(path) as file:
        return json.load(file)


def get_couples_list_from_json(path='../resources/points_list.json'):
    data = get_points_list_from_result_list(load_json(path))

    return create_point_and_antipodal_couple(data)


# todo: use reverse geocoding to get the name of the found coordinates
def create_point_and_antipodal_couple(locations_list):
    couples_list = []

    for location in locations_list:
        antipodal = find_antipodal_point(location)
        couple = Couple(location, antipodal)
        if location.name is None:
            couple.name = f'{couple.point.get_coordinates} to {couple.antipodal_point.get_coordinates()} distance'
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


# def set_elevation


# todo: add exception handling ?
def import_equatorial_points():
    URL = 'https://api.open-elevation.com/api/v1/lookup?locations='
    parameters = ''

    for i in range(0, 179):
        parameters += f'0,{i}|'
    parameters += '0,180'

    equator_points = requests.get(f'{URL}{parameters}').json()

    with open("../resources/points_list.json", "w") as outfile:
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