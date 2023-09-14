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