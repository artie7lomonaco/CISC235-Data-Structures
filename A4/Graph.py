import random
import heapq
import sys


# https://www.bogotobogo.com/python/python_graph_data_structures.php
# https://www.bogotobogo.com/python/python_Prims_Spanning_Tree_Data_Structure.php

class Vertex():
    def __init__(self, key):
        self.key = key
        self.neighbors = {}
        self.visited = False
        self.distance = 0
        self.previous = None

    def add_neighbor(self, neighbor, weight=0):
        self.neighbors[neighbor] = weight

    def get_connections(self):
        return self.neighbors.keys()

    def get_weight(self, neighbor):
        return self.neighbors[neighbor]

    # instead of having a variable in a list for when visited
    # easier to have it as a field of the class Vertex
    def set_visited(self):
        self.visited = True

    # set the distance of the node, used in prim's mst
    def set_distance(self, dist):
        self.distance = dist

    # gets distance, also for prim's mst
    def get_distance(self):
        return self.distance

    # used in the prim's mst, gets the previous element which is a new
    # field added to the Vertex class
    def set_previous(self, prev):
        self.previous = prev

    def __str__(self):
        return '{} neighbors: {}'.format(
            self.key,
            [x.key for x in self.neighbors]
        )


class Graph():
    def __init__(self):
        self.verticies = {}

    # so that we are able to iterate over the values of the dictionary
    # that is provided to us in the graph
    def __iter__(self):
        return iter(self.verticies.values())

    def add_vertex(self, vertex):
        self.verticies[vertex.key] = vertex

    def get_vertex(self, key):
        try:
            return self.verticies[key]
        except KeyError:
            return None

    def __contains__(self, key):
        return key in self.verticies

    def add_edge(self, from_key, to_key, weight=0):
        if from_key not in self.verticies:
            return False
        elif to_key not in self.vertices:
            return False
        else:
            # adds the weight from from not to toNode, then vide versa to account for
            # that edges have only one weight, not the one direction has a different weight than
            # the other
            self.vertices[from_key].add_neighbor(self.vertices[to_key], weight)
            self.vertices[to_key].add_neighbor(self.vertices[from_key], weight)

        return 'gay'

    def get_vertices(self):
        return self.verticies.keys()

    # 1.2 Breadth-First Search
    def Bfs(self):
        randIndex = random.randint(1, len(self.verticies)) - 1
        # visited = [False] * (len(self.verticies))
        # gets a random vertex
        x = self.get_vertex(randIndex)
        n = self.get_vertex(randIndex).get_connections()
        result = 0
        # the visited queue, append the elements starting with the first
        Q = [x]
        # visited[randIndex - 1] = True
        x.set_visited()
        # loop that goes until Q is empty
        while not Q:
            Q.pop(0)
            for y in n:
                # visited[y.get(y.key)] = True
                y.set_visited()
                Q.append(y)
                result = result + x.get_weight(y)
        return result

    # 1.3
    # For a BFS in a directed graph, each edge of the graph will either connects to two vertices at the
    # same level, goes down exactly one level, or will go up in any number of levels. So in the above code would
    # modify the for loop, so that in the code it just goes down one level at a time.


# 1.4 Prim's MST algorithm
def Mst(graph, startNode):
    # put tuple pair into priority queue
    # will be using a new distance field in the Vertex class
    # set the distance of the first selected vertex to 0
    startNode.set_distance(0)
    unvisitedQ = [(v.get_distance(), v) for v in graph]
    heapq.heapify(unvisitedQ)
    while len(unvisitedQ):
        # Pop a vertex with the smallest distance
        uv = heapq.heappop(unvisitedQ)
        current = uv[1]
        current.set_visited()
        result = 0
        # for the next in the v.adjacent
        for next in current.neighbours:
            # if node has been visited, will be skipped
            if next.visited:
                continue
            newDistance = current.get_distance() + current.get_weight(next)

            if newDistance < next.get_distance():
                next.set_distance(newDistance)
                next.set_previous(current)
                # where we add the results of the edges visited
            result = result + current.get_weight() + next.get_weight()
        return result


# Test Graph from 1.2
def testGraph():
    result = Graph()
    for i in range(0, 5 + 1):
        v = Vertex(i)
        result.add_vertex(v)
    # values to be used in the graph
    values = [[0, 15, 0, 7, 10, 0], [15, 0, 9, 11, 0, 9], [0, 9, 0, 0, 12, 7], [7, 11, 0, 0, 8, 14],
              [10, 0, 12, 8, 0, 8], [0, 9, 7, 14, 8, 0]]
    # going through length of the 2d array above
    for i in range(len(values)):
        fromV = result.get_vertex(i)
        # going though elements of the arrays
        for j in range(len(values[i])):
            toV = result.get_vertex(j)
            result.add_edge(fromV, toV)
    # returns the graph with specified weights
    return result


# 1.1 Random Graph Generation
# takes in a number, which is number of vertices
def init_random(vNum):
    result = Graph()
    keyList = []
    for k in range(1, vNum + 1):
        v = Vertex(k)
        result.add_vertex(v)
        keyList.append(k)
    for i in range(2, vNum + 1):
        x = random.randint(1, i - 1)  # x is a random number in range [1..i-1]
        # S be a randomly selected sample of x in value from the set
        # uses randome.choice(), from a list l, randomly gets number k of
        # elements
        S = random.choices(keyList[0:i - 1], k=x)
        for s in S:
            w = random.randint(10, 100)
            # add and edge
            # current vertex at index i
            curVertex = result.verticies.get(i)
            # next node element at index s
            nextVertex = result.verticies.get(s)
            # creates new edge from curVertex to nextVertex with weight w
            result.add_edge(curVertex, nextVertex, w)
    return result


# 1.5 compare BFS with prim's algorithm
def compare(k):
    # below is the algorithm given to us in teh section 1.5 of the assignment
    for n in [20, 40, 60]:
        Diff = 0
        for k in range(k):
            graph = init_random(n)
            B = graph.Bfs()
            P = Mst(graph, graph.get_vertex(1))
            Diff = Diff + (B - P) / P
            # prints out the averages which is the value of Diff over k
            # which is how many times the above for loop has ran
        print("Average of", k, "=", Diff / k)


# test for all of the methods
if __name__ == '__main__':
    # testing the random graph generator with n vertices
    test1 = init_random(7)
    # testing the testgraph that is given to us, then with bfs and prim's mst
    test2 = testGraph()
    print(test2.Bfs())
    test3 = testGraph()
    node = test3.get_vertex(1)
    print(Mst(test3, node))
    # testing the compare function of bfs and prim's mst
    compare(10)
