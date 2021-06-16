import csv
from packages import Package
from hash_table_chaining import ChainingHashTable


package_hash = ChainingHashTable()
def load_packages(fileName):
    with open(fileName, 'r') as file:
        package_reader = csv.reader(file)

        for package in package_reader:
            package_id = int(package[0])
            package_address = package[1]
            package_city = package[2]
            package_state = package[3]
            package_zip = package[4]
            package_deadline = package[5]
            package_mass = package[6]

            # create package object
            package_obj = Package(package_id, package_address, package_city, package_state, package_zip,
                              package_deadline, package_mass)
            print(package)
            # insert package into the hash table
            package_hash.insert(package_id, package_obj)

