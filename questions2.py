# Artificial Intelligence Assignment - 1
# Problem 2: Bridge Crossing Problem (BFS and DFS)

from collections import deque

# Each state: (frozenset of left side, frozenset of right side, umbrella side, time elapsed, path)
people = {'A': 5, 'B': 10, 'C': 20, 'D': 25}  # Amogh, Ameya, Grandmother, Grandfather

def bridge_bfs():
    start = (frozenset(people.keys()), frozenset(), 'L', 0, [])
    queue = deque([start])
    visited = set()
    while queue:
        left, right, umbrella, time, path = queue.popleft()
        state_id = (left, right, umbrella)
        if state_id in visited:
            continue
        visited.add(state_id)
        if len(left) == 0 and umbrella == 'R':
            return path, time
        if umbrella == 'L':
            # Move 1 or 2 people from left to right
            for p1 in left:
                for p2 in left:
                    if p1 < p2:
                        move = {p1, p2}
                        new_left = left - move
                        new_right = right | move
                        t = max(people[p1], people[p2])
                        new_path = path + [(f"{p1} and {p2} cross", t)]
                        queue.append((new_left, new_right, 'R', time + t, new_path))
                # Single person crosses
                move = {p1}
                new_left = left - move
                new_right = right | move
                t = people[p1]
                new_path = path + [(f"{p1} crosses", t)]
                queue.append((new_left, new_right, 'R', time + t, new_path))
        else:
            # Move 1 person back from right to left
            for p1 in right:
                move = {p1}
                new_left = left | move
                new_right = right - move
                t = people[p1]
                new_path = path + [(f"{p1} returns", t)]
                queue.append((new_left, new_right, 'L', time + t, new_path))
    return None, None

def bridge_dfs():
    start = (frozenset(people.keys()), frozenset(), 'L', 0, [])
    stack = [start]
    visited = set()
    while stack:
        left, right, umbrella, time, path = stack.pop()
        state_id = (left, right, umbrella)
        if state_id in visited:
            continue
        visited.add(state_id)
        if len(left) == 0 and umbrella == 'R':
            return path, time
        if umbrella == 'L':
            for p1 in left:
                for p2 in left:
                    if p1 < p2:
                        move = {p1, p2}
                        new_left = left - move
                        new_right = right | move
                        t = max(people[p1], people[p2])
                        new_path = path + [(f"{p1} and {p2} cross", t)]
                        stack.append((new_left, new_right, 'R', time + t, new_path))
                move = {p1}
                new_left = left - move
                new_right = right | move
                t = people[p1]
                new_path = path + [(f"{p1} crosses", t)]
                stack.append((new_left, new_right, 'R', time + t, new_path))
        else:
            for p1 in right:
                move = {p1}
                new_left = left | move
                new_right = right - move
                t = people[p1]
                new_path = path + [(f"{p1} returns", t)]
                stack.append((new_left, new_right, 'L', time + t, new_path))
    return None, None

def print_bridge_solution(path, total_time):
    if path is None:
        print("No solution found.")
        return
    for step, t in path:
        print(f"{step} ({t} min)")
    print(f"Total time: {total_time} min")

if __name__ == "__main__":
    print("--- Bridge Crossing Problem (BFS) ---")
    path, total_time = bridge_bfs()
    print_bridge_solution(path, total_time)

    print("\n--- Bridge Crossing Problem (DFS) ---")
    path, total_time = bridge_dfs()
    print_bridge_solution(path, total_time)
