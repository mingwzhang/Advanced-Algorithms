# Import the heap queue module to use a min-heap
import heapq  

def Dijkstra_Algorithm(graph, source):
    # Create a new dictionay were all node distances are set to infinity
    distance = {node: float('inf') for node in graph}
    # Set source or starting distance to 0
    distance[source] = 0 
    # Priority queue will store tuples of (distance, node) to help select the closest node
    priority_queue = [(0, source)] 

    # The while loop runs until all reachable nodes are processed (priority_queue is empty)
    while priority_queue:
        # Extract the node with the shortest known distance
        current_distance, current_node = heapq.heappop(priority_queue)

        # Iterate over all neighbors of the current node
        for neighbor, weight in graph[current_node]:
            # Calculate the new tentative distance to the neighbor traveling the current node
            update_distance = current_distance + weight  

            # Condition to update the distance if the new distance is shorter
            if update_distance < distance[neighbor]:
                # Update the shortest distance for the neighbor
                distance[neighbor] = update_distance

                # Add the neighbor to the priority queue with the updated distance
                heapq.heappush(priority_queue, (update_distance, neighbor))
    print(distance)

# Graph Representation Input:
graph = {
    'A': [('B', 3), ('C', 2), ('D', 8)],
    'B': [('C', 1), ('E', 3)],
    'C': [('D', 4), ('E', 5)],
    'D': [('E', 5)],
    'E': []
}

# Print the graph representation to provide context before running the algorithm
print()
print("Graph")
for node in graph:
    print(f'{node}: {graph[node]}')

# Find and print the shortest path from the source node 'A' to all other nodes
print()
print("Shortest Path For Each Node:")
Dijkstra_Algorithm(graph, 'A')


