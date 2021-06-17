from data_loader import package_hash
from hash_table_chaining import ChainingHashTable

truck_hash = ChainingHashTable(3)


def load_trucks():
    # do a loop using hash search method
    truck_one = []
    truck_two = []
    truck_three = []

    i = 0
    for package in package_hash.table:
        i = i + 1

    while i > 0:
        if package_hash.search(i) is not None:
            truck_one.append(package_hash.search(i))
        i = i - 1

    # Create truck object
    truck_obj = Truck(truck_one, '8:00', '9:00')

    # Insert truck into truck hash table
    truck_hash.insert(0, truck_obj)



class Truck:
    def __init__(self, packages, time, time_left_hub):
        self.package_array = []

        for package in packages:
            self.package_array.append(package)

        self.time = time
        self.time_left_hub = time_left_hub

    def __str__(self):
        i = 1
        truck_string = 'Package ' + str(i) + ' = '
        for package in self.package_array:
            if i == 1:
                truck_string += package.str() + '\n'
                i = i + 1
            else:
                truck_string += 'Package ' + str(i) + ' = ' + package.str() + '\n'
                i = i + 1
        return truck_string
