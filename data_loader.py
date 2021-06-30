import csv
from packages import Package, package_hash
from hash_table_chaining import ChainingHashTable


# Class that holds graph data about a truck's route
class LoadLocation:
    def __init__(self, truck_graph, vertex_list, truck):
        self.truck_graph = truck_graph
        self.vertex_list = vertex_list
        self.truck = truck


# Used as a vertex on a graph, each location has a vertex and the vertex label is the location name
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


# Location data and distances are stored in a graph data structure
class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.edge_weights = {}
        self.return_to_hub = False

    # Space complexity is dependent on the size of the adjacency list -> O(n)
    def get_vertexes(self):
        adjacency_list = []
        for vertex in self.adjacency_list:
            adjacency_list.append(vertex.label)
        return adjacency_list

    # Adds a location vertex to the graph
    def add_vertex(self, new_vertex):
        # A new vertex doesn't have any edges when it is initially added
        self.adjacency_list[new_vertex] = []

    def add_directed_edge(self, from_vertex, to_vertex, weight=1.0):
        self.edge_weights[(from_vertex, to_vertex)] = weight
        self.adjacency_list[from_vertex].append(to_vertex)

    # This program only uses add_undirected_edge
    def add_undirected_edge(self, vertex_a, vertex_b, weight=1.0):
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)


# Space and Time Complexity -> O(N)
# Responsible for reading all the package data from the packages.csv file. For every package in the file, attributes
# are saved to create package objects. Those objects are then inserted into the package_hash where they are accessible
# in O(1) time given their id.
def load_packages(fileName):
    # Opens the file, 'r' means reading
    with open(fileName, 'r') as file:
        # Creates a reader object of the file
        package_reader = csv.reader(file)

        # Loops through every package -> O(n)
        for package in package_reader:
            package_id = int(package[0])
            package_address = package[1]
            package_city = package[2]
            package_state = package[3]
            package_zip = package[4]
            package_deadline = package[5]
            package_mass = package[6]
            package_notes = package[7]

            # create package object
            package_obj = Package(package_id, package_address, package_city, package_state, package_zip,
                                  package_deadline, package_mass, package_notes)

            # insert package into the hash table
            package_hash.insert(package_id, package_obj)


# Space - Time Complexity O(N^2)
# In the nearest neighbor algorithm, if package 9 is on the current truck route being created and the current truck
# time is after the time in which package 9's address is updated, the algorithm finds the distance between the current
# location and package 9's new address. It returns the distance between the two locations.
def determine_distance_two_locations(location_list):
    locations_to_visit = []

    with open('CSV_files/locations.csv', 'r') as locations_file:
        location_reader = list(csv.reader(locations_file))

    with open('CSV_files/distances.csv', 'r') as distances_file:
        distance_reader = list(csv.reader(distances_file))

    indices_list = []

    for location in location_list:
        i = 0
        for address in location_reader:
            if location_reader[i][2] == location:
                location_in_csv = location_reader[i][2]
                locations_to_visit.append(location_in_csv)
                # Save the indices of the location in location reader.
                indices_list.append(i)

            i = i + 1

    # Space - Time Complexity -> O(N^2).
    # Each indice in the indices list points to the row of a location, and looping
    # through the indices again for the columns returns the distances between the location in the row and all the
    # locations that have to be visited.
    for row in indices_list:
        # iterator
        c = 0
        # only iterate through columns whose indices are in the indices list
        for col in indices_list:
            if distance_reader[row][col] != '':
                distance = distance_reader[row][col]
                if float(distance) > 0:
                    # Returns distance between the two locations because the indices list only has two indices
                    return distance_reader[row][col]
            c = c + 1
    return


# Space - Time Complexity -> O(N^2)
# load_locations creates the graph for each truck. It does so by obtaining all package locations from the truck. It
# will search for these locations in the locations.csv and save the indices. Similar to the above function,
# it determines distance between all locations.
def load_locations(truck):
    # Creates a graph instance
    truck_graph = Graph()

    # Every trucks starts at WGUPS which is '4001 South 700 East.'
    locations_to_visit = ['4001 South 700 East']
    vertex_list = []

    with open('CSV_files/locations.csv', 'r') as locations_file:
        location_reader = list(csv.reader(locations_file))

    with open('CSV_files/distances.csv', 'r') as distances_file:
        distance_reader = list(csv.reader(distances_file))

    # WGUPS' indice is 0 because it is the first in the locations csv. It is added to the indices_list
    indices_list = [0]

    package_locations = []
    # Adds all locations in the truck's package list to the package_locations list
    for package in truck.package_list:
        # Does not add the same address twice
        if package.address not in package_locations:
            package_locations.append(package.address)

    for package in package_locations:
        i = 0
        for address in location_reader:
            # Finds the address in the locations.csv file and saves the indice of each location
            if location_reader[i][2] == package:
                location = location_reader[i][2]
                locations_to_visit.append(location)
                indices_list.append(i)

            i = i + 1

    # Creates vertexes and adds them to the graph for all the locations that are to be visited
    for location in locations_to_visit:
        location_vertex = Vertex(location)
        vertex_list.append(location_vertex)
        truck_graph.add_vertex(location_vertex)

    # iterator for undirected edges
    f = 0
    for row in indices_list:
        # iterator
        c = 0
        # only iterate through columns whose indices are in the indices list
        for col in indices_list:
            if distance_reader[row][col] != '':
                first_vertex = vertex_list[f]
                second_vertex = vertex_list[c]
                distance = distance_reader[row][col]
                if float(distance) > 0:
                    truck_graph.add_undirected_edge(first_vertex, second_vertex, distance)
            c = c + 1
        f = f + 1

    # There is a lot to return in this function and it made sense to create a class that holds all this data so that
    # an instance of the returned data can be accessed.
    return LoadLocation(truck_graph, vertex_list, truck)
