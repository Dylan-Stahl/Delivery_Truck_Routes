from data_loader import load_packages
from data_loader import package_hash
from truck import *

# Name: Dylan Stahl
# Student ID: 002996740

load_packages('CSV_files/packages.csv')
first_package = package_hash.search(1)
second_package = package_hash.search(2)

Truck = Truck([first_package, second_package], '8:00', '9:00')

# print(Truck)

load_trucks()

for e in truck_hash.table:
    print(e)
truck_one = truck_hash.search(0)
print(truck_one)
