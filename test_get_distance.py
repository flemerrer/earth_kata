import pytest

from get_distance import find_max_distance, find_antipodal_point, get_elevation, Location, \
    find_antipodal_points, create_diameters_list, get_capitals_list, Couple


# Reminder about tests : they must be simple to avoid them being false / wrong, and because they are a form of documentation. They must show how functions work ; not be another implementation of tested functions. If they have the same complexity level as the tested function, it is not right.
# To help achieving that, use hard coded values in test. And like in any docu!entation, choose values to test that are not abstract. It facilitates comprehension (Alice and Bob > A & B)


# @pytest.mark.parametrize({"location", "antipodal", "expected_distance"},
#                          [
#                              {location_a, antipodal_b, 12742515},
#                              {location_b, antipodal_b, 12742545},
#                          ])
def test_diameter_calculation_should_return_the_distance_between_two_points():
    location_1 = Location(10, 10, 515)
    antipodal_a = Location(-10, -170)
    location_2 = Location(-20, -20, 545)
    antipodal_b = Location(20, 160)

    couple_a = Couple(location_1, antipodal_a)
    couple_b = Couple(location_2, antipodal_b)

    assert couple_a.diameter_calculation() == 12742515
    assert couple_b.diameter_calculation() == 12742545


def test_find_max_distance_should_return_the_greatest_value_from_input_distances():
    distances = [
        ('distance 1', 1),
        ('distance 2', 2),
        ('distance 3', 10)
    ]

    result = find_max_distance(distances)

    assert result == ('distance 3', 10)


# @pytest.mark.parametrize({"given_locations", "expected_coordinates"},
#                          [
#                              {Location(40, -5), (-40, 175)},
#                              {Location(49, 7), (-49, -173)},
#                              {Location(-32, 52), (32, -128)},
#                              {Location(75, 140), (-75, -40)},
#                              {Location(-25, -50), (25, 130)},
#                          ])
def test_find_antipodal_point_should_return_the_antipodal_point_coordinates():
    location = Location(40, -5)

    assert find_antipodal_point(location) == (-40, 175)


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
    paris = Location(49, 2, 'Paris')
    camberra = Location(-35, 149, 'Canberra')
    lima = Location(-12, -77, 'Lima')
    locations = (paris, camberra, lima)

    antipodal_locations = find_antipodal_points(locations)

    assert antipodal_locations[0].get_coordinates() == (-49, -178)
    assert antipodal_locations[1].get_coordinates() == (35, -31)
    assert antipodal_locations[2].get_coordinates() == (12, 103)


# I started by coding a function that returned a list using a for loop on dictionary but I refactored it later
@pytest.mark.skip('now unnecessary')
def test_get_locations_list_should_return_a_list_of_location_from_dictionary():
    locations = get_capitals_list()

    assert locations[0].coordinates == (49, 2) and locations[0].name == 'Paris'


def test_create_diameters_list_should_return_a_list_of_tuples():
    capitals_coordinates = {
        'Paris': Location(49, 2, 182, 'Paris', ),
        'London': Location(51, -0, 0, 'London', ),
        'New York': Location(41, 0, -74, 'New York', ),
        'Mexico': Location(19, -99, 0, 'Mexico'),
        'Rio de Janeiro': Location(-23, -43, 0, 'Rio de Janeiro'),
        'Lima': Location(-12, -77, 221, 'Lima', ),
        'New Delhi': Location(28, 77, 0, 'New Delhi'),
        'Beijin': Location(22, 113, 0, 'Beijin'),
        'Canberra': Location(-35, 149, 0, 'Canberra'),
    }

    locations_list = get_capitals_list(capitals_coordinates)
    antipodal_list = find_antipodal_points(locations_list)

    diameters = create_diameters_list(locations_list, antipodal_list)

    assert diameters[0][0] == f'Paris <-> Opposite of Paris Distance'
    assert diameters[0][1] == 12742182
    assert diameters[5][0] == f'Lima <-> Opposite of Lima Distance'
    assert diameters[5][1] == 12742221

