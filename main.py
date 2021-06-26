from data_loader import load_packages, load_locations
from data_loader import package_hash
from truck import *
from nearest_neighbor import Graph, Vertex, nearest_neighbor, truck_three_graph
import datetime
import operator
import numbers

# Name: Dylan Stahl
# Student ID: 002996740

def result():
    load_packages('CSV_files/packages.csv')
    first_package = package_hash.search(1)
    second_package = package_hash.search(2)

    # initializes three trucks
    load_trucks()

    # new test data
    # create a truck with every package on it to test algorithm

    truck_one = truck_hash.search(1)
    truck_two = truck_hash.search(2)
    truck_three = truck_hash.search(3)

    truck_one_graph = load_locations(truck_one)

    truck_one_graph.truck
    truck_one_graph.truck_graph.return_to_hub = True
    print('Truck 1 Results:')
    test_algorithm = nearest_neighbor(truck_one_graph.truck_graph, truck_one_graph.vertex_list[0], truck_one_graph.truck)
    i = 0
    for package in truck_one.package_array:
        i = i + 1
    print(str(i) + ' packages')
    print(test_algorithm.path)
    print()
    print(truck_one)

    truck_two_graph = load_locations(truck_two)
    print('Truck 2 Results:')
    test_algorithm = nearest_neighbor(truck_two_graph.truck_graph, truck_two_graph.vertex_list[0], truck_two_graph.truck)
    i = 0
    for package in truck_two.package_array:
        i = i + 1
    print(str(i) + ' packages')
    print(test_algorithm.path)
    print()
    print(truck_two)

    truck_three_graph = load_locations(truck_three)
    print('Truck 3 Results:')
    test_algorithm = nearest_neighbor(truck_three_graph.truck_graph, truck_three_graph.vertex_list[0], truck_three_graph.truck)
    i = 0
    for package in truck_three.package_array:
        i = i + 1
    print(str(i) + ' packages')
    print(test_algorithm.path)
    print()
    print(truck_three)






def main():
    print('Welcome to Western Governors University Parcel Service (WGUPS), this program has found an efficient route '
          'and delivery distribution for the Daily Local Deliveries (DLD).')
    user_input = '1'
    while user_input != 'quit':
        print('Press 1 to insert a package into the system')
        print('Press 2 to check the status of a package')
        print('Press 3 to view the status and info of all packages at a specified time, and the total mileage driven '
              'by each truck')
        print('Press 4 to view the result')
        print('Type \'quit\' to stop running application')
        print()

        user_input = (input(''))
        if user_input == '2':
            package_id_input = (input('Enter the ID of the package: '))
            if (package_id_input.isdigit()):

                print(package_hash.search(int(package_id_input)))
            else:
                print('naw')


            #package_hash.search(package_id_input)

        if user_input == '4':
            result()


if __name__ == '__main__':
    main()
