import json, requests


class Location:
    def __init__(self, lati, long, name='', elev=0):
        self.name = name
        self.coordinates = (lati, long)
        self.elevation = elev

    def set_elevation(self, elevation):
        self.elevation = elevation


def get_capitals_list(dict):
    return list(dict.values())


def get_points_list_from_file(path='points_list.json'):
    with open(path) as file:
        return json.load(file)


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
        diameters.append((f'{elem.name} <-> {antipodals[i].name} Distance', diameter))

    return diameters


def find_antipodal_point(coordinates):
    latitude = coordinates[0]

    if coordinates[1] > 0:
        longitude = 180 - coordinates[1]
    else:
        longitude = 180 - abs(coordinates[1])
        longitude = -longitude

    return -latitude, -longitude


# todo: make it so that get_elevation only sends one request for any given list of coordinates

def get_elevation(coordinates):
    response = requests.get(
        f'https://api.open-elevation.com/api/v1/lookup?locations={coordinates[0]},{coordinates[1]}').json()

    return response['results'][0]['elevation']


def import_equatorial_points():
    URL = 'https://api.open-elevation.com/api/v1/lookup?locations='
    parameters = ''

    for i in range(0, 179):
        parameters += f'0,{i}|'
    parameters += '0,180'

    equator_points = requests.get(f'{URL}{parameters}').json()

    with open("points_list.json", "w") as outfile:
        json.dump(equator_points, outfile)

    #todo: add exception handling ?

    return True

# earth_diameter is about 12742 km
def diameter_calculation(elevation_a, elevation_b, earth_diameter=12742000):
    elevation_difference = elevation_a + elevation_b

    return earth_diameter + elevation_difference


def find_max_distance(diameters_list):
    max_distance = 0
    i = -1

    for elem in diameters_list:
        if elem[1] > max_distance:
            max_distance = elem[1]
            i = diameters_list.index(elem)

    return diameters_list[i]
