from collections import deque

class BridgeCrossingSolver:
    def __init__(self):
        # Crossing times for each person
        self.people = {
            'Suprith': 5,
            'Amulya': 10,
            'Mahi': 20,
            'Shravan': 25
        }
        # Initial state: (left_set, right_set, time, umbrella_side)
        self.initial_state = (frozenset(self.people.keys()), frozenset(), 0, 'L')

    def goal_condition(self, state):
        left, right, time_so_far, side = state
        return len(left) == 0 and side == 'R' and time_so_far <= 60

    def get_successors(self, state):
        left, right, time_so_far, side = state
        successors = []

        if side == 'L':
            left_list = list(left)
            for i in range(len(left_list)):
                for j in range(i + 1, len(left_list)):
                    p1, p2 = left_list[i], left_list[j]
                    new_left = left.difference({p1, p2})
                    new_right = right.union({p1, p2})
                    crossing_time = max(self.people[p1], self.people[p2])
                    new_time = time_so_far + crossing_time
                    if new_time <= 60:
                        new_state = (frozenset(new_left), frozenset(new_right), new_time, 'R')
                        action = f"{p1} and {p2} cross right ({crossing_time} min)"
                        successors.append((new_state, action, new_time))
        else:
            right_list = list(right)
            for person in right_list:
                new_left = left.union({person})
                new_right = right.difference({person})
                crossing_time = self.people[person]
                new_time = time_so_far + crossing_time
                if new_time <= 60:
                    new_state = (frozenset(new_left), frozenset(new_right), new_time, 'L')
                    action = f"{person} returns left ({crossing_time} min)"
                    successors.append((new_state, action, new_time))

        return successors

    def bfs(self):
        queue = deque()
        visited = set()
        queue.append((self.initial_state, [], 0))

        while queue:
            current_state, path, time_so_far = queue.popleft()

            if self.goal_condition(current_state):
                return path + [(current_state, "Goal reached", time_so_far)]

            state_id = (current_state[0], current_state[1], current_state[3], current_state[2])  # include time
            if state_id in visited:
                continue
            visited.add(state_id)

            for next_state, action, next_time in self.get_successors(current_state):
                queue.append((next_state, path + [(current_state, action, time_so_far)], next_time))

        return None

    def dfs(self):
        stack = [(self.initial_state, [], 0)]
        visited = set()

        while stack:
            current_state, path, time_so_far = stack.pop()

            if self.goal_condition(current_state):
                return path + [(current_state, "Goal reached", time_so_far)]

            state_id = (current_state[0], current_state[1], current_state[3], current_state[2])  # include time
            if state_id in visited:
                continue
            visited.add(state_id)

            for next_state, action, next_time in self.get_successors(current_state):
                stack.append((next_state, path + [(current_state, action, time_so_far)], next_time))

        return None


if __name__ == "__main__":
    solver = BridgeCrossingSolver()

    print("BFS Solution (Optimal):")
    bfs_solution = solver.bfs()
    if bfs_solution:
        for state, action, time in bfs_solution:
            left, right, _, side = state
            print(f"Time: {time} min | Left: {sorted(left)} | Right: {sorted(right)} | Side: {side} | {action}")
        print(f"Total Time: {bfs_solution[-1][2]} minutes")
    else:
        print("No BFS solution found.")

    print("\n DFS Solution: ")
    dfs_solution = solver.dfs()
    if dfs_solution:
        for state, action, time in dfs_solution:
            left, right, _, side = state
            print(f"Time: {time} min | Left: {sorted(left)} | Right: {sorted(right)} | Side: {side} | {action}")
        print(f"\n Total Time: {dfs_solution[-1][2]} minutes")
    else:
        print(" No DFS solution found.")

