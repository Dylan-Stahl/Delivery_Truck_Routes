from data_loader import load_packages, load_locations
from packages import package_hash
from truck import *
from nearest_neighbor import Graph, Vertex, nearest_neighbor, truck_three_graph
import datetime
import operator
import numbers


def end_of_day_result():
    load_packages('CSV_files/packages.csv')

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
    print('After truck one completes it\'s route, the driver will be at WGUPS and will start driving the third truck '
          'immediately')
    nearest_neighbor_results_1 = nearest_neighbor(truck_one_graph.truck_graph, truck_one_graph.vertex_list[0],
                                                  truck_one_graph.truck)
    i = 0
    for package in truck_one.package_array:
        i = i + 1
    print(str(i) + ' packages')
    print(nearest_neighbor_results_1.path)
    print()
    print(truck_one)

    truck_two_graph = load_locations(truck_two)
    print('Truck 2 Results:')
    nearest_neighbor_results_2 = nearest_neighbor(truck_two_graph.truck_graph, truck_two_graph.vertex_list[0],
                                                  truck_two_graph.truck)
    i = 0
    for package in truck_two.package_array:
        i = i + 1
    print(str(i) + ' packages')
    print(nearest_neighbor_results_2.path)
    print()
    print(truck_two)

    truck_three_graph = load_locations(truck_three)
    print('Truck 3 Results:')
    nearest_neighbor_results_3 = nearest_neighbor(truck_three_graph.truck_graph, truck_three_graph.vertex_list[0],
                                                  truck_three_graph.truck)
    i = 0
    for package in truck_three.package_array:
        i = i + 1
    print(str(i) + ' packages')
    print(nearest_neighbor_results_3.path)
    print()
    print(truck_three)

    total_distance_traveled = nearest_neighbor_results_1.total_distance + nearest_neighbor_results_2.total_distance + \
                              nearest_neighbor_results_3.total_distance
    print('Total miles driven across the three trucks: ' + str(round(total_distance_traveled, 1)) + ' miles.')
    print()


def results_at_specified_time(time):
    load_packages('CSV_files/packages.csv')

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
    nearest_neighbor_results_1 = nearest_neighbor(truck_one_graph.truck_graph, truck_one_graph.vertex_list[0],
                                                  truck_one_graph.truck)
    print('Truck 1 Results:')
    print('After truck one completes it\'s route, the driver will be at WGUPS and will start driving the third truck '
          'immediately')
    i = 0
    for package in truck_one.package_array:
        i = i + 1
    print(str(i) + ' packages')
    print(nearest_neighbor_results_1.path)
    print()
    print(truck_one.truck_header_at_specified_time(time))

    for package in truck_one.package_array:
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

    truck_two_graph = load_locations(truck_two)
    nearest_neighbor_results_2 = nearest_neighbor(truck_two_graph.truck_graph, truck_two_graph.vertex_list[0],
                                                  truck_two_graph.truck)
    print('Truck 2 Results:')
    for package in truck_two.package_array:
        i = i + 1
    print(str(i) + ' packages')
    print(nearest_neighbor_results_2.path)
    print()
    print(truck_two.truck_header_at_specified_time(time))
    i = 0

    for package in truck_two.package_array:
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

    truck_three_graph = load_locations(truck_three)
    nearest_neighbor_results_3 = nearest_neighbor(truck_three_graph.truck_graph, truck_three_graph.vertex_list[0],
                                                  truck_three_graph.truck)

    print('Truck 3 Results:')
    i = 0
    for package in truck_three.package_array:
        i = i + 1
    print(str(i) + ' packages')
    print(nearest_neighbor_results_3.path)
    print()
    print(truck_three.truck_header_at_specified_time(time))
    for package in truck_three.package_array:
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
    print('Total miles driven or to be driven across the three trucks: ' + str(round(total_distance_traveled, 1)) + ' miles.')
    print()


def package_status(package_to_check, time):
    # perform nearest neighbor on the package's truck
    # compare the packages delivery time to the argument's time
    # if the argument's time is after the truck has left and before the package has been delivered, mark package status
    # as en route.
    # if the truck hasn't left the depot left, mark package status as at hub, else mark delivered

    load_packages('CSV_files/packages.csv')

    # initializes three trucks
    load_trucks()

    # new test data
    # create a truck with every package on it to test algorithm

    truck_one = truck_hash.search(1)
    truck_two = truck_hash.search(2)
    truck_three = truck_hash.search(3)

    truck_one_graph = load_locations(truck_one)
    truck_one_graph.truck_graph.return_to_hub = True
    truck_two_graph = load_locations(truck_two)
    truck_three_graph = load_locations(truck_three)

    package_nine_original_address = package_hash.search(9).address
    package_nine_corrected_time = datetime.datetime.today()
    package_nine_corrected_time = package_nine_corrected_time.replace(hour=10, minute=20)

    nearest_neighbor_results_1 = nearest_neighbor(truck_one_graph.truck_graph, truck_one_graph.vertex_list[0],
                                                  truck_one_graph.truck)
    nearest_neighbor_results_2 = nearest_neighbor(truck_two_graph.truck_graph, truck_two_graph.vertex_list[0],
                                                  truck_two_graph.truck)
    nearest_neighbor_results_3 = nearest_neighbor(truck_three_graph.truck_graph, truck_three_graph.vertex_list[0],
                                                  truck_three_graph.truck)

    for package in truck_one.package_array:
        # loop through the package hash, if package_to_check == element in the package hash, save the id for further
        # calculate size of the package hash
        if package.id == package_to_check.id:
            if package.package_notes == 'Wrong address listed' and time < package_nine_corrected_time:
                package.address = package_nine_original_address
            if truck_one.time_left_hub < time < package.time_delivered:
                package.status = 'En Route'
                print(package.check_status_en_route(time))
            elif truck_one.time_left_hub <= package.time_delivered <= time:
                package.status = 'Delivered'
                print(package)
            elif time < truck_one.time_left_hub:
                package.status = 'At Hub'
                print(package.check_status_at_hub())
            print()
            return
        # package = package_hash.search()
    for package in truck_two.package_array:
        if package.id == package_to_check.id:
            if package.package_notes == 'Wrong address listed' and time < package_nine_corrected_time:
                package.address = package_nine_original_address
            if truck_two.time_left_hub < time < package.time_delivered:
                package.status = 'En Route'
                print(package.check_status_en_route(time))
            elif truck_two.time_left_hub <= package.time_delivered <= time:
                package.status = 'Delivered'
                print(package)
            elif time < truck_two.time_left_hub:
                package.status = 'At Hub'
                print(package.check_status_at_hub())
            print()
            return
    for package in truck_three.package_array:
        if package.id == package_to_check.id:
            if package.package_notes == 'Wrong address listed' and time < package_nine_corrected_time:
                package.address = package_nine_original_address
            if truck_three.time_left_hub < time < package.time_delivered:
                package.status = 'En Route'
                print(package.check_status_en_route(time))
            elif truck_three.time_left_hub <= package.time_delivered <= time:
                package.status = 'Delivered'
                print(package)
            elif time < truck_three.time_left_hub:
                package.status = 'At Hub'
                print(package.check_status_at_hub())
            print()
            return

    return print('Not working')
