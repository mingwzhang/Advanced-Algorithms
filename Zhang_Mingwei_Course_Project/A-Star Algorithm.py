import heapq
import time

def astar_algorithm(graph, start, goal, heuristic):
    if start not in graph or goal not in graph:
        return "Failure: Start or goal node not in the graph."
    
    # Priority queue for open nodes
    open_set = []
    heapq.heappush(open_set, (0, start))
    open_set_tracker = {start}  # Set for fast lookup of open nodes

    # For reconstructing the path
    came_from = {}

    # Cost from start to a node
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    # Estimated total cost from start to goal through a node
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic(start, goal)

    nodes_expanded = 0
    start_time = time.time()

    while open_set:
        nodes_expanded += 1
        # Node with the lowest f_score
        current = heapq.heappop(open_set)[1]
        open_set_tracker.remove(current)

        # Goal reached
        if current == goal:
            print(f"Nodes expanded: {nodes_expanded}")
            print(f"Execution time: {time.time() - start_time:.4f} seconds")
            return reconstruct_path(came_from, current)

        # Check all neighbors
        for neighbor, weight in graph[current]:
            tentative_g_score = g_score[current] + weight
            if tentative_g_score < g_score[neighbor]:
                # Update path and scores
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                if neighbor not in open_set_tracker:
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
                    open_set_tracker.add(neighbor)

    # No path found
    print(f"Nodes expanded: {nodes_expanded}")
    print(f"Execution time: {time.time() - start_time:.4f} seconds")
    return "Failure: No path exists from start to goal"

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]

def heuristic(node, goal):
    # ASCII-based placeholder heuristic
    return abs(ord(node) - ord(goal))

# Example graph
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('E', 4)],
    'C': [('E', 1)],
    'D': [('G', 2)],
    'E': [('G', 3)],
    'G': []
}

# Define start and goal
start = 'A'
goal = 'G'

# Run A* algorithm
path = astar_algorithm(graph, start, goal, heuristic)
print("Path from start to goal:", path)
