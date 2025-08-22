import heapq
import math

def a_star_search(grid):
    n = len(grid)
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1, []
    
    # 8 possible movement directions (horizontal, vertical, diagonal)
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),           (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]
    
    # heuristic function (Euclidean distance)
    def heuristic(x, y):
        return math.sqrt((n-1-x)**2 + (n-1-y)**2)
    
    # priority queue for A* Search
    pq = []
    heapq.heappush(pq, (heuristic(0, 0), 0, 0, 0))  # (f, g, x, y)
    
    # track visited nodes, their g-values, and parents for path reconstruction
    g_values = [[float('inf')] * n for _ in range(n)]
    g_values[0][0] = 0
    parent = [[None] * n for _ in range(n)]
    
    while pq:
        f, g, x, y = heapq.heappop(pq)
        
        # check if we reached the goal
        if x == n-1 and y == n-1:
            # reconstruct path
            path = []
            while (x, y) != (0, 0):
                path.append((x, y))
                x, y = parent[x][y]
            path.append((0, 0))
            path.reverse()
            return len(path), path
        
        # skip if we found a better path to this node already
        if g > g_values[x][y]:
            continue
            
        # explore neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # check if the neighbor is within bounds and is traversable
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                # cost to move to neighbor (1 for horizontal/vertical, sqrt(2) for diagonal)
                cost = 1 if dx == 0 or dy == 0 else math.sqrt(2)
                new_g = g + cost
                
                # if we found a better path to this neighbor
                if new_g < g_values[nx][ny]:
                    g_values[nx][ny] = new_g
                    parent[nx][ny] = (x, y)
                    f_value = new_g + heuristic(nx, ny)
                    heapq.heappush(pq, (f_value, new_g, nx, ny))
    
    return -1, []

def test_algorithm():
    print("Example 1:")
    grid1 = [[0, 1],
             [1, 0]]
    
    astar_len1, astar_path1 = a_star_search(grid1)
    print(f"A* Search → Path length: {astar_len1}, Path: {astar_path1}")
    print()
    
    print("Example 2:")
    grid2 = [[0, 0, 0],
             [1, 1, 0],
             [1, 1, 0]]
    astar_len2, astar_path2 = a_star_search(grid2)
    print(f"A* Search → Path length: {astar_len2}, Path: {astar_path2}")
    print()
    
    print("Example 3:")
    grid3 = [[1, 0, 0],
             [1, 1, 0],
             [1, 1, 0]]
    astar_len3, astar_path3 = a_star_search(grid3)
    print(f"A* Search → Path length: {astar_len3}, Path: {astar_path3}")

if __name__ == "__main__":
    test_algorithm()

