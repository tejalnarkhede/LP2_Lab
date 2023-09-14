import heapq #module used to represent priority queue

def dijkstra(graph, start):
    distance = {node: float('inf') for node in graph}
    distance[start] = 0

    pq = [(0, start)]

    while pq:
        curr_dist, curr_node = heapq.heappop(pq) #return smallest element
        if curr_dist > distance[curr_node]:
            continue
        for neighbor, weight in graph[curr_node].items():
            new_dist = distance[curr_node] + weight
            if new_dist < distance[neighbor]:
                distance[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    return distance
	
graph = {}
num_nodes = int(input("\nNumber of nodes: "))
for i in range(num_nodes):
    node = input(f"Name of Node {i+1}: ")
    num_edges = int(input(f"\nNumber of Edges for Node {node}: "))
    edges = {}
    for j in range(num_edges):
        neighbor = input(f"\nName of Neighbor {j+1}: ")
        weight = int(input(f"Enter the weight for edge {node}-{neighbor}: "))
        edges[neighbor] = weight
    graph[node] = edges
    
start_node = input("Enter the starting node: ")
result = dijkstra(graph, start_node)

for node, dist in result.items():
    print(f"Shortest distance from {start_node} to {node}: {dist}")
    
# ------------------------------------------------------------------------------------------    
#  Output:
 
#  Number of nodes: 6
# Name of Node 1: A

# Number of Edges for Node A: 2

# Name of Neighbor 1: B
# Enter the weight for edge A-B: 7

# Name of Neighbor 2: C
# Enter the weight for edge A-C: 12
# Name of Node 2: B

# Number of Edges for Node B: 2

# Name of Neighbor 1: C
# Enter the weight for edge B-C: 2

# Name of Neighbor 2: D
# Enter the weight for edge B-D: 9
# Name of Node 3: C

# Number of Edges for Node C: 1

# Name of Neighbor 1: E
# Enter the weight for edge C-E: 10
# Name of Node 4: D

# Number of Edges for Node D: 1

# Name of Neighbor 1: F
# Enter the weight for edge D-F: 1
# Name of Node 5: E

# Number of Edges for Node E: 2

# Name of Neighbor 1: D
# Enter the weight for edge E-D: 4

# Name of Neighbor 2: F
# Enter the weight for edge E-F: 5
# Name of Node 6: F

# Number of Edges for Node F: 0
# Enter the starting node: A
# Shortest distance from A to A: 0
# Shortest distance from A to B: 7
# Shortest distance from A to C: 9
# Shortest distance from A to D: 16
# Shortest distance from A to E: 19
# Shortest distance from A to F: 17