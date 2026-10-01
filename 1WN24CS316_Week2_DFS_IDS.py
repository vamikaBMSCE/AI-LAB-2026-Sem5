# 8-Puzzle Problem Implementation using DFS and IDS

GOAL_STATE = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def print_board(state):
    """Displays 3x3 board layout with '_' representing the empty tile."""
    for i in range(0, 9, 3):
        row = ["_" if tile == 0 else str(tile) for tile in state[i:i+3]]
        print(" " + " | ".join(row))
    print()

def get_neighbors(state):
    """Generates next valid states by sliding the blank space (0) Up, Down, Left, or Right."""
    zero_idx = state.index(0)
    r, c = divmod(zero_idx, 3)
    neighbors = []
    
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dr, dc in moves:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            n_idx = nr * 3 + nc
            new_state = list(state)
            new_state[zero_idx], new_state[n_idx] = new_state[n_idx], new_state[zero_idx]
            neighbors.append(tuple(new_state))
            
    return neighbors

def dfs(start, goal, max_depth=20):
    """Depth-First Search using an explicit stack."""
    stack = [(start, [start])]
    visited = {start}
    
    while stack:
        current, path = stack.pop()
        
        if current == goal:
            return path
            
        if len(path) - 1 < max_depth:
            for neighbor in get_neighbors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append((neighbor, path + [neighbor]))
                    
    return None

def dls(current, goal, depth, path, visited):
    """Helper function: Depth-Limited Search (DLS)."""
    if current == goal:
        return path
    if depth <= 0:
        return None
        
    for neighbor in get_neighbors(current):
        if neighbor not in visited:
            visited.add(neighbor)
            result = dls(neighbor, goal, depth - 1, path + [neighbor], visited)
            if result is not None:
                return result
            visited.remove(neighbor)
            
    return None

def ids(start, goal, max_depth=50):
    """Iterative Deepening Search that gradually increases the depth limit."""
    for depth in range(max_depth + 1):
        visited = {start}
        result = dls(start, goal, depth, [start], visited)
        if result is not None:
            return result
    return None

if __name__ == "__main__":
    # Start state (2 moves away from goal)
    start_state = (1, 2, 3, 
                   4, 0, 6, 
                   7, 5, 8)

    print("=" * 40)
    print("START STATE:")
    print_board(start_state)
    print("GOAL STATE:")
    print_board(GOAL_STATE)
    print("=" * 40)

    # Execute DFS
    print("\n--- 1. Depth-First Search (DFS) ---")
    dfs_path = dfs(start_state, GOAL_STATE)
    if dfs_path:
        print(f"DFS found solution in {len(dfs_path) - 1} moves:\n")
        for step, state in enumerate(dfs_path):
            print(f"Step {step}:")
            print_board(state)
    else:
        print("DFS failed to find a solution.")

    # Execute IDS
    print("\n--- 2. Iterative Deepening Search (IDS) ---")
    ids_path = ids(start_state, GOAL_STATE)
    if ids_path:
        print(f"IDS found solution in {len(ids_path) - 1} moves:\n")
        for step, state in enumerate(ids_path):
            print(f"Step {step}:")
            print_board(state)
    else:
        print("IDS failed to find a solution.")