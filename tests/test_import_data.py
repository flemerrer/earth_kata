import pytest

from package.get_distance import load_json
from package.import_data import get_elevation, generate_mock_elevation_data_as_json, get_all_points_as_json
from package.models import Location


# avoid calling APIs during test > prefer the use of mocks
@pytest.mark.skip
@pytest.mark.parametrize({"given_location", "expected_elevation"},
                         [
                             pytest.param(Location(10, 10), 515),
                             pytest.param(Location(20, 20), 545),
                         ])
def test_get_elevation(given_location, expected_elevation):
    coordinates = (given_location)
    elevation = get_elevation(coordinates)

    assert elevation == expected_elevation


# @requests_mock.Mocker()
def test_get_elevation_should_return_a_valid_json(mocker):
    test_coordinates = Location(10, 10)
    test_data = {"results": [{"latitude": 10.0, "longitude": 10.0, "elevation": 515.0}]}

    mock_response = mocker.MagicMock()
    mock_response.json.return_value = test_data

    mocker.patch("requests.get", return_value=mock_response)

    # version that tests the whole data response
    # assert result == test_data
    # assert type(result) == dict
    # assert result["results"][0]["elevation"] == 515

    assert get_elevation(test_coordinates) == 515

def test_import_mock_elevation_data_as_json_should_return_a_structured_json_file():

    generate_mock_elevation_data_as_json()

    data = load_json('../resources/mock_data.json')

    assert list(data.values())[0][0] == {'longitude': 10, 'latitude': 10, 'elevation': 10}


def test_get_all_points_as_json_should_return_a_list_of_coordinates_and_respective_elevation_as_json():

    # pace is specified as 1 for now (so coordinates should go from 0,1 to 0,2 and forward up to 90, 180)
    get_all_points_as_json(1)

    data = load_json('../resources/mock_data.json')

    assert list(data.values())[0][0] == {'longitude': 0, 'latitude': 0, 'elevation': 0}