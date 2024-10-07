import get_distance
from get_distance import get_capitals_list

capitals_coordinates = {
    'Paris': get_distance.Location(49, 2, 'Paris', 182),
    'London': get_distance.Location(51, -0, 'London', ),
    'New York': get_distance.Location(41, -74, 'New York', ),
    'Mexico': get_distance.Location(19, -99, 'Mexico', ),
    'Rio de Janeiro': get_distance.Location(-23, -43, 'Rio de Janeiro'),
    'Lima': get_distance.Location(-12, -77, 'Lima', 221),
    'New Delhi': get_distance.Location(28, 77, 'New Delhi'),
    'Beijin': get_distance.Location(22, 113, 'Beijin'),
    'Canberra': get_distance.Location(-35, 149, 'Canberra'),
}

locations_list = get_capitals_list(capitals_coordinates)
antipodal_list = get_distance.find_antipodal_points(locations_list)
diameters_list = get_distance.create_diameters_list(locations_list, antipodal_list)
max_diameter = get_distance.find_max_distance(diameters_list)
print(f'The biggest diameter from the list is "{max_diameter[0]}" ({max_diameter[1]} m)')