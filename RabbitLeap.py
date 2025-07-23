from collections import deque

class RabbitLeapSolver:
    def __init__(self):
        self.initial_state = ['E', 'E', 'E', '_', 'W', 'W', 'W']
        self.goal_state = ['W', 'W', 'W', '_', 'E', 'E', 'E']

    def get_neighbors(self, state):
        neighbors = []
        idx = state.index('_')
        directions = [-1, -2, 1, 2]  # Possible move positions

        for d in directions:
            new_idx = idx + d
            if 0 <= new_idx < len(state):
                if abs(d) == 1:
                    # Move one step: E moves right, W moves left
                    if (state[new_idx] == 'E' and d == -1) or (state[new_idx] == 'W' and d == 1):
                        new_state = state[:]
                        new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
                        neighbors.append(new_state)
                elif abs(d) == 2:
                    # Jump over one rabbit
                    if (state[idx + d // 2] != '_') and \
                       ((state[new_idx] == 'E' and d == -2) or (state[new_idx] == 'W' and d == 2)):
                        new_state = state[:]
                        new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
                        neighbors.append(new_state)
        return neighbors

    def bfs(self):
        queue = deque()
        visited = set()
        queue.append((self.initial_state, [self.initial_state]))

        while queue:
            current, path = queue.popleft()
            state_str = ''.join(current)

            if state_str in visited:
                continue
            visited.add(state_str)

            if current == self.goal_state:
                return path

            for neighbor in self.get_neighbors(current):
                queue.append((neighbor, path + [neighbor]))

        return None

    def dfs(self):
        stack = [(self.initial_state, [self.initial_state])]
        visited = set()

        while stack:
            current, path = stack.pop()
            state_str = ''.join(current)

            if state_str in visited:
                continue
            visited.add(state_str)

            if current == self.goal_state:
                return path

            for neighbor in self.get_neighbors(current):
                stack.append((neighbor, path + [neighbor]))

        return None

# Example usage:
if __name__ == "__main__":
    solver = RabbitLeapSolver()

    print("BFS Solution: ")
    bfs_solution = solver.bfs()
    for step in bfs_solution:
        print(step)

    print("DFS Solution: ")
    dfs_solution = solver.dfs()
    for step in dfs_solution:
        print(step)

