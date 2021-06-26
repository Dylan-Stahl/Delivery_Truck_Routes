import operator
from locations import Location
from datetime import datetime, timedelta
import math


class Nearest_Neighbor_Results:
    def __init__(self, ordered_list_delivery, total_distance, path):
        self.ordered_list_delivery = ordered_list_delivery
        self.total_distance = total_distance
        self.path = path


class Vertex:
    # Constructor for a new Vertx object. All vertex objects
    # start with a distance of positive infinity.
    def __init__(self, label):
        self.label = label
        self.distance = float('inf')
        self.pred_vertex = None
        self.visited = False

    def __str__(self):
        return self.label


class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.edge_weights = {}
        self.return_to_hub = False

    def get_vertexes(self):
        adjacency_list = []
        for vertex in self.adjacency_list:
            adjacency_list.append(vertex.label)
        return adjacency_list

    def add_vertex(self, new_vertex):
        self.adjacency_list[new_vertex] = []

    def add_directed_edge(self, from_vertex, to_vertex, weight=1.0):
        self.edge_weights[(from_vertex, to_vertex)] = weight
        self.adjacency_list[from_vertex].append(to_vertex)

    def add_undirected_edge(self, vertex_a, vertex_b, weight=1.0):
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)


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
    print('Number of locations to visit: ' + str(len(unvisited_list)))
    current_vertex = start_vertex
    order_to_visit.append(current_vertex)

    # while the unvisited list is not empty
    # while loop iterator
    c = 0
    while len(unvisited_list) > 0:
        # iterator
        i = 1

        # if the list is on the last item, that item must return to wgu only if the graph for that truck says it must
        if len(unvisited_list) == 1:
            if g.return_to_hub == True:
                closest_location_distance = g.edge_weights[(current_vertex, start_vertex)]
                distance_traveled = distance_traveled + float(closest_location_distance)
                closest_location = start_vertex
                order_to_visit.append(closest_location)
                current_vertex.visited == True
                #print('Closest loc dist= ' + str(closest_location_distance))
                #print('Closet loc vertex = ' + str(closest_location))

            path = 'Total distance traveled ' + str(distance_traveled) + '\n' + 'Path: '
            path_list = ''
            z = 0
            for location in order_to_visit:
                if z == 0:
                    path_list = path_list + str(location)
                    z = z + 1
                else:
                    path_list = path_list + ', ' + str(location)
            path = path + path_list

            hours_to_add = (float(distance_traveled) / 18)
            truck.time = truck.time + timedelta(hours=hours_to_add)

            # will return so no need to make unvisitied_list 0 to exit while loop
            #   delete_already_visited_vertex = current_vertex
            #   unvisited_list.remove(delete_already_visited_vertex)
            return Nearest_Neighbor_Results(order_to_visit, distance_traveled, path)

        # find all vertexes adjacent to the start vertex
        for vertex in g.adjacency_list[current_vertex]:
            #print(current_vertex)
            #print(vertex)
            # search through all packages on the truck, if the package address == the vertex.label, than mark the
            # package as visited
            # Marks package as delivered
            # find distance between current vertex and vertex
            if i == 1 and vertex.visited == False:
                # need to update truck time based on closest_location_distance
                closest_location_distance = float(g.edge_weights[(current_vertex, vertex)])
                closest_location = vertex
                #print(closest_location_distance)
                i = i + 1
                #print('Closest loc dist= ' + str(closest_location_distance))
                #print('Closet loc vertex = ' + str(closest_location))
            # Just fixed bux here that I have been working on for days The current vertex and vertex being looped
            # through were being compared against a string of a number (closest_location_distance), I simply converted
            # each string to a float and now the nearest neighbor algorithm is extremely efficient
            else:
                if float(g.edge_weights[(current_vertex, vertex)]) < float(closest_location_distance) and vertex.visited == False:
                    #print(g.edge_weights[(current_vertex, vertex)])
                    #print(closest_location_distance)

                    closest_location_distance = g.edge_weights[(current_vertex, vertex)]
                    closest_location = vertex
                    #print(closest_location_distance)

                    i = i + 1
            #print()

                    #print('Closest loc dist= ' + str(closest_location_distance))
                    #print('Closet loc vertex = ' + str(closest_location))
        # Big brain idea
        # run Dijkstra algorithm between current vertex and closest_location
        # problem: closest location is a label
        # search through vertex list in the graph, if the vertex.label == closest_location, return vertex and send to get_shortest_path
        # look into the adjacency lists for each location in data loader, i suspect not all edges are being loaded in.
        # dijkstra_shortest_path(truck.graph, current_vertex)
        # get_shortest_path(current_vertex, closest_location)


        if c != 0:
            for package in truck.package_array:
                if package.address == closest_location.label:
                    package.status = 'Delivered'
                    hours_to_add = (float(closest_location_distance) / 18)
                    package.time_delivered = last_package.time_delivered + timedelta(hours=hours_to_add)
        elif c == 0:
            for package in truck.package_array:
                if package.address == closest_location.label:
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

        for package in truck.package_array:
            if package.address == closest_location.label:
                last_package = package

        c = c + 1

    if float(distance_traveled) > 18:
        hours_to_add = math.floor(float(closest_location_distance) / 18)
        truck.time = truck.time + timedelta(hours=hours_to_add)
        print(truck.time)

    return Nearest_Neighbor_Results(order_to_visit, distance_traveled)



