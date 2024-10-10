import json, requests
from random import random


def get_elevation(location):
    response = requests.get(
        f'https://api.open-elevation.com/api/v1/lookup?locations={location.latitude},{location.longitude}'
    ).json()

    return response['results'][0]['elevation']


# todo: add exception handling ?
# fixme: doesn't work for now
def get_all_points_as_json():
    URL = 'https://api.open-elevation.com/api/v1/lookup?locations='
    temp_data =''

    for i in range(0, 90, 1):
        parameters = ''
        for j in range(0, 180, 1):
            parameters += f'{i},{j}|'
        print(parameters)
        request = requests.get(f'{URL}{parameters}')
        print(request.status_code)
        temp_data += request.text
        print(temp_data)

    json_coordinates = json.loads(temp_data.text)

    with open('../resources/points_list.json', 'a') as file:
        json.dump(json_coordinates, file)

def import_mock_elevation_data_as_json():

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

    # for i in range(0, 90, 1):
    #     for j in range(0, 180, 1):
    #         parameters += f'{"{"}"latitude":{i}, "longitude":{j}, "elevation": {random()*1000}{"}"},'
    #
    # data += f'{parameters}]{"}"}'

    # with open('../resources/mock_data.json', 'w') as file:
    #     json.dump(json, file, indent=4, sort_keys=True)

import_mock_elevation_data_as_json()