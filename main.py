from data_loader import load_packages
from data_loader import package_hash
from truck import *

# Name: Dylan Stahl
# Student ID: 002996740

load_packages('CSV_files/packages.csv')
first_package = package_hash.search(1)
second_package = package_hash.search(2)

# print(Truck)

load_trucks()

for e in truck_hash.table:
    print(e)
truck_one = truck_hash.search(1)
print(truck_one)

truck_two = truck_hash.search(2)
print(truck_two)

truck_three = truck_hash.search(3)
print(truck_three)
for e in truck_three.package_array:
    # print for now, but eventually add to nearest neighbor algorithm
    print(e)
print(truck_three.package_array)
