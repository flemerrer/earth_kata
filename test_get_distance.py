from pdb import find_function

import pytest

from get_distance import two_points_distance_calculation, find_max_distance, find_antipodal_point


def test_two_points_distance_calculation_should_return_the_distance_between_two_points():
    position1 = (40, -5, 100)
    position2 = (-40, 175, -50)

    distance = two_points_distance_calculation(position1, position2)

    assert distance == 12792


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
def test_find_opposite_point_should_return_the_antipodal_point_coordinates_of_given_point_coordinates(given_coordinates, expected_coordinates):
    result_coordinates = find_antipodal_point(given_coordinates)

    assert result_coordinates == expected_coordinates

def test_get_altitude():
    pass

