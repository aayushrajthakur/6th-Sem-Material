from collections import deque
import matplotlib.pyplot as plt
import numpy as np

def bfs(grid, start, destination):
    rows, cols = len(grid), len(grid[0])
    queue = deque([start])
    visited = set()
    visited.add(start)
    parent = {start: None} 

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] 

    while queue:
        current = queue.popleft()

        if current == destination:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return len(path) - 1, path[::-1] 

        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])

            if (0 <= neighbor[0] < rows and
                0 <= neighbor[1] < cols and
                grid[neighbor[0]][neighbor[1]] == 1 and
                neighbor not in visited):
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    return -1, []  # Return -1 if no path found

# Example usage
grid = [
    [1, 1, 0, 1],
    [0, 1, 0, 1],
    [1, 1, 1, 0],
    [0, 0, 1, 1]
]
start = (0, 0)
destination = (3, 3)
length, path = bfs(grid, start, destination)

# Output results
print("Length of shortest path:", length)
print("Path:", path)

# Visualization
def visualize_grid(grid, path):
    grid_np = np.array(grid)
    plt.imshow(grid_np, cmap='Greys', interpolation='nearest')
    
    if path:
        for (x, y) in path:
            plt.text(y, x, 'X', ha='center', va='center', color='red', fontsize=12)

    plt.title("Grid Visualization with Path")
    plt.axis("off")
    plt.show()

visualize_grid(grid, path)
