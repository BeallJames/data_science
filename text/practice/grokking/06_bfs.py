from collections import deque

graph = {}

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

def person_is_seller(name):
    return name[-1] == 'm'

graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "johny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["johny"] = []

search("you")

# Output:
# thom is a mango seller!

# Time complexity: O(V+E)
# V = number of vertices
# E = number of edges

# Breadth-first search is used to find the shortest path between two nodes
# in an unweighted graph.
# If you add a weight to each edge, the algorithm becomes a more general
# algorithm called Dijkstra's algorithm.