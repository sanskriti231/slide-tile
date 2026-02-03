from bfs import *
from shuffle import *

def printTile(state, n):
    for i in range(n * n):
        print(state[i], end="\t")
        if (i + 1) % n == 0: print()

n = 3
null_pos = [2,2]
target_state = [[1,2,3],[4,5,6],[7,8,'X']]
initial_state, null_pos = shuffle(target_state, null_pos, n)
initial_state = tuple(x for row in initial_state for x in row)
target_state = (1,2,3,4,5,6,7,8,'X')
print("Initial state: ")
printTile(initial_state, n)
print()
visited = set()
solved_state, num_moves = bfs(initial_state, target_state)
print("Solved state: ")
printTile(solved_state, n)
print()
print("Min. number of moves: ", num_moves)