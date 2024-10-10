import json, requests
from random import random
from time import sleep

from requests import Request


def get_elevation(location):
    response = requests.get(
        f'https://api.open-elevation.com/api/v1/lookup?locations={location.latitude},{location.longitude}'
    ).json()

    return response['results'][0]['elevation']


# todo: add exception handling ?
def get_all_points_as_json(pace):
    URL = 'https://api.open-elevation.com/api/v1/lookup?locations='
    json_coordinates = []

    with open('../resources/points_list.json', 'w') as file:
        file.write("")

    for i in range(0, 90, pace):
        parameters = ''
        for j in range(0, 180, pace):
            parameters += f'{i},{j}|'
        request = requests.get(f'{URL}{parameters}')
        # print(request.status_code)
        response = request.json()
        json_coordinates += response['results']
        with open('../resources/points_list.json', 'a') as file:
            file.write(f'{"{"}"results": ')
            json.dump(json_coordinates, file)
            file.write(f'{"}"}')
        sleep(1)


def generate_mock_elevation_data_as_json():

    dict_list = []

    test_obj = {
            "longitude": 10,
            "latitude": 10,
            "elevation": 10
        }

    dict_list.append(test_obj)

    for lat in range(0, 90, 1):
        for long in range(0, 180, 1):
            elev = random()*1000
            coordinates = [(lat, long, elev)]
            dict_list.append ({k: v for e in coordinates for k, v in zip(("longitude", "latitude", "elevation"), e)})

    result = {"results": dict_list}
    json_obj = json.dumps(result, indent = 4)

    with open("../resources/mock_data.json", "w") as outfile:
        outfile.write(json_obj)
