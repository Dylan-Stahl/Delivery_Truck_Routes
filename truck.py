from data_loader import package_hash
from hash_table_chaining import ChainingHashTable
import datetime

truck_hash = ChainingHashTable(4)


def load_trucks():
    # What i need to change:
    # packages that have the same location should be put on the same truck

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
            # packaged 13, 14, 15, 16, 19, and 20 must be shipped together. These packages do not have to be delivered
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
                d = d + 1
                truck_two.append(package_hash.search(c))
                package_hash.search(c).number_on_truck = c

            # if the package has no special notes and has to be delivered before the end of the day, they are added
            # to trucks 1 and 2. By using the iterator the packages are alternated between loading on truck 1 and 2.
            if packaged_being_loaded.package_notes == 'None' and packaged_being_loaded.deadline != 'EOD' and packaged_being_loaded.number_on_truck != c:
                # First two trucks will be leaving the depot first. They will have the packages loaded on them that have
                # Delivery deadlines before the end of the day.

                # NEW IDEA: loop through packages on all trucks, if a truck is visiting the location that the package is being
                # delivered to, add that package to the truck

                for package in truck_two:
                    if packaged_being_loaded is not None:
                        if packaged_being_loaded.address == package.address and packaged_being_loaded.number_on_truck != c:
                            if d < 16:
                                d = d + 1
                                truck_two.append(packaged_being_loaded)
                                packaged_being_loaded.number_on_truck = c

                for package in truck_one:
                    if packaged_being_loaded is not None:
                        if packaged_being_loaded.address == package.address and packaged_being_loaded.number_on_truck != c:
                            if j < 16:
                                j = j + 1
                                truck_one.append(packaged_being_loaded)
                                packaged_being_loaded.number_on_truck = c

                if c % 2 == 0 and j < 16 and packaged_being_loaded.number_on_truck != c:
                    j = j + 1
                    truck_one.append(package_hash.search(c))
                    package_hash.search(c).number_on_truck = c

                if c % 2 == 1 and d < 16 and packaged_being_loaded.number_on_truck != c:
                    d = d + 1
                    truck_two.append(package_hash.search(c))
                    package_hash.search(c).number_on_truck = c
        c = c + 1

    # This while loop loads the packages that do not have special conditions
    # For each location, create a list with all the packages going there
    # loop through all package address, for every time there is 1 occurence of an address,
    # loop through all key and values, if there is more than 1 value that is the same, obtain the keys and do a
    # package _hash.search(key). Add those packages to a list and when adding packages loop through that list and add
    # packages to same truck

    # create two lists, one with packages that don't share addreses, and one that shares addresses
    # holds address
    packages_with_different_addresses = []
    # holds package object
    packages_different_address = []

    # holds address
    packages_with_same_addresses = []
    # holds package object
    packages_same_address = []

    c = 0
    while c <= i:
        packaged_being_loaded = package_hash.search(c)

        # NEW IDEA: loop through packages on all trucks, if a truck is visiting the location that the package is being
        # delivered to, add that package to the truck

        for package in truck_two:
            if packaged_being_loaded is not None:
                if packaged_being_loaded.address == package.address and packaged_being_loaded.number_on_truck != c:
                    if d < 16:
                        d = d + 1
                        truck_two.append(packaged_being_loaded)
                        packaged_being_loaded.number_on_truck = c

        for package in truck_one:
            if packaged_being_loaded is not None:
                if packaged_being_loaded.address == package.address and packaged_being_loaded.number_on_truck != c:
                    if j < 16:
                        j = j + 1
                        truck_one.append(packaged_being_loaded)
                        packaged_being_loaded.number_on_truck = c

        for package in truck_three:
            if packaged_being_loaded is not None:
                if packaged_being_loaded.address == package.address and packaged_being_loaded.number_on_truck != c:
                    if f < 16:
                        f = f + 1
                        truck_three.append(packaged_being_loaded)
                        packaged_being_loaded.number_on_truck = c

        # won't add packages that have already been added to truck by using 'and
        # packaged_being_loaded.number_on_truck != c'
        if packaged_being_loaded is not None and packaged_being_loaded.number_on_truck != c:
            if packaged_being_loaded.address not in packages_with_different_addresses:
                packages_with_different_addresses.append(packaged_being_loaded.address)
                packages_different_address.append(packaged_being_loaded)
                packaged_being_loaded.number_on_truck = c
            else:
                packages_with_same_addresses.append(packaged_being_loaded.address)
                packages_same_address.append(packaged_being_loaded)
                packaged_being_loaded.number_on_truck = c

        c = c + 1

    # want to keep packages with the same addresses on the same truck, lets use truck one if its not full and then
    # use truck 2 and 3 as backups
    c = 0
    for package in packages_same_address:
        if f < 16 and package.number_on_truck != c:
            f = f + 1
            truck_three.append(package)
            package.number_on_truck = c
        elif d < 16 and package.number_on_truck != c:
            d = d + 1
            truck_two.append(package)
            package.number_on_truck = c
        elif j < 16 and package.number_on_truck != c:
            j = j + 1
            truck_one.append(package)
            package.number_on_truck = c
        c = c + 1

    c = 0
    for package in packages_different_address:
        for package_on_truck_one in truck_one:
            if package.address == package_on_truck_one.address and package.number_on_truck != c:
                if j < 16:
                    j = j + 1
                    truck_one.append(package)
                    package.number_on_truck = c

        for package_on_truck_two in truck_two:
            if package.address == package_on_truck_two.address and package.number_on_truck != c:
                if d < 12:
                    d = d + 1
                    truck_two.append(package)
                    package.number_on_truck = c

        for package_on_truck_three in truck_three:
            if package.address == package_on_truck_three.address and package.number_on_truck != c:
                if f < 16:
                    f = f + 1
                    truck_three.append(package)
                    package.number_on_truck = c

        if package.number_on_truck != c:
            if f < 16:
                f = f + 1
                truck_three.append(package)
                package.number_on_truck = c
            elif j < 16:
                j = j + 1
                truck_one.append(package)
                package.number_on_truck = c

            elif d < 16:
                d = d + 1
                truck_two.append(package)
                package.number_on_truck = c

        c = c + 1

    # Create truck object
    date = datetime.date.today()

    truck_obj1 = Truck(1, truck_one, datetime.datetime(date.year, date.month, date.day, 8, 0, 0),
                       datetime.datetime(date.year, date.month, date.day, 8, 0, 0))
    truck_obj2 = Truck(2, truck_two, datetime.datetime(date.year, date.month, date.day, 9, 5, 0),
                       datetime.datetime(date.year, date.month, date.day, 9, 5, 0))
    truck_obj3 = Truck(3, truck_three, datetime.datetime(date.year, date.month, date.day, 9, 45, 20),
                       datetime.datetime(date.year, date.month, date.day, 9, 45, 20))

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
        truck_string = 'Truck ' + str(self.id) + ', Time left hub: ' + str(
            self.time_left_hub) + ', Time truck completed route: ' + str(self.time) + ':\n'
        truck_string = truck_string + 'Package '
        for package in self.package_array:
            if i == 1:
                truck_string += package.str() + '\n'
                i = i + 1
            else:
                truck_string += 'Package ' + package.str() + '\n'
                i = i + 1
        return truck_string
