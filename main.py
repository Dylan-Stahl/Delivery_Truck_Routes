from data_loader import load_packages, load_locations
from data_loader import package_hash
from truck import *
from nearest_neighbor import Graph, Vertex, nearest_neighbor, truck_three_graph
# Name: Dylan Stahl
# Student ID: 002996740

load_packages('CSV_files/packages.csv')
first_package = package_hash.search(1)
second_package = package_hash.search(2)

# initializes three trucks
load_trucks()

# new test data
# create a truck with every package on it to test algorithm
'''
all_packages = []
i = 0
for package in package_hash.table:
    i = i + 1
c = 0
while c <= i:
    packaged_being_loaded = package_hash.search(c)
    if packaged_being_loaded is not None:
        all_packages.append(packaged_being_loaded)
    c = c + 1
for package in all_packages:
    print(package.address)

truck_with_all_packages = Truck(0, all_packages, '8:00', '8:00')

truck_graph = load_locations(truck_with_all_packages)

result = nearest_neighbor(truck_graph.truck_graph, truck_graph.vertex_list[0])


# I need to drop off multiple packages at the same address if possible
'''



#for e in truck_hash.table:
    #print(e)
truck_one = truck_hash.search(1)
i = 0
for package in truck_one.package_array:
    i = i + 1
print(i)
print(truck_one)

truck_two = truck_hash.search(2)
i = 0
for package in truck_two.package_array:
    i = i + 1
print(i)
print(truck_two)

truck_three = truck_hash.search(3)
i = 0
for package in truck_three.package_array:
    i = i + 1
print(i)
print(truck_three)


# I will create separate graphs for each truck
# for e in truck_three.package_array:
    # print for now, but eventually add to nearest neighbor algorithm
    # print(e.address)
    # new_vertex = Vertex(e.address)
    # truck_three_graph.add_vertex(new_vertex)
    # add each address to a graph
'''
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


# Nearest neighbor results on added manual data

closest_location = (nearest_neighbor(truck_three_graph, vertex_1))

print(round(closest_location.total_distance))
print('Following is printing result: ')


for e in closest_location.ordered_list_delivery:
    print(e)


# loading locations test data
truck_two_graph = load_locations(truck_two)
#print(truck_two_graph.vertex_list)
#print(truck_two_graph.truck_graph.get_vertexes())

'''
truck_one_graph = load_locations(truck_one)
truck_one_graph.truck
test_algorithm = nearest_neighbor(truck_one_graph.truck_graph, truck_one_graph.vertex_list[0], truck_one_graph.truck)

truck_two_graph = load_locations(truck_two)
truck_two_graph.truck_graph.return_to_hub = True
test_algorithm = nearest_neighbor(truck_two_graph.truck_graph, truck_two_graph.vertex_list[0], truck_two_graph.truck)

truck_three_graph = load_locations(truck_three)
test_algorithm = nearest_neighbor(truck_three_graph.truck_graph, truck_three_graph.vertex_list[0], truck_three_graph.truck)


