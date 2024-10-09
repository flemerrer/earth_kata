import pytest

from package.get_distance import find_max_distance, find_antipodal_point, get_elevation, Location, Couple, \
    get_couples_list_from_json, \
    get_points_list_from_dict, create_point_and_antipodal_couple


# Reminder about tests : they must be simple to avoid them being false / wrong, and because they are a form of documentation. They must show how functions work ; not be another implementation of tested functions. If they have the same complexity level as the tested function, it is not right.
# To help achieving that, use hard coded values in test. And like in any docu!entation, choose values to test that are not abstract. It facilitates comprehension (Alice and Bob > A & B)


# @pytest.mark.parametrize({"couple", "expected_distance"},
#                          [
#                              {Couple(Location(10, 10, 515), Location(-10, -170)), 12742515},
#                              {Couple(Location(-20, -20, 545), Location(20, 160)), 12742545},
#                          ])
def test_diameter_calculation_should_return_the_distance_between_two_points():
    couple = Couple(Location(10, 10, 515), Location(-10, -170))
    expected_distance = 12742515

    assert couple.return_distance() == expected_distance


def test_find_max_distance_should_return_the_greatest_value_from_distances_listed_in_test_file():

    couple = find_max_distance(get_couples_list_from_json('../resources/seven_summits.json'))

    assert couple.name is not None
    assert couple.return_distance() == 12750771.0

@pytest.mark.parametrize({"given_location", "expected_antipodal"},
                         [
                             {Location(40, -5), Location(-40, 175)},
                             {Location(49, 7), Location(-49, -173)},
                             {Location(-32, 52), Location(32, -128)},
                             {Location(75, 140), Location(-75, -40)},
                             {Location(-25, -50), Location(25, 130)},
                         ])
def test_find_antipodal_point_should_return_the_antipodal_point_coordinates(given_location, expected_antipodal):

    assert find_antipodal_point(given_location).latitude == expected_antipodal.latitude
    assert find_antipodal_point(given_location).longitude == expected_antipodal.longitude


# pay attention and insert a backspace after a comma while listing ints ; if not, it'll be considered as one float !
# avoid calling APIs during test > prefer the use of mocks

# @pytest.mark.parametrize({"given_latitude", "given_longitude", "expected_elevation"},
#                          [
#                              pytest.param(10, 10, 515),
#                              pytest.param(20, 20, 545),
#                          ])
# def test_get_elevation(given_latitude, given_longitude, expected_elevation):
#     coordinates = (given_latitude, given_longitude)
#     elevation = get_elevation(coordinates)
#
#     assert elevation == expected_elevation

#@requests_mock.Mocker()
def test_get_elevation_should_return_a_valid_json(mocker):
    test_coordinates = Location(10, 10)
    test_data = {"results":[{"latitude":10.0,"longitude":10.0,"elevation":515.0}]}

    mock_response = mocker.MagicMock()
    mock_response.json.return_value = test_data

    mocker.patch("requests.get", return_value=mock_response)

    # version that tests the whole data response
    # assert result == test_data
    # assert type(result) == dict
    # assert result["results"][0]["elevation"] == 515

    assert get_elevation(test_coordinates) == 515

def test_find_antipodal_points_should_return_a_list_of_opposite_locations():
    paris = Location(49, 2, 0, 'Paris')
    camberra = Location(-35, 149, 0, 'Canberra')
    lima = Location(-12, -77, 0, 'Lima')
    locations_list = (paris, camberra, lima)

    couples_list = create_point_and_antipodal_couple(locations_list)

    assert couples_list[0].antipodal_point.get_coordinates() == (-49, -178)
    assert couples_list[1].antipodal_point.get_coordinates() == (35, -31)
    assert couples_list[2].antipodal_point.get_coordinates() == (12, 103)


capitals_coordinates = {
    'Paris': Location(49, 2, 182, 'Paris'),
    'London': Location(51, -0, 0, 'London'),
    'New York': Location(41, -74, 0, 'New York'),
    'Mexico': Location(19, -99, 0, 'Mexico'),
    'Rio de Janeiro': Location(-23, -43, 0, 'Rio de Janeiro'),
    'Lima': Location(-12, -77, 221, 'Lima'),
    'New Delhi': Location(28, 77, 0, 'New Delhi'),
    'Beijing': Location(22, 113, 0, 'Beijin'),
    'Canberra': Location(-35, 149, 0,'Canberra'),
}


def test_create_point_and_antipodal_couples_should_return_a_list_of_couple_instances_containing_two_locations_with_names():

    locations_list = get_points_list_from_dict(capitals_coordinates)
    expected_name_1 = locations_list[0].name
    expected_name_2 = locations_list[8].name
    couples_list = create_point_and_antipodal_couple(locations_list)

    assert couples_list[0].point.name == expected_name_1
    assert couples_list[0].name == f'{expected_name_1} to its antipodal point distance'
    assert couples_list[8].point.name == expected_name_2
    assert couples_list[8].name == f'{expected_name_2} to its antipodal point distance'


def test_get_couples_list_from_json_should_return_a_list_of_couple_objects():
    result = get_couples_list_from_json('../resources/seven_summits.json')

    assert isinstance(result[1], Couple)
    assert isinstance(result[1].point, Location)
