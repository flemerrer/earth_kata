from get_distance import two_points_distance_calculation, find_max_distance


def test_two_points_distance_calculation_should_return_the_hypotenuse_value_of_x_y_rectangle_triangle():
    position1 = (30, 50)
    position2 = (40, 60)

    result = two_points_distance_calculation(position1, position2)

    assert round(result, 3) == round(14.1421, 3)
    
def test_find_max_distance_should_return_the_greatest_value_from_input_distances():
    distances = (14.142, 56.987, 100.265, 5.120)

    result = find_max_distance(distances)

    assert result == 100.256