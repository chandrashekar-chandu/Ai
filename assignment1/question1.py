# Artificial Intelligence Assignment - 1
# Problem 1: Rabbit Leap Problem (BFS and DFS)

from collections import deque

# --- Problem 1: Rabbit Leap Problem ---

def rabbit_leap_bfs(start, goal):
    visited = set()
    queue = deque([(start, [start])])
    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path
        visited.add(state)
        for next_state in rabbit_leap_moves(state):
            if next_state not in visited:
                queue.append((next_state, path + [next_state]))
    return None

def rabbit_leap_dfs(start, goal):
    visited = set()
    stack = [(start, [start])]
    while stack:
        state, path = stack.pop()
        if state == goal:
            return path
        visited.add(state)
        for next_state in rabbit_leap_moves(state):
            if next_state not in visited:
                stack.append((next_state, path + [next_state]))
    return None

def rabbit_leap_moves(state):
    state = list(state)
    moves = []
    for i, c in enumerate(state):
        if c == 'E':
            # Move right
            if i+1 < len(state) and state[i+1] == '_':
                new = state.copy()
                new[i], new[i+1] = new[i+1], new[i]
                moves.append(tuple(new))
            # Jump over one rabbit
            if i+2 < len(state) and state[i+1] in 'EW' and state[i+2] == '_':
                new = state.copy()
                new[i], new[i+2] = new[i+2], new[i]
                moves.append(tuple(new))
        elif c == 'W':
            # Move left
            if i-1 >= 0 and state[i-1] == '_':
                new = state.copy()
                new[i], new[i-1] = new[i-1], new[i]
                moves.append(tuple(new))
            # Jump over one rabbit
            if i-2 >= 0 and state[i-1] in 'EW' and state[i-2] == '_':
                new = state.copy()
                new[i], new[i-2] = new[i-2], new[i]
                moves.append(tuple(new))
    return moves

def print_rabbit_leap_solution(path):
    for state in path:
        print(''.join(state))
    print(f"Total moves: {len(path)-1}")

if __name__ == "__main__":
    print("--- Rabbit Leap Problem (BFS) ---")
    start = ('E', 'E', 'E', '_', 'W', 'W', 'W')
    goal = ('W', 'W', 'W', '_', 'E', 'E', 'E')
    path = rabbit_leap_bfs(start, goal)
    print_rabbit_leap_solution(path)

    print("\n--- Rabbit Leap Problem (DFS) ---")
    path = rabbit_leap_dfs(start, goal)
    print_rabbit_leap_solution(path)
