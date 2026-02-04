from heapq import *

def manhattanDistance(state, n):
    dist = 0
    for i in range(n * n):
        if state[i] == 'X': continue
        
        curr_row, curr_col = divmod(i, n)
        goal_row, goal_col = divmod(state[i] - 1, n)
        
        dist += abs(curr_row - goal_row) + abs(curr_col - goal_col)

    return dist

def validMoves(n):
    moves = []
    for i in range(n * n):
        movesx = []
        row, col = divmod(i, n)
        if row > 0: movesx.append(-n)
        if row < n - 1: movesx.append(n)
        if col > 0: movesx.append(-1)
        if col < n - 1: movesx.append(1)

        moves.append(movesx)
    return moves

def astar(state, n, null_pos, goal):
    pq = []
    hf = manhattanDistance(state, n)
    heappush(pq, (hf, 1, null_pos, state))
    moves = validMoves(n)
    visited = set()
    visited.add(state)
    while pq:
        cost, level, npos, front = heappop(pq)
        if front == goal: return front, level
        m = moves[npos]
        x = npos
        for action in m:
            new_x = x + action
            newstate = list(front)
            newstate[x], newstate[new_x] = newstate[new_x], newstate[x]
            newstate = tuple(newstate)
            if newstate in visited: continue
            visited.add(newstate)
            cost = manhattanDistance(newstate, n) + level + 1
            heappush(pq, (cost, level + 1, new_x, newstate))

    return None, -1