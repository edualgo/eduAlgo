from .__init__ import print_msg_box

import sys


def dijkstra_algorithm(graph, hint=False):

    global visited_and_distance

    # Providing the graph

    vertices = []
    for x in graph:
        vertices.append([int(y) for y in input().split()])

    edges = []
    for x in graph:
        edges.append([int(y) for y in input().split()])

    # Find which vertex is to be visited next

    to_be_visited()

    num_of_vertices = len(vertices[0])

    visited_and_distance = [[0, 0]]
    for i in range(num_of_vertices-1):
        visited_and_distance.append([0, sys.maxsize])

    for vertex in range(num_of_vertices):

        # Find next vertex to be visited
        to_visit = to_be_visited()
        for neighbor_index in range(num_of_vertices):

            # Updating new distances
            if vertices[to_visit][neighbor_index] == 1 and \
                    visited_and_distance[neighbor_index][0] == 0:
                new_distance = visited_and_distance[to_visit][1] \
                    + edges[to_visit][neighbor_index]
                if visited_and_distance[neighbor_index][1] > new_distance:
                    visited_and_distance[neighbor_index][1] = new_distance

            visited_and_distance[to_visit][0] = 1

    i = 0

    # Printing the distance
    for distance in visited_and_distance:
        print("Distance of ", chr(ord('a') + i),
              " from source vertex: ", distance[1])
        i = i + 1


# Function to Find which vertex is to be visited next

def to_be_visited(num_of_vertices):
    v = -10
    for index in range(num_of_vertices):
        if visited_and_distance[index][0] == 0 \
                and (v < 0 or visited_and_distance[index][1] <= visited_and_distance[v][1]):
            v = index
    return v


def print_Dijkstras_hint(self):
    message = """
    Dijkstra's algorithm allows us to find the shortest path between any two vertices of a graph.
    -+-+-+-+-+-+-+-+-+-+-+-+-+--+-+-+-+-+-+-+-+-+-+-+-+-+--+-+-+-+-+-+-+-+-+-+-+-+-+--+-+-+-+-+-+-+-+-+
    
    Dijkstra's Algorithm works on the basis that any subpath Point 2 ⇒ Point 4 of the shortest path Point 1 ⇒ Point 4 between vertices Point 1 and Point 4 is also the shortest path between vertices Point 2 and Point 4.
    Djikstra used this property in the opposite direction i.e we overestimate the distance of each vertex from the starting vertex. Then we visit each node and its neighbors to find the shortest subpath to those neighbors.
    The algorithm uses a greedy approach in the sense that we find the next best solution hoping that the end result is the best solution for the whole problem.
    -+-+-+-+-+--+-+-+-+--+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+--+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

    PseudoCode:

    * We need to take care of the trail distance of each vertex. we will store that in an array of size v, where v is that the number of vertices.

    * We also want to be ready to get the shortest path, not only know the length of the shortest path. For this, we map each vertex to the vertex that last updated its path length.

    * Once the algorithm is over, we will backtrack from the destination vertex to the source vertex to seek out the trail .

    * A minimum priority queue are often wont to efficiently receive the vertex with the smallest amount path distance.
    
    Code:

    function dijkstra(G, S)
    for each vertex V in G
        distance[V] <- infinite
        previous[V] <- NULL
        If V != S, add V to Priority Queue Q
    distance[S] <- 0
	
    while Q IS NOT EMPTY
        U <- Extract MIN from Q
        for each unvisited neighbour V of U
            tempDistance <- distance[U] + edge_weight(U, V)
            if tempDistance < distance[V]
                distance[V] <- tempDistance
                previous[V] <- U
    return distance[], previous[]

    -+-+-+-+-+-+-+-+-+-+--+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-

    Complexity:

    Time Complexity: O(E Log V)
        where, E is the number of edges and V is the number of vertices.

    Space Complexity: O(V)
    -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    
    More Info Here: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
    """
    print_msg_box(message)
