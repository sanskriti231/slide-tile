import sys
from shuffle import *
from astar import astar

if len(sys.argv) < 2: 
    print("Board size expected as a command line argument.")
    sys.exit()

n = int(sys.argv[1])
if n < 2 or n > 4: 
    print("Invalid board size.")
    sys.exit()

def printTile(state, n):
    for i in range(n * n):
        print(state[i], end="\t")
        if (i + 1) % n == 0: print()

target_state = tuple(range(1,n*n)) + ('X',)
null_pos = n*n - 1
initial_state, null_pos = shuffle(target_state, null_pos, n)
print("Initial state:")
printTile(initial_state, n)
print()
solved_state, level = astar(initial_state, n, null_pos, target_state)
print("Solved state:")
printTile(solved_state, n)
print("Minimum number of moves =", level)