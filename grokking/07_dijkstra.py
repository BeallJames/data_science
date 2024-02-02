graph = {}

graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["finish"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["finish"] = 5

graph["finish"] = {}


costs = {}
costs["a"] = 6
costs["b"] = 2
costs["finish"] = float("inf")


parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["finish"] = None

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    # print('neighbors:', neighbors)
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if new_cost < costs[n]:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)
    
def print_path():
    finish = 'finish'
    path = []
    while finish is not None:
        path.append(finish)
        # finish = parents[finish] see below
        finish = parents.get(finish)
    for node in reversed(path):
        print(node)

print_path()


# The difference lies in how these two expressions handle cases where the key finish is not present in the parents dictionary.

# parents[finish]: This expression directly accesses the value associated with the key finish in the parents dictionary. If the key is not present, it will raise a KeyError.

# parents.get(finish): This expression uses the get method of dictionaries. It returns the value associated with the key finish if the key is present. If the key is not present, it returns None by default (or you can provide a default value as the second argument to get).

# In the context of the print_path function, using parents.get(finish) is a safer option because it prevents a KeyError from being raised if the key is not found. Instead, it gracefully returns None, allowing the loop to terminate without errors when it reaches the 'start' node.





# print(parents[parents['fin']])
# for i in parents:
#     print(i, parents[i])

# print(parents[parents[parents['fin']]], parents[parents['fin']], parents['fin'])