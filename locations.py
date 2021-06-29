# Stores the location id, location name, and location address for each location in the locations.csv file.
class Location:
    def __init__(self, location_id, location_name, location_address):
        self.location_id = location_id
        self.location_name = location_name
        self.location_address = location_address