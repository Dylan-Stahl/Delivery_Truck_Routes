from data_loader import load_locations
from nearest_neighbor import nearest_neighbor
from packages import package_hash
from hash_table_chaining import ChainingHashTable
import datetime

# Hash table that holds each truck
truck_hash = ChainingHashTable(4)


# Algorithm that sorts all the packages in the package hash into trucks so that nearest neighbor will be more efficient
def load_trucks():
    truck_one = []
    truck_two = []
    truck_three = []
    indice_array = []

    # i will represent number of packages
    i = 0
    for package in range(len(package_hash.table)):
        if package_hash.search(package) is not None:
            i = i + 1
            indice_array.append(package_hash.search(package).id)
            # -1 indicates that the package was not yet put on a truck
            package_hash.search(package).number_on_truck = -1

    # iterator for number of packages on truck one
    j = 0

    # iterator for number of packages on truck two
    d = 0

    # iterator for number of packages on truck three
    f = 0

    # iterator for iterating i times
    c = 0

    # The first for loop inserts packages that have special requirements, like being with other packages, must be on
    # truck two, if the package is delayed, and if the package must be delivered before the end of the day
    for package_id in indice_array:
        packaged_being_loaded = package_hash.search(package_id)
        if packaged_being_loaded is not None:
            # packaged 13, 14, 15, 16, 19, and 20 must be shipped together. Some of these packages have early deadlines
            # so they will be loaded onto truck one.
            if packaged_being_loaded.id == 13 or packaged_being_loaded.id == 14 or packaged_being_loaded.id == 15 or \
                    packaged_being_loaded.id == 16 or packaged_being_loaded.id == 19 or packaged_being_loaded.id == 20:
                j = j + 1
                truck_one.append(packaged_being_loaded)
                packaged_being_loaded.number_on_truck = c

            # If the package must be on truck two, that package is added to truck two.
            if packaged_being_loaded.package_notes == 'Can only be on truck 2' and d < 16:
                d = d + 1
                truck_two.append(packaged_being_loaded)
                packaged_being_loaded.number_on_truck = c

            # Truck three has packages that are being delivered last, since package 9's address is being updated at
            # 10:20 it is placed on truck three.
            if packaged_being_loaded.package_notes == 'Wrong address listed' and f < 16:
                f = f + 1
                truck_three.append(packaged_being_loaded)
                packaged_being_loaded.number_on_truck = c

            # Truck two leaves at 9:05 and will have all the delayed packages on it.
            if packaged_being_loaded.package_notes.startswith('Delayed') and f < 16:
                d = d + 1
                truck_two.append(packaged_being_loaded)
                packaged_being_loaded.number_on_truck = c

            # If the package has no special notes and has to be delivered before the end of the day, they are added
            # to trucks 1 and 2. By using the iterator the packages are alternated between loading on truck 1 and 2.
            if packaged_being_loaded.package_notes == 'None' and packaged_being_loaded.deadline != 'EOD' and packaged_being_loaded.number_on_truck != c:
                # NEW IDEA: loop through packages on all trucks, if a truck is visiting the location that the package is being
                # delivered to, add that package to the truck
                # Trucks 1 and 2 are leaving early enough that they can deliver packages that have early deadlines

                # If a package that is already loaded onto truck two has the same address as the package being loaded
                # currently, the the current package is placed on that truck so the trucks will have less locations
                # to visit.
                for package in truck_two:
                    if packaged_being_loaded is not None:
                        if packaged_being_loaded.address == package.address and packaged_being_loaded.number_on_truck != c:
                            if d < 16:
                                d = d + 1
                                truck_two.append(packaged_being_loaded)
                                packaged_being_loaded.number_on_truck = c

                # If a package that is already loaded onto truck one has the same address as the package being loaded
                # currently, the the current package is placed on that truck so the trucks will have less locations
                # to visit.
                for package in truck_one:
                    if packaged_being_loaded is not None:
                        if packaged_being_loaded.address == package.address and packaged_being_loaded.number_on_truck != c:
                            if j < 16:
                                j = j + 1
                                truck_one.append(packaged_being_loaded)
                                packaged_being_loaded.number_on_truck = c

                # If the package was not loaded already, the iterator modulus of 2 determines if it loaded onto truck
                # one or truck two unless that truck is already full.
                if c % 2 == 0 and j < 16 and packaged_being_loaded.number_on_truck != c:
                    j = j + 1
                    truck_one.append(packaged_being_loaded)
                    packaged_being_loaded.number_on_truck = c

                if c % 2 == 1 and d < 16 and packaged_being_loaded.number_on_truck != c:
                    d = d + 1
                    truck_two.append(packaged_being_loaded)
                    packaged_being_loaded.number_on_truck = c
            c = c + 1

    # This next part of the algorithm adds packages that do not have special requirements
    # Packages will loaded onto trucks that already are going to the same delivery location.
    # If the location is not being traveled to already, it is added to a list, packages_with_different_addresses, that
    # holds unique addresses. If an address needs to be added but is already in packages_with_different_addresses, it
    # is added to packages_with_same_addresses.

    # holds address
    packages_with_different_addresses = []
    # holds package object
    packages_different_address = []

    # holds address
    packages_with_same_addresses = []
    # holds package object
    packages_same_address = []

    # Iterator that determines number on truck and ensures packages do get get loaded twice
    c = 0
    for package_id in indice_array:
        packaged_being_loaded = package_hash.search(package_id)
        if packaged_being_loaded is not None:

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

    # want to keep packages with the same addresses on the same truck, lets use truck three if its not full and then
    # use truck 2 and 1 as backups
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
        # These three for loops try to add the package to a truck where the address is already being visited.

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

        # If no trucks are visiting the package's address, the package will be loaded onto truck three if not full.
        # If truck 3 is full, truck 1, if truck 1 is full, truck 2.
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

    # Truck 1 leaves at 8:00
    truck_obj1 = Truck(1, truck_one, datetime.datetime(date.year, date.month, date.day, 8, 0, 0),
                       datetime.datetime(date.year, date.month, date.day, 8, 0, 0))
    # Truck 2 leaves at 9:05
    truck_obj2 = Truck(2, truck_two, datetime.datetime(date.year, date.month, date.day, 9, 5, 0),
                       datetime.datetime(date.year, date.month, date.day, 9, 5, 0))
    # Truck 3 leaves at 9:43:40, when truck 1 returns with the original list
    truck_obj3 = Truck(3, truck_three, datetime.datetime(date.year, date.month, date.day, 9, 43, 40),
                       datetime.datetime(date.year, date.month, date.day, 9, 43, 40))

    # Insert truck into truck hash table
    truck_hash.insert(1, truck_obj1)
    truck_hash.insert(2, truck_obj2)
    truck_hash.insert(3, truck_obj3)

    # If different packages are used, truck 3's time left hub must be when truck 1 returns.
    set_truck_three_time_left_hub(truck_obj1)


# Sets the time in which truck three will leave the hub.
def set_truck_three_time_left_hub(truck_one):
    date = datetime.date.today()

    truck_one_graph = load_locations(truck_one)
    truck_one_graph.truck_graph.return_to_hub = True

    truck_one_path = nearest_neighbor(truck_one_graph.truck_graph,
                                      truck_one_graph.vertex_list[0],
                                      truck_one_graph.truck)
    truck_one_time_completion = truck_one.time
    truck_hash.search(3).time = truck_one_time_completion
    truck_hash.search(3).time_left_hub = truck_one_time_completion

    # Set truck one's time back to it's set leaving time, 8:00.
    truck_hash.search(1).time = datetime.datetime(date.year, date.month, date.day, 8, 0, 0)


# Truck class
class Truck:
    def __init__(self, id, packages, time, time_left_hub):
        self.package_list = []

        for package in packages:
            self.package_list.append(package)

        self.id = id
        self.time = time
        self.time_left_hub = time_left_hub

    # Returns correct string based on the time.
    def truck_header_at_specified_time(self, time_specified):
        if self.time <= time_specified:
            truck_string = 'Truck ' + str(self.id) + ', Time left hub: ' + str(
                self.time_left_hub) + ', Time truck completed route: ' + str(self.time) + ':'
            return truck_string
        elif self.time >= time_specified >= self.time_left_hub:
            truck_string = 'Truck ' + str(self.id) + ', Time left hub: ' + str(
                self.time_left_hub) + ', Time expected to complete route: ' + str(self.time) + ':'
            return truck_string
        elif time_specified <= self.time_left_hub:
            truck_string = 'Truck ' + str(self.id) + ', Truck leaving hub at: ' + str(
                self.time_left_hub) + ', Time expected to complete route: ' + str(self.time) + ':'
            return truck_string

    def __str__(self):
        i = 1
        truck_string = 'Truck ' + str(self.id) + ', Time left hub: ' + str(
            self.time_left_hub) + ', Time truck completed route: ' + str(self.time) + ':\n'
        truck_string = truck_string + 'Package '
        for package in self.package_list:
            if i == 1:
                truck_string += package.str() + '\n'
                i = i + 1
            else:
                truck_string += 'Package ' + package.str() + '\n'
                i = i + 1
        return truck_string
