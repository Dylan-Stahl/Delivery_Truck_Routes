from data_loader import load_packages, load_locations
from data_loader import package_hash
from truck import *
from nearest_neighbor import Graph, Vertex, nearest_neighbor, truck_three_graph
# Name: Dylan Stahl
# Student ID: 002996740

load_packages('CSV_files/packages.csv')
first_package = package_hash.search(1)
second_package = package_hash.search(2)

# print(Truck)

load_trucks()

for e in truck_hash.table:
    print(e)
truck_one = truck_hash.search(1)
print(truck_one)

truck_two = truck_hash.search(2)
print(truck_two)

truck_three = truck_hash.search(3)
print(truck_three)


# I will create separate graphs for each truck
# for e in truck_three.package_array:
    # print for now, but eventually add to nearest neighbor algorithm
    # print(e.address)
    # new_vertex = Vertex(e.address)
    # truck_three_graph.add_vertex(new_vertex)
    # add each address to a graph

vertex_1 = Vertex('WGU')
truck_three_graph.add_vertex(vertex_1)
vertex_2 = Vertex('Garden')
truck_three_graph.add_vertex(vertex_2)
vertex_3 = Vertex('Park')
truck_three_graph.add_vertex(vertex_3)
vertex_4 = Vertex('Taylorsville')
truck_three_graph.add_vertex(vertex_4)


truck_three_graph.add_undirected_edge(vertex_1, vertex_2, 7.2)
truck_three_graph.add_undirected_edge(vertex_1, vertex_3, 3.8)
truck_three_graph.add_undirected_edge(vertex_1, vertex_4, 11.0)

truck_three_graph.add_undirected_edge(vertex_2, vertex_3, 7.1)
truck_three_graph.add_undirected_edge(vertex_2, vertex_4, 6.4)
truck_three_graph.add_undirected_edge(vertex_3, vertex_4, 9.2)

closest_location = (nearest_neighbor(truck_three_graph, vertex_1))

print(round(closest_location.total_distance))
print('Following is printing result: ')


for e in closest_location.ordered_list_delivery:
    print(e)


# loading locations test data
truck_two_graph = load_locations(truck_two)
print(truck_two_graph.vertex_list)
print(truck_two_graph.truck_graph.get_vertexes())


# nearest_neighbor_truck_three = nearest_neighbor(truck_two_graph, truck_two_graph.adj)
# adds weighted edge between WGU and 195 W oakland Ave
truck_two_graph.truck_graph.add_undirected_edge(truck_two_graph.vertex_list[0], truck_two_graph.vertex_list[1], 3.5)
truck_two_graph.truck_graph.add_undirected_edge(truck_two_graph.vertex_list[1], truck_two_graph.vertex_list[2], 4.5)

truck_two_nearest_neighbor = nearest_neighbor(truck_two_graph.truck_graph, truck_two_graph.vertex_list[0])

