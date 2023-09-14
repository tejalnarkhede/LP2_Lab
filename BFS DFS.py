from collections import deque

def dfs(graph, start_vertex, visited):
    visited.add(start_vertex)
    print(start_vertex, end=' ')
    for neighbor in graph[start_vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def bfs(graph, start_vertex):
    visited = set()
    queue = deque([start_vertex])
    visited.add(start_vertex)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

def main():
    graph = {}

    num_vertices = int(input("Enter the number of vertices: "))
    for i in range(num_vertices):
        vertex = input("Vertex {}: ".format(i+1))
        graph[vertex] = set()

    num_edges = int(input("Enter the number of edges: "))

    for i in range(num_edges):
        edge = input("Edge {}: ".format(i+1))
        vertex1, vertex2 = edge.split()
        graph[vertex1].add(vertex2)
        graph[vertex2].add(vertex1)

    visited = set()

    start_vertex = input("\nStart Vertex: ")
    print("\n\nDFS traversal:")

    dfs(graph, start_vertex, visited)

    print("\n\nBFS traversal:")
    bfs(graph, start_vertex)

# Run the main function
if __name__ == "__main__":
    main()


# #output
# Enter the number of vertices: 7
# Vertex 1: A
# Vertex 2: B
# Vertex 3: C
# Vertex 4: D
# Vertex 5: E
# Vertex 6: F
# Vertex 7: G
# Enter the number of edges: 7
# Edge 1: A B
# Edge 2: A D
# Edge 3: B C
# Edge 4: D C
# Edge 5: C E
# Edge 6: E F
# Edge 7: E G

# Start Vertex: A


# DFS traversal:
# A B C E G F D 

# BFS traversal:
# A B D C E G F 