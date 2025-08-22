import heapq
import math

def best_first_search(grid):
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
    
    # priority queue for Best First Search
    pq = []
    heapq.heappush(pq, (heuristic(0, 0), 0, 0))
    
    # track visited nodes and their parents for path
    visited = [[False] * n for _ in range(n)]
    parent = [[None] * n for _ in range(n)]
    visited[0][0] = True
    
    while pq:
        _, x, y = heapq.heappop(pq)
        
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
        
        # explore neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # check if the neighbor is within bounds and is traversable
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                parent[nx][ny] = (x, y)
                heapq.heappush(pq, (heuristic(nx, ny), nx, ny))
    
    return -1, []

def test_algorithm():
    print("Example 1:")
    grid1 = [[0, 1],
             [1, 0]]
    
    bfs_len1, bfs_path1 = best_first_search(grid1)
    print(f"Best First Search → Path length: {bfs_len1}, Path: {bfs_path1}")
    print()
    
    print("Example 2:")
    grid2 = [[0, 0, 0],
             [1, 1, 0],
             [1, 1, 0]]
    
    bfs_len2, bfs_path2 = best_first_search(grid2)
    print(f"Best First Search → Path length: {bfs_len2}, Path: {bfs_path2}")
    print()
    
    print("Example 3:")
    grid3 = [[1, 0, 0],
             [1, 1, 0],
             [1, 1, 0]]
    
    bfs_len3, bfs_path3 = best_first_search(grid3)
    print(f"Best First Search → Path length: {bfs_len3}, Path: {bfs_path3}")
    
if __name__ == "__main__":
    test_algorithm()
