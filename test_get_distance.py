import pytest

from get_distance import diameter_calculation, find_max_distance, find_antipodal_point, get_elevation, Location, \
    find_antipodal_points, create_locations_list, create_diameters_list


def test_diameter_calculation_should_return_the_distance_between_two_points():
    elevation1 = 100
    elevation2 = -50

    distance = diameter_calculation(elevation1, elevation2)

    assert distance == 12742050


def test_find_max_distance_should_return_the_greatest_value_from_input_distances():
    distances = (14.142, 56.987, 100.256, 5.120)

    result = find_max_distance(distances)

    assert result == 100.256


@pytest.mark.parametrize({"given_coordinates", "expected_coordinates"},
                         [
                             {(40, -5), (-40, 175)},
                             {(49, 7), (-49, -173)},
                             {(-32, 52), (32, -128)},
                             {(75, 140), (-75, -40)},
                             {(-25, -50), (25, 130)},
                         ])
def test_find_opposite_point_should_return_the_antipodal_point_coordinates_of_given_point_coordinates(given_coordinates,
                                                                                                      expected_coordinates):
    result_coordinates = find_antipodal_point(given_coordinates)

    assert result_coordinates == expected_coordinates


# pay attention and insert a backspace after a comma while listing ints ; if not, it'll be considered as one float !

@pytest.mark.parametrize({"given_latitude", "given_longitude", "expected_elevation"},
                         [
                             pytest.param(10, 10, 515),
                             pytest.param(20, 20, 545),
                         ])
def test_get_elevation(given_latitude, given_longitude, expected_elevation):
    coordinates = (given_latitude, given_longitude)
    elevation = get_elevation(coordinates)

    assert elevation == expected_elevation

def test_find_antipodal_points_should_return_a_list_of_opposite_locations():
    paris = Location (49, 2, 'Paris')
    camberra = Location(-35, 149, 'Canberra')
    lima = Location(-12, -77, 'Lima')
    locations = (paris, camberra, lima)

    antipodal_locations = find_antipodal_points(locations)

    assert antipodal_locations[0].coordinates == (-49, -178)
    assert antipodal_locations[1].coordinates == (35, -31)
    assert antipodal_locations[2].coordinates == (12, 103)


def test_createlocations_list_should_return_a_list_of_location_from_dictionnary():
    list = create_locations_list()

    assert list[0].coordinates == (49, 2) and list[0].name == 'Paris'


def test_create_diameters_list_should_return_a_list_of_tuples():
    locations_list = create_locations_list()
    antipodal_list = find_antipodal_points(locations_list)

    diameters = create_diameters_list(locations_list, antipodal_list)

    for elem in diameters:
        index = diameters.index(elem)
        assert elem[0] == f'{locations_list[index].name} - {antipodal_list[index].name} Distance' and elem[1] == 12742000