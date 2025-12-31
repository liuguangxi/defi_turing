from collections import deque

def solve():
    """
    Solves the file shelf puzzle:
    - 8 shelves (E1-E4 top, E8-E5 bottom) arranged in a 2x4 grid.
    - 7 files (D1-D7) messily placed, with one empty shelf.
    - Objective: Reach the goal state where each file i is on shelf i (S1:D1... S7:D7).
    - Find the minimum moves A and the state B after move p = floor((A+1)/2).
    - Return A * B.
    """

    # Adjacency graph based on the shelf layout labels:
    # 1 - 2 - 3 - 4
    # |   |   |   |
    # 8 - 7 - 6 - 5
    # indices 0-7 represent shelves 1-8.
    adj = {
        0: [1, 7],    # S1 connects to S2, S8
        1: [0, 2, 6], # S2 connects to S1, S3, S7
        2: [1, 3, 5], # S3 connects to S2, S4, S6
        3: [2, 4],    # S4 connects to S3, S5
        4: [3, 5],    # S5 connects to S4, S6
        5: [4, 6, 2], # S6 connects to S5, S7, S3
        6: [5, 7, 1], # S7 connects to S6, S8, S2
        7: [6, 0]     # S8 connects to S7, S1
    }

    # Initial state provided in the problem (S1...S8): 5, 0, 6, 2, 1, 7, 4, 3
    # Matches the visual arrangement:
    # S1:5, S2:Empty, S3:6, S4:2
    # S8:3, S7:4, S6:7, S5:1
    start = (5, 0, 6, 2, 1, 7, 4, 3)

    # Goal state: File i is on shelf i for i=1..7. Shelf 8 is empty (0).
    goal = (1, 2, 3, 4, 5, 6, 7, 0)

    # BFS to find the shortest path (minimum moves A)
    queue = deque([(start, [])])
    visited = {start}

    while queue:
        state, path = queue.popleft()

        if state == goal:
            # A is the number of moves (path length)
            A = len(path)
            # p is the integer part of (A+1)/2
            p = (A + 1) // 2
            # B is the 8-digit number representing the shelf state after move p
            # The state after the p-th move is the p-th element in the path list.
            B_tuple = path[p - 1]
            B = int("".join(map(str, B_tuple)))
            print(f"A = {A}, B = {B}")
            return A * B

        # Find the empty shelf (0) to identify valid moves
        empty_pos = state.index(0)

        for neighbor in adj[empty_pos]:
            # Sliding a file from a neighbor to the empty spot
            new_state = list(state)
            new_state[empty_pos], new_state[neighbor] = new_state[neighbor], new_state[empty_pos]
            t_state = tuple(new_state)

            if t_state not in visited:
                visited.add(t_state)
                # Store the resulting state in the path
                queue.append((t_state, path + [t_state]))

# The resulting product of the minimum moves A and the state number B after p moves
print(solve())
