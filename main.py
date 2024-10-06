import get_distance

locations_list = get_distance.create_locations_list()
antipodal_list = get_distance.find_antipodal_points(locations_list)
diameters_list = get_distance.create_diameters_list(locations_list, antipodal_list)
max_diameter = get_distance.find_max_distance(diameters_list)
print(f'The biggest diameter from the list is {max_diameter[0]} of {max_diameter[1]} kms')