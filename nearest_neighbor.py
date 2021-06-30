import operator
from locations import Location
from datetime import *
import math
from packages import package_hash
from data_loader import *


# Class to holds the results from the nearest neighbor algorithm
class Nearest_Neighbor_Results:
    def __init__(self, ordered_list_delivery, total_distance, path):
        self.ordered_list_delivery = ordered_list_delivery
        self.total_distance = total_distance
        self.path = path


# Algorithm that find an efficient route for each truck -> O(N^2)
def nearest_neighbor(graph, start_vertex, truck):
    # Order to visit will hold the order in which the truck path will be
    order_to_visit = []

    # All vertexes in the graph are added to the unvisited_list
    unvisited_list = []

    # total distance traveled for the truck
    distance_traveled = 0

    # add all vertexes to unvisited_list
    for current_vertex in graph.adjacency_list:
        unvisited_list.append(current_vertex)
        # make sure all vertexes are set to not visited
        current_vertex.visited = False

    # The algorithm starts at the start vertex
    current_vertex = start_vertex
    order_to_visit.append(current_vertex)

    # Accounting for packages with wrong addresses:
    # loop through truck package array, if a package's notes say that the wrong address is listed, mark that packages
    # address vertex as visited, this way the algorithm does not visit that vertex
    for package in truck.package_list:
        if package.package_notes == 'Wrong address listed':
            # This way the algorithm doesn't visit the vertex
            visit_address = False
            # If the truck is visiting the location by dropping off another package with the same address,
            # then the location should still be visited. If no other packages have the address of the package with
            # the wrong address, then that location should not be visited.
            for packages in truck.package_list:
                if packages.address == package.address:
                    visit_address = True
                    continue
                else:
                    visit_address = False
                    continue

            package.visited = True

            # If the boolean variable visit_address is False, then the vertex is marked as visited so the algorithm
            # skips over it.
            if visit_address == False:
                for vertex in unvisited_list:
                    if vertex.label == package.address:
                        vertex.visited = True
    # Holds the time in which the package will be visited
    package_nine_corrected_time = datetime.today()
    package_nine_corrected_time = package_nine_corrected_time.replace(hour=10, minute=20)

    # while the unvisited list is not empty the algorithm runs, it will go through every vertex in the list and remove
    # them from the list once it is added to the order_to_visit_list
    # while loop counter
    c = 0
    while len(unvisited_list) > 0:
        # iterator
        i = 1

        # if the list is on the last item, the path has been almost finished and a few things need to be checked.
        if len(unvisited_list) == 1:
            # This if statement is executed for truck 1, as truck 1 returns to the hub to drive truck three. It
            # adds WGUPS in the order to visit and adds the total distance to distance_traveled.
            if graph.return_to_hub == True:
                closest_location_distance = graph.edge_weights[(current_vertex, start_vertex)]
                distance_traveled = distance_traveled + float(closest_location_distance)
                closest_location = start_vertex
                order_to_visit.append(closest_location)
                current_vertex.visited == True
                hours_to_add = (float(closest_location_distance) / 18)
                truck.time = truck.time + timedelta(hours=hours_to_add)

            # After all the packages have been delivered, the packaged, 9, that has the wrong address will be delivered
            # if the truck's current time is after the time in which package 9's address is corrected.
            if truck.id == 3 and truck.time > package_nine_corrected_time:
                # Changes the address of package 9 to the correct address
                package_hash.search(9).address = '410 S State St'
                package_hash.search(9).visited = True
                # determine distance from the new address and last package delivered location
                determine_distance = [last_package.address, package_hash.search(9).address]
                distance_between_nine_and_last_package = (determine_distance_two_locations(determine_distance))

                closest_location_distance = float(distance_between_nine_and_last_package)
                distance_traveled = distance_traveled + closest_location_distance
                order_to_visit.append(package_hash.search(9).address)

                package_hash.search(9).visited = True
                package_hash.search(9).status = 'Delivered'

                hours_to_add = (float(closest_location_distance) / 18)
                package_hash.search(9).time_delivered = last_package.time_delivered + timedelta(hours=hours_to_add)
                # The truck completes it's route when package 9 is delivered
                truck.time = last_package.time_delivered + timedelta(hours=hours_to_add)

            path = 'Total distance to travel or traveled ' + str(
                round(distance_traveled, 1)) + ' miles.' + '\n' + 'Path: '
            path_list = ''
            z = 0
            for location in order_to_visit:
                if z == 0:
                    path_list = path_list + str(location)
                    z = z + 1
                else:
                    path_list = path_list + ', ' + str(location)
            path = path + path_list

            # Functions returns so no need to make unvisited_list 0 to exit while loop.
            # Results are stored in a Nearest_Neighbor_Results object.
            return Nearest_Neighbor_Results(order_to_visit, distance_traveled, path)

        # Loop through all vertexes adjacent to the current vertex vertex
        for vertex in graph.adjacency_list[current_vertex]:
            # When looping through all the adjacent vertex of the current vertex, if the algorithm is searching
            # the first adjacent vertex, it will need to mark that vertex as the closest_location. Then
            # in the elif statement after this if statement, it will be able to compare all the other adjacent vertexes
            # effectively.
            if i == 1 and vertex.visited == False:
                closest_location_distance = float(graph.edge_weights[(current_vertex, vertex)])
                closest_location = vertex
                i = i + 1
            # Fixed bug here. The current vertex and vertex being looped
            # through were being compared against a string of a number, I simply converted
            # each string to a float and now the nearest neighbor algorithm is working as expected
            elif vertex.visited == False:
                # Compares the previous closest_location_distance to the current vertex in the adjacency lists distance
                # If the current vertex that is being looped through is closer to the current than the previous closest,
                # The current vertex being looped through is saved as the closest_location
                if float(graph.edge_weights[(current_vertex, vertex)]) < float(
                        closest_location_distance) and vertex.visited == False:
                    closest_location_distance = graph.edge_weights[(current_vertex, vertex)]
                    closest_location = vertex
                    i = i + 1

        # This if - elif block saves the packages with the address of the closest_location as visited and marks the
        # delivery status to 'Delivered'. It will also change the package data member, time_delivered, to the correct
        # value.
        if c != 0:
            for package in truck.package_list:
                if package.address == closest_location.label and package.visited == False:
                    package.visited = True
                    package.status = 'Delivered'
                    hours_to_add = (float(closest_location_distance) / 18)
                    package.time_delivered = last_package.time_delivered + timedelta(hours=hours_to_add)
        # If it is the first iteration of the while loop, there is no last_package. The closest_location will be the
        # first package dropped off and therefore the time the package is delivered is the truck.time + (
        # closest_location_distance/18). Divided by 18 because all the trucks are driving at a constant 18 miles per
        # hour.
        elif c == 0:
            for package in truck.package_list:
                if package.address == closest_location.label and package.visited == False:
                    package.visited = True
                    package.status = 'Delivered'
                    hours_to_add = (float(closest_location_distance) / 18)
                    package.time_delivered = truck.time + timedelta(hours=hours_to_add)

        # The order_to_visit list appends the closest_location found in the current vertex's adjacency list.
        order_to_visit.append(closest_location)
        # Changes current vertex's data member visited to True so that it will not be visited by nearest_neighbor
        # again.
        current_vertex.visited = True

        # Temporary variable to delete the current vertex from the unvisited_list
        delete_already_visited_vertex = current_vertex

        # Nearest neighbor's next iteration will use the closest_location as the current_vertex
        current_vertex = closest_location
        unvisited_list.remove(delete_already_visited_vertex)
        # Updates the variable distance_traveled to the new value of traveling to the nearest location.
        distance_traveled = distance_traveled + float(closest_location_distance)

        # Updates the truck's time by finding the amount of time to add and then adding that to the truck's current
        # time.
        hours_to_add = (float(closest_location_distance) / 18)
        truck.time = truck.time + timedelta(hours=hours_to_add)

        # Last package needs to be a package that was delivered in the current iteration. last_package is used to
        # keep track of package delivery times.
        for package in truck.package_list:
            if package.address == closest_location.label:
                last_package = package

        # While loop counter is updated
        c = c + 1

    return Nearest_Neighbor_Results(order_to_visit, distance_traveled)
