import csv
from packages import Package
from hash_table_chaining import ChainingHashTable
from nearest_neighbor import Graph, Vertex


class LoadLocation:
    def __init__(self, truck_graph, vertex_list, truck):
        self.truck_graph = truck_graph
        self.vertex_list = vertex_list
        self.truck = truck


# Change chaining hash table size based on number of packages
package_hash = ChainingHashTable(41)


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


def load_locations(truck):
    truck_graph = Graph()

    locations_to_visit = ['4001 South 700 East']
    vertex_list = []

    with open('CSV_files/locations.csv', 'r') as locations_file:
        location_reader = list(csv.reader(locations_file))
        #print(location_reader)

    with open('CSV_files/distances.csv', 'r') as distances_file:
        distance_reader = list(csv.reader(distances_file))
        #print(distance_reader)
        #print()

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
