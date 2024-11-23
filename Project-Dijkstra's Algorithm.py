import heapq  # Import the heap queue module to use a min-heap (priority queue)

def Dijkstra_Algorithm(graph, source):
    distance = {node: float('inf') for node in graph}  # Create a new dictionay were all node distances are set to infinity
    distance[source] = 0 # Set source or starting distance to 0
    
    priority_queue = [(0, source)] 
    
    while priority_queue:  #The while loop will iterate until priority_queue is empty / every node in the heap are poped
        current_distance, current_node = heapq.heappop(priority_queue) # 
        for neighbor, weight in graph[current_node]:
            update_distance = current_distance + weight  #Setting update_distance based on current distance to neighbor distance
            if update_distance < distance[neighbor]:  #Condition to update the distance if the new distance is shorter
                distance[neighbor] = update_distance
                heapq.heappush(priority_queue, (update_distance, neighbor))
    print(distance)
    
graph = {
    'A': [('B', 3), ('C', 2), ('D', 8)],
    'B': [('C', 1), ('E', 3)],
    'C': [('D', 4), ('E', 5)],
    'D': [('E', 5)],
    'E': []
}

print()
print("Graph")
for node in graph:
    print(f'{node}: {graph[node]}')

print()
print("Shortest Path For Each Node:")
Dijkstra_Algorithm(graph, 'A')


