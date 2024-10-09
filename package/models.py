class Location:
    def __init__(self, lati, long, elev=0, name=None):
        self.name = name
        self.latitude = lati
        self.longitude = long
        self.elevation = elev

    def get_coordinates(self):
        return self.latitude, self.longitude

    def set_elevation(self, elevation):
        self.elevation = elevation


class Couple:
    def __init__(self, point_a, point_b):
        self.point: Location = point_a
        self.antipodal_point: Location = point_b
        self.name = None

    # earth_diameter is about 12742 km
    def return_distance(self):
        # print()
        return 12742000 + self.point.elevation + self.antipodal_point.elevation