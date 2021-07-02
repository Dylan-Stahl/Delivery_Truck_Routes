from data_loader import load_packages, load_locations
from packages import package_hash
from truck import *
from nearest_neighbor import Graph, Vertex, nearest_neighbor
import datetime
import operator
import numbers


# end_of_day_result displays the packages on each truck, the package information, the path for the truck,
# the distance traveled per truck, and the total distance traveled across all three trucks.
# Space and Time Complexity -> O(N^2)
def end_of_day_result():
    # initializes the three trucks -> O(N^2)
    load_trucks()

    # Get a reference to each truck through the hash table -> O(1)
    truck_one = truck_hash.search(1)
    truck_two = truck_hash.search(2)
    truck_three = truck_hash.search(3)

    # Following code displays truck one's data.
    # load_locations is O(N^2)
    truck_one_graph = load_locations(truck_one)

    truck_one_graph.truck_graph.return_to_hub = True
    print('Truck 1 Results:')
    print('After truck one completes it\'s route, the driver will be at WGUPS and will start driving the third truck '
          'immediately')
    # Nearest neighbor algorithm runs at Space and Time complexity O(N^2)
    nearest_neighbor_results_1 = nearest_neighbor(truck_one_graph.truck_graph, truck_one_graph.vertex_list[0],
                                                  truck_one_graph.truck)
    i = 0
    for package in truck_one.package_list:
        i = i + 1

    # Prints the number of packages
    print(str(i) + ' packages')
    print(nearest_neighbor_results_1.path)
    print()
    print(truck_one)

    # Following code displays truck two's data.
    # load_locations is O(N^2)
    truck_two_graph = load_locations(truck_two)
    print('Truck 2 Results:')
    # Nearest neighbor algorithm runs at Space and Time complexity O(N^2)
    nearest_neighbor_results_2 = nearest_neighbor(truck_two_graph.truck_graph, truck_two_graph.vertex_list[0],
                                                  truck_two_graph.truck)
    i = 0
    for package in truck_two.package_list:
        i = i + 1

    # Prints the number of packages
    print(str(i) + ' packages')
    print(nearest_neighbor_results_2.path)
    print()
    print(truck_two)

    # Following code displays truck three's data.
    # load_locations is O(N^2)
    truck_three_graph = load_locations(truck_three)
    print('Truck 3 Results:')
    # Nearest neighbor algorithm runs at Space and Time complexity O(N^2)
    nearest_neighbor_results_3 = nearest_neighbor(truck_three_graph.truck_graph, truck_three_graph.vertex_list[0],
                                                  truck_three_graph.truck)
    i = 0
    for package in truck_three.package_list:
        i = i + 1

    # Prints the number of packages
    print(str(i) + ' packages')
    print(nearest_neighbor_results_3.path)
    print()
    print(truck_three)

    total_distance_traveled = nearest_neighbor_results_1.total_distance + nearest_neighbor_results_2.total_distance + \
                              nearest_neighbor_results_3.total_distance
    print('Total miles driven across the three trucks: ' + str(round(total_distance_traveled, 1)) + ' miles.')
    print()
    return


# Space and Time Complexity -> O(N^2)
def results_at_specified_time(time):
    # initializes the three trucks -> O(N^2)
    load_trucks()

    # Package nine data, package nine has the wrong address
    package_nine_original_address = package_hash.search(9).address
    package_nine_corrected_time = datetime.datetime.today()
    package_nine_corrected_time = package_nine_corrected_time.replace(hour=10, minute=20)

    # Get a reference to each truck through the hash table -> O(1)
    truck_one = truck_hash.search(1)
    truck_two = truck_hash.search(2)
    truck_three = truck_hash.search(3)

    # Following code displays truck one's data.
    # load_locations is O(N^2)
    truck_one_graph = load_locations(truck_one)
    # Truck one is unique in that is is the only truck that has to return to hub.
    truck_one_graph.truck_graph.return_to_hub = True
    # Nearest neighbor algorithm runs at Space and Time complexity O(N^2)
    nearest_neighbor_results_1 = nearest_neighbor(truck_one_graph.truck_graph, truck_one_graph.vertex_list[0],
                                                  truck_one_graph.truck)
    print('Truck 1 Results:')
    print('After truck one completes it\'s route, the driver will be at WGUPS and will start driving the third truck '
          'immediately')
    i = 0
    for package in truck_one.package_list:
        i = i + 1
    print(str(i) + ' packages')
    print(nearest_neighbor_results_1.path)
    print()
    print(truck_one.truck_header_at_specified_time(time))

    for package in truck_one.package_list:
        # There is only one package in the program that is labeled Wrong Address listed, package nine. Package nine's
        # address gets updated at 10:20 and if the user want to see the package status before that time, than the
        # package address must be the incorrect one.
        if package.package_notes == 'Wrong address listed' and time < package_nine_corrected_time:
            package.address = package_nine_original_address
        # Determines for each package if it is En Route, delivered, or at the hub. Changes the package status.
        if truck_one.time_left_hub < time < package.time_delivered:
            package.status = 'En Route'
            print('Package ' + str(package.check_status_en_route(time)))
        elif truck_one.time_left_hub <= package.time_delivered <= time:
            package.status = 'Delivered'
            print('Package ' + str(package.check_status_en_route(time)))
        elif time < truck_one.time_left_hub:
            package.status = 'At Hub'
            print('Package ' + str(package.check_status_en_route(time)))
    print()

    # Following code displays truck two's data.
    # load_locations is O(N^2)
    truck_two_graph = load_locations(truck_two)
    # Nearest neighbor algorithm runs at Space and Time complexity O(N^2)
    nearest_neighbor_results_2 = nearest_neighbor(truck_two_graph.truck_graph, truck_two_graph.vertex_list[0],
                                                  truck_two_graph.truck)
    print('Truck 2 Results:')
    i = 0
    for package in truck_two.package_list:
        i = i + 1
    print(str(i) + ' packages')
    print(nearest_neighbor_results_2.path)
    print()
    print(truck_two.truck_header_at_specified_time(time))
    i = 0

    for package in truck_two.package_list:
        # There is only one package in the program that is labeled Wrong Address listed, package nine. Package nine's
        # address gets updated at 10:20 and if the user want to see the package status before that time, than the
        # package address must be the incorrect one.
        if package.package_notes == 'Wrong address listed' and time < package_nine_corrected_time:
            package.address = package_nine_original_address
        # Determines for each package if it is En Route, delivered, or at the hub. Changes the package status.
        if truck_two.time_left_hub < time < package.time_delivered:
            package.status = 'En Route'
            print('Package ' + str(package.check_status_en_route(time)))
        elif truck_two.time_left_hub <= package.time_delivered <= time:
            package.status = 'Delivered'
            print('Package ' + str(package.check_status_en_route(time)))
        elif time < truck_two.time_left_hub:
            package.status = 'At Hub'
            print('Package ' + str(package.check_status_en_route(time)))
    print()

    # Following code displays truck three's data.
    # load_locations is O(N^2)
    truck_three_graph = load_locations(truck_three)
    # Nearest neighbor algorithm runs at Space and Time complexity O(N^2)
    nearest_neighbor_results_3 = nearest_neighbor(truck_three_graph.truck_graph, truck_three_graph.vertex_list[0],
                                                  truck_three_graph.truck)

    print('Truck 3 Results:')
    i = 0
    for package in truck_three.package_list:
        i = i + 1
    print(str(i) + ' packages')
    print(nearest_neighbor_results_3.path)
    print()
    print(truck_three.truck_header_at_specified_time(time))
    for package in truck_three.package_list:
        # There is only one package in the program that is labeled Wrong Address listed, package nine. Package nine's
        # address gets updated at 10:20 and if the user want to see the package status before that time, than the
        # package address must be the incorrect one.
        if package.package_notes == 'Wrong address listed' and time < package_nine_corrected_time:
            package.address = package_nine_original_address
        # Determines for each package if it is En Route, delivered, or at the hub. Changes the package status.
        if truck_three.time_left_hub < time < package.time_delivered:
            package.status = 'En Route'
            print('Package ' + str(package.check_status_en_route(time)))
        elif truck_three.time_left_hub <= package.time_delivered <= time:
            package.status = 'Delivered'
            print('Package ' + str(package.check_status_en_route(time)))
        elif time < truck_three.time_left_hub:
            package.status = 'At Hub'
            print('Package ' + str(package.check_status_en_route(time)))
    print()

    total_distance_traveled = nearest_neighbor_results_1.total_distance + nearest_neighbor_results_2.total_distance + \
                              nearest_neighbor_results_3.total_distance
    print('Total miles driven or to be driven across the three trucks: ' + str(
        round(total_distance_traveled, 1)) + ' miles.')
    print()
    return


# Space and Time Complexity -> O(N^2)
def package_status(package_to_check, time):
    # initializes the three trucks -> O(N^2)
    load_trucks()

    # Lines 201 - 219 are used to obtain the end of day results.
    truck_one = truck_hash.search(1)
    truck_two = truck_hash.search(2)
    truck_three = truck_hash.search(3)

    # load_locations is O(N^2)
    truck_one_graph = load_locations(truck_one)
    truck_one_graph.truck_graph.return_to_hub = True
    truck_two_graph = load_locations(truck_two)
    truck_three_graph = load_locations(truck_three)

    # package_hash.search() Space and Time complexity is O(1)
    package_nine_original_address = package_hash.search(9).address
    package_nine_corrected_time = datetime.datetime.today()
    package_nine_corrected_time = package_nine_corrected_time.replace(hour=10, minute=20)

    # Nearest neighbor algorithm runs at Space and Time complexity O(N^2)
    nearest_neighbor_results_1 = nearest_neighbor(truck_one_graph.truck_graph, truck_one_graph.vertex_list[0],
                                                  truck_one_graph.truck)
    nearest_neighbor_results_2 = nearest_neighbor(truck_two_graph.truck_graph, truck_two_graph.vertex_list[0],
                                                  truck_two_graph.truck)
    nearest_neighbor_results_3 = nearest_neighbor(truck_three_graph.truck_graph, truck_three_graph.vertex_list[0],
                                                  truck_three_graph.truck)

    # Will hold all the package's ids in the whole program
    indices_array = []

    # Appends package ids to the indices_array -> 0(N)
    for package in range(len(package_hash.table)):
        if package_hash.search(package) is not None:
            indices_array.append(package_hash.search(package).id)

    # Displays package status information -> O(N)
    for package_id in indices_array:
        if package_id == package_to_check.id:
            package_to_display = package_hash.search(package_id)
            # If the user want to view the package status at the end of day, the package is printed.
            if time == 'EOD':
                print(package_to_display)
                return

            # There is only one package in the program that is labeled Wrong Address listed, package nine. Package
            # nine's address gets updated at 10:20 and if the user want to see the package status before that time,
            # than the package address must be the incorrect one.
            if package_to_display.package_notes == 'Wrong address listed' and time < package_nine_corrected_time:
                package_to_display.address = package_nine_original_address
            # Determines if the package is En Route, delivered, or at the hub. Changes the package status.
            if truck_one.time_left_hub < time < package_to_display.time_delivered:
                package_to_display.status = 'En Route'
                print(package_to_display.check_status_en_route(time))
            elif truck_one.time_left_hub <= package_to_display.time_delivered <= time:
                package_to_display.status = 'Delivered'
                print(package_to_display)
            elif time < truck_one.time_left_hub:
                package_to_display.status = 'At Hub'
                print(package_to_display.check_status_at_hub())
            print()
            return
