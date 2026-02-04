def manhattanDistance(state, n):
    dist = 0
    for i in range(n * n):
        if state[i] == 'X': continue
        
        curr_row, curr_col = divmod(i, n)
        goal_row, goal_col = divmod(state[i] - 1, n)
        
        dist += abs(curr_row - goal_row) + abs(curr_col - goal_col)

    return dist

def astar(state, n):
    dirs = (-n, n, -1, 1)
    return manhattanDistance(state, n)
    # pass