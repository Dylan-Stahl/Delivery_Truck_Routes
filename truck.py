from data_loader import package_hash
from hash_table_chaining import ChainingHashTable

truck_hash = ChainingHashTable(4)


def load_trucks():
    # do a loop using hash search method
    truck_one = []
    truck_two = []
    truck_three = []

    # i represents number of packages
    i = 0
    for package in package_hash.table:
        i = i + 1

    # iterator for number of packages on truck one
    j = 0

    # iterator for number of packages on truck two
    d = 0

    # iterator for number of packages on truck three
    f = 0

    # iterator for iterating i times
    c = 0

    # first while loop inserts packages that have special requirements, like being with other packages, must be on
    # truck two, if the package is delayed, and if the package must be delivered before the end of the day
    while c <= i:
        packaged_being_loaded = package_hash.search(c)
        if packaged_being_loaded is not None:
            # packaged 13, 15, and 19 must be shipped together. These packages do not have to be delivered
            # before the end of the day so they will be added to truck one
            if packaged_being_loaded.id == 13 or packaged_being_loaded.id == 14 or packaged_being_loaded.id == 15 or \
                    packaged_being_loaded.id == 16 or packaged_being_loaded.id == 19 or packaged_being_loaded.id == 20:
                j = j + 1
                truck_one.append(package_hash.search(c))
                package_hash.search(c).number_on_truck = c

            # if the package must be on truck two, that package is added to truck two
            if packaged_being_loaded.package_notes == 'Can only be on truck 2' and d < 16:
                d = d + 1
                truck_two.append(package_hash.search(c))
                package_hash.search(c).number_on_truck = c

            if packaged_being_loaded.package_notes == 'Wrong address listed' and f < 16:
                f = f + 1
                truck_three.append(package_hash.search(c))
                package_hash.search(c).number_on_truck = c

            if packaged_being_loaded.package_notes.startswith('Delayed') and f < 16:
                f = f + 1
                truck_three.append(package_hash.search(c))
                package_hash.search(c).number_on_truck = c

            # if the package has no special notes and has to be delivered before the end of the day, they are added
            # to trucks 1 and 2. By using the iterator the packages are alternated between loading on truck 1 and 2.
            if packaged_being_loaded.package_notes == 'None' and packaged_being_loaded.deadline != 'EOD' and packaged_being_loaded.number_on_truck != c:
                # First two trucks will be leaving the depot first. They will have the packages loaded on them that have
                # Delivery deadlines before the end of the day.
                if c % 2 == 0 and j < 16:
                    j = j + 1
                    truck_one.append(package_hash.search(c))
                    package_hash.search(c).number_on_truck = c

                if c % 2 == 1 and d < 16:
                    d = d + 1
                    truck_two.append(package_hash.search(c))
                    package_hash.search(c).number_on_truck = c
        c = c + 1

    c = 0
    while c <= i:
        packaged_being_loaded = package_hash.search(c)
        if packaged_being_loaded is not None and packaged_being_loaded.number_on_truck != c:
            if c % 3 == 0 and j < 16:
                j = j + 1
                truck_one.append(package_hash.search(c))
                package_hash.search(c).number_on_truck = c

            if c % 3 == 1 and d < 16:
                d = d + 1
                truck_two.append(package_hash.search(c))
                package_hash.search(c).number_on_truck = c

            if c % 3 == 2 and f < 16:
                f = f + 1
                truck_three.append(packaged_being_loaded)
                packaged_being_loaded.number_on_truck = c
        c = c + 1

    # Create truck object
    truck_obj1 = Truck(1, truck_one, '8:00', '8:00')
    truck_obj2 = Truck(2, truck_two, '8:00', '8:00')
    truck_obj3 = Truck(3, truck_three, '9:00', '9:05')

    # Insert truck into truck hash table
    truck_hash.insert(1, truck_obj1)
    truck_hash.insert(2, truck_obj2)
    truck_hash.insert(3, truck_obj3)


class Truck:
    def __init__(self, id, packages, time, time_left_hub):
        self.package_array = []

        for package in packages:
            self.package_array.append(package)

        self.id = id
        self.time = time
        self.time_left_hub = time_left_hub

    def __str__(self):
        i = 1
        truck_string = 'Truck ' + str(self.id) + ':\n'
        truck_string = truck_string + 'Package '
        for package in self.package_array:
            if i == 1:
                truck_string += package.str() + '\n'
                i = i + 1
            else:
                truck_string += 'Package ' + package.str() + '\n'
                i = i + 1
        return truck_string
