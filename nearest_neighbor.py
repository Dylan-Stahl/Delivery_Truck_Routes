import operator
from locations import Location
from datetime import *
import math
from packages import package_hash
from data_loader import *


class Nearest_Neighbor_Results:
    def __init__(self, ordered_list_delivery, total_distance, path):
        self.ordered_list_delivery = ordered_list_delivery
        self.total_distance = total_distance
        self.path = path


truck_three_graph = Graph()


def nearest_neighbor(g, start_vertex, truck):
    # what i need to change:
    # packages that must be delivered by end of the day must be delivered first

    order_to_visit = []
    # Put all vertices in an unvisited queue.
    unvisited_list = []

    # total distance traveled for the truck
    distance_traveled = 0

    # add all vertexes to unvisited queue
    for current_vertex in g.adjacency_list:
        unvisited_list.append(current_vertex)
        # make sure all vertexes are set to not visited
        current_vertex.visited = False
        # unvisited_queue = [vertex_1, vertex_2, ...]

    # new design here
    # print('Number of locations to visit: ' + str(len(unvisited_list)))
    current_vertex = start_vertex
    order_to_visit.append(current_vertex)

    # Accounting for packages with wrong addresses:
    # loop through truck package array, if a package's notes say that the wrong address is listed, mark that packages
    # address vertex as visited, this way the algorithm does not visit that vertex
    # Create an if statement that will compare the truck's current time to the time in which the package's address
    # will be updated, if the truck's time is after that time, update the packages address and change the vertex.visited
    # to false

    for package in truck.package_array:
        if package.package_notes == 'Wrong address listed':
            # This way the algorithm doesn't visit the vertex
            visit_address = False
            for packages in truck.package_array:
                if packages.address == package.address:
                    visit_address = True
                    continue
                else:
                    visit_address = False
                    continue

            package.visited = True

            if visit_address == False:
                for vertex in unvisited_list:
                    if vertex.label == package.address:
                        vertex.visited = True
    package_nine_corrected_time = datetime.today()
    package_nine_corrected_time = package_nine_corrected_time.replace(hour=10, minute=20)

    # while the unvisited list is not empty
    # while loop iterator
    c = 0
    while len(unvisited_list) > 0:
        # iterator
        i = 1

        # if the list is on the last item, that item must return to wgu only if the graph for that truck says it must
        if len(unvisited_list) == 1:
            # This if statement is executed for truck 1, as truck 1 returns to the hub to drive truck three
            if g.return_to_hub == True:
                closest_location_distance = g.edge_weights[(current_vertex, start_vertex)]
                distance_traveled = distance_traveled + float(closest_location_distance)
                closest_location = start_vertex
                order_to_visit.append(closest_location)
                current_vertex.visited == True
                hours_to_add = (float(closest_location_distance) / 18)
                truck.time = truck.time + timedelta(hours=hours_to_add)

            # After all the packages have been delivered, the packaged, 9, that has the wrong address will be delivered
            if truck.id == 3 and truck.time > package_nine_corrected_time:
                package_hash.search(9).address = '410 S State St'
                package_hash.search(9).visited = True
                # determine distance from the new address and last package delivered location
                # last_package.address
                # package_hash.search(9).address
                determine_distance = [last_package.address, package_hash.search(9).address]
                distance_between_nine_and_last_package = (determine_distance_two_locations(determine_distance))

                distance_traveled = distance_traveled + float(distance_between_nine_and_last_package)
                closest_location_distance = distance_between_nine_and_last_package
                order_to_visit.append(package_hash.search(9).address)
                package_hash.search(9).visited = True
                package_hash.search(9).status = 'Delivered'
                package_hash.search(9).time_delivered = last_package.time_delivered + timedelta(hours=hours_to_add)

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

            # will return so no need to make unvisitied_list 0 to exit while loop
            #   delete_already_visited_vertex = current_vertex
            #   unvisited_list.remove(delete_already_visited_vertex)
            return Nearest_Neighbor_Results(order_to_visit, distance_traveled, path)

        # find all vertexes adjacent to the start vertex
        for vertex in g.adjacency_list[current_vertex]:
            # print(current_vertex)
            # print(vertex)
            # search through all packages on the truck, if the package address == the vertex.label, than mark the
            # package as visited
            # Marks package as delivered
            # find distance between current vertex and vertex
            if i == 1 and vertex.visited == False:
                # need to update truck time based on closest_location_distance
                closest_location_distance = float(g.edge_weights[(current_vertex, vertex)])
                closest_location = vertex
                # print(closest_location_distance)
                i = i + 1
                # print('Closest loc dist= ' + str(closest_location_distance))
                # print('Closet loc vertex = ' + str(closest_location))
            # Just fixed bux here that I have been working on for days The current vertex and vertex being looped
            # through were being compared against a string of a number (closest_location_distance), I simply converted
            # each string to a float and now the nearest neighbor algorithm is extremely efficient
            elif vertex.visited == False:
                if float(g.edge_weights[(current_vertex, vertex)]) < float(
                        closest_location_distance) and vertex.visited == False:
                    # print(g.edge_weights[(current_vertex, vertex)])
                    # print(closest_location_distance)

                    closest_location_distance = g.edge_weights[(current_vertex, vertex)]
                    closest_location = vertex
                    # print(closest_location_distance)

                    i = i + 1
            else:
                continue

        if c != 0:
            for package in truck.package_array:
                if package.address == closest_location.label and package.visited == False:
                    package.visited = True
                    package.status = 'Delivered'
                    hours_to_add = (float(closest_location_distance) / 18)
                    package.time_delivered = last_package.time_delivered + timedelta(hours=hours_to_add)
        elif c == 0:
            for package in truck.package_array:
                if package.address == closest_location.label and package.visited == False:
                    package.visited = True
                    package.status = 'Delivered'
                    hours_to_add = (float(closest_location_distance) / 18)
                    package.time_delivered = truck.time + timedelta(hours=hours_to_add)
                    last_package = package

        order_to_visit.append(closest_location)
        current_vertex.visited = True

        delete_already_visited_vertex = current_vertex

        current_vertex = closest_location
        unvisited_list.remove(delete_already_visited_vertex)
        distance_traveled = distance_traveled + float(closest_location_distance)

        hours_to_add = (float(closest_location_distance) / 18)
        truck.time = truck.time + timedelta(hours=hours_to_add)

        for package in truck.package_array:
            if package.address == closest_location.label:
                last_package = package

        c = c + 1

    if float(distance_traveled) > 18:
        hours_to_add = math.floor(float(closest_location_distance) / 18)
        truck.time = truck.time + timedelta(hours=hours_to_add)
        print(truck.time)

    return Nearest_Neighbor_Results(order_to_visit, distance_traveled)
