import json, requests
import time


def get_elevation(location):
    response = requests.get(
        f"https://api.open-elevation.com/api/v1/lookup?locations={location.latitude},{location.longitude}"
    ).json()

    return response["results"][0]["elevation"]


# todo: add exception handling ?
def import_all_points_as_json():
    URL = "https://api.open-elevation.com/api/v1/lookup?locations="
    parameters = ""
    all_round_coordinates = ""

    for i in range(0, 90, 1):
        for j in range(0, 180, 1):
            parameters += f"{i},{j}|"
        all_round_coordinates += requests.get(f"{URL}{parameters}").text
        print(1)
        time.sleep(1)

    json_coordinates = json.loads(all_round_coordinates)

    with open("../resources/points_list.json", "w") as outfile:
        json.dump(json_coordinates, outfile)
