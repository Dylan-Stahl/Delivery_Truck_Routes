import csv
from packages import Package, package_hash
from hash_table_chaining import ChainingHashTable


class LoadLocation:
    def __init__(self, truck_graph, vertex_list, truck):
        self.truck_graph = truck_graph
        self.vertex_list = vertex_list
        self.truck = truck


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
            package_notes = package[7]

            # create package object
            package_obj = Package(package_id, package_address, package_city, package_state, package_zip,
                                  package_deadline, package_mass, package_notes)
            # print(package)
            # insert package into the hash table
            package_hash.insert(package_id, package_obj)


def determine_distance_two_locations(location_list):
    locations_to_visit = []
    vertex_list = []

    with open('CSV_files/locations.csv', 'r') as locations_file:
        location_reader = list(csv.reader(locations_file))
        # print(location_reader)

    with open('CSV_files/distances.csv', 'r') as distances_file:
        distance_reader = list(csv.reader(distances_file))
        # print(distance_reader)
        # print()

    indice_array = []

    for location in location_list:
        i = 0
        for address in location_reader:
            if location_reader[i][2] == location:
                # location_reader[i][1] becomes  a key in the dictionary
                location_in_csv = location_reader[i][2]
                locations_to_visit.append(location_in_csv)
                indice_array.append(i)

            i = i + 1

    # iterator for directed edges
    f = 0
    for e in indice_array:
        # iterator
        c = 0
        # only iterate through coloumns whose indice is in the indice array
        for col in indice_array:
            if distance_reader[e][col] != '':
                distance = distance_reader[e][col]
                if float(distance) > 0:
                    return (distance_reader[e][col])
            c = c + 1
        f = f + 1

    return


def load_locations(truck):
    truck_graph = Graph()

    locations_to_visit = ['4001 South 700 East']
    vertex_list = []

    with open('CSV_files/locations.csv', 'r') as locations_file:
        location_reader = list(csv.reader(locations_file))
        # print(location_reader)

    with open('CSV_files/distances.csv', 'r') as distances_file:
        distance_reader = list(csv.reader(distances_file))
        # print(distance_reader)
        # print()

    # regardless of truck, wgu must be an address/ vertex
    indice_array = [0]

    # check all packages locations, mark each location as visited, if another package has that same location, do not add
    # location
    package_locations = []
    for package in truck.package_array:
        if package.address not in package_locations:
            package_locations.append(package.address)

    for package in package_locations:
        i = 0
        for address in location_reader:
            if location_reader[i][2] == package:
                # location_reader[i][1] becomes  a key in the dictionary
                location = location_reader[i][2]
                locations_to_visit.append(location)
                indice_array.append(i)

            i = i + 1
        # print(package.address)

    for location in locations_to_visit:
        location_vertex = Vertex(location)
        vertex_list.append(location_vertex)
        truck_graph.add_vertex(location_vertex)

    # iterator for directed edges
    f = 0
    for e in indice_array:
        # iterator
        c = 0
        # only iterate through coloumns whose indice is in the indice array
        for col in indice_array:
            if distance_reader[e][col] != '':
                first_vertex = vertex_list[f]
                second_vertex = vertex_list[c]
                distance = distance_reader[e][col]
                if float(distance) > 0:
                    truck_graph.add_undirected_edge(first_vertex, second_vertex, distance)
                    '''
                    print(first_vertex)
                    print(second_vertex)

                    # search for second vertex
                    print(distance_reader[e][col])
                    if distance_reader[col][e] != '':
                        print(distance_reader[col][e])
                    print() '''
            c = c + 1
        f = f + 1

    return LoadLocation(truck_graph, vertex_list, truck)
