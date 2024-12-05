import heapq

def astar_algorithm(graph, start, goal):
    open_set = []  # Using a heap as a priority queue
    heapq.heappush(open_set, (0, start))
    
    came_from = {}  # To keep track of the path
    
    g_score = {node: float('inf') for node in graph}  # Initialize g_scores to infinity
    g_score[start] = 0  # Starting point has a g_score of 0
    
    f_score = {node: float('inf') for node in graph}  # Initialize f_scores to infinity
    f_score[start] = g_score[start]  # f_score for start node
    
    while open_set:
        current = heapq.heappop(open_set)[1]  # Pop the node with the lowest f_score
        
        if current == goal:  # Goal has been reached
            return reconstruct_path(came_from, current)
        
        for neighbor, weight in graph[current]:
            tentative_g_score = g_score[current] + weight
            
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor]
                heapq.heappush(open_set, (f_score[neighbor], neighbor))
                
    return "Failure: Path not found"

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    return total_path[::-1]

# Example usage
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('E', 4)],
    'C': [('E', 1)],
    'D': [('G', 2)],
    'E': [('G', 3)],
    'G': []
}

start = 'A'
goal = 'G'

path = astar_algorithm(graph, start, goal)
print("Path from start to goal:", path)
