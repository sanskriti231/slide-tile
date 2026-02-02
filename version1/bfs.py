from queue import *

dirs = [[1,3],[0,2,4],[1,5],
        [0,4,6],[1,3,5,7],[2,4,8],
        [3,7],[6,4,8],[5,7]]

def bfs(state, goal):
    if state == goal: return state, 0
    q = Queue()
    q.push([state, 0])
    visited = set()
    visited.add(state)

    while not q.isEmpty():
        front, dist = q.front()
        q.pop()
        if front == goal: return [front, dist]
        idx = front.index('X')
        for x in dirs[idx]:
            newstate = list(front)
            newstate[idx], newstate[x] = newstate[x], newstate[idx]
            newstate = tuple(newstate)
            if newstate in visited: continue
            q.push([newstate, dist + 1])
            visited.add(newstate)
    return None, -1
