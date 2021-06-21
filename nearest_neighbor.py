import operator
from locations import Location


class Nearest_Neighbor_Results:
    def __init__(self, ordered_list_delivery, total_distance):
        self.ordered_list_delivery = ordered_list_delivery
        self.total_distance = total_distance


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

    def add_vertex(self, new_vertex):
        self.adjacency_list[new_vertex] = []

    def add_directed_edge(self, from_vertex, to_vertex, weight=1.0):
        self.edge_weights[(from_vertex, to_vertex)] = weight
        self.adjacency_list[from_vertex].append(to_vertex)

    def add_undirected_edge(self, vertex_a, vertex_b, weight=1.0):
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)


truck_three_graph = Graph()


def nearest_neighbor(g, start_vertex):
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
    print(len(unvisited_list))
    for e in unvisited_list:
        print('Unvisited list: ' + str(e))
    print()

    current_vertex = start_vertex
    order_to_visit.append(current_vertex)

    # while the unvisited list is not empty
    while len(unvisited_list) > 0:
        # iterator
        i = 1
        print('Distance traveled: ' + str(distance_traveled))
        print('Current vertex: ' + str(current_vertex))

        # if the list is on the last item, that item must return to wgu
        if len(unvisited_list) == 1:
            closest_location_distance = g.edge_weights[(current_vertex, start_vertex)]
            distance_traveled = distance_traveled + closest_location_distance
            closest_location = start_vertex
            order_to_visit.append(closest_location)
            current_vertex.visited == True

            delete_already_visited_vertex = current_vertex
            unvisited_list.remove(delete_already_visited_vertex)
            return Nearest_Neighbor_Results(order_to_visit, distance_traveled)

        # find all vertexes adjacent to the start vertex
        for vertex in g.adjacency_list[current_vertex]:
            print(vertex)
            # find distance between current vertex and vertex
            if i == 1 and vertex.visited == False:
                closest_location_distance = g.edge_weights[(current_vertex, vertex)]
                closest_location = vertex
                i = i + 1
            else:
                if g.edge_weights[(current_vertex, vertex)] < closest_location_distance and vertex.visited == False:
                    closest_location_distance = g.edge_weights[(current_vertex, vertex)]
                    closest_location = vertex
                    i = i + 1
            # print(vertex)
        order_to_visit.append(closest_location)
        current_vertex.visited = True

        delete_already_visited_vertex = current_vertex

        current_vertex = closest_location
        print('Current vertex now: ' + str(current_vertex))

        unvisited_list.remove(delete_already_visited_vertex)
        distance_traveled = distance_traveled + closest_location_distance

        print('Closest Location: ' + str(closest_location))
        print('Closest location distance: ' + str(closest_location_distance))
        print()
    print()

    return Nearest_Neighbor_Results(order_to_visit, distance_traveled)

# obtain distance data from distances.csv
# implement nearest neighbor algorithm

def load_distances(fileName):
    with open(fileName, 'r') as file:
        distance_reader = csv.reader(file)


def load_locations(fileName):
    with open(fileName, 'r') as file:
        location_reader = csv.reader(file)

        for location in location_reader:
            location_id = int(location[0])
            location_name = location[1]
            location_address = location[2]

            location_obj = Location(location_id, location_name, location_address)
