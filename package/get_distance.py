import json

from package.models import Couple, Location


def get_points_list_from_dict(dictionary):
    return list(dictionary.values())


def get_points_list_from_result_list(dictionary):
    locations_list = []

    for elem in list(dictionary.values())[0]:
        locations_list.append(
            Location(elem["latitude"], elem["longitude"], elem["elevation"])
        )

    return locations_list


def load_json(path):
    with open(path) as file:
        return json.load(file)


def get_couples_list_from_json(path="../resources/points_list.json"):
    data = get_points_list_from_result_list(load_json(path))

    return create_point_and_antipodal_couple(data)


def get_summits_max_elevation():
    return get_max_distance_from_couples_list(
        get_couples_list_from_json("../resources/seven_summits.json")
    )


# todo: use reverse geocoding to get the name of the found coordinates
def create_point_and_antipodal_couple(locations_list):
    couples_list = []

    for location in locations_list:
        antipodal = find_antipodal_point(location)
        couple = Couple(location, antipodal)
        name_distance(couple, location)
        couples_list.append(couple)

    return couples_list


def name_distance(couple, location):
    if location.name is None:
        couple.name = f"{couple.point.get_coordinates()} to {couple.antipodal_point.get_coordinates()} distance"
    else:
        couple.name = f"{location.name} to its antipodal point distance"


def find_antipodal_point(location):
    if location.longitude > 0:
        longitude = 180 - location.longitude
    else:
        longitude = 180 - abs(location.longitude)
        longitude = -longitude

    return Location(-location.latitude, -longitude)


def get_max_distance_from_couples_list(couples_list):
    max_distance = 0
    i = -1

    for couple in couples_list:
        distance = couple.return_distance()
        if distance > max_distance:
            max_distance = couple.return_distance()
            i = couples_list.index(couple)

    return couples_list[i]


# todo: write a reverse geocoding function to print the name of the place that's found with the algorithm


def find_max_diameter():
    max_summit_elevation = get_summits_max_elevation().return_distance()
    couples_list = get_couples_list_from_json() + get_couples_list_from_json(
        "../resources/seven_summits.json"
    )

    for elem in couples_list:
        if elem.point.elevation == 0 and elem.antipodal_point.elevation == 0:
            couples_list.remove(elem)
        elif elem.return_distance() < max_summit_elevation:
            couples_list.remove(elem)
        else:
            name_distance(elem, elem.point)

    return get_max_distance_from_couples_list(couples_list)


# import_all_points_as_json()
max_distance_couple = find_max_diameter()
print(
    f"\nThe maximum distance found from the diameters created from the given list is "
    f"{max_distance_couple.return_distance() / 1000} km. \nIt is the distance from {max_distance_couple.name}"
)
