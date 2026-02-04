import sys
from shuffle import *
from astar import astar

n = int(sys.argv[1])
if n < 2: 
    print("Invalid board size.")
    sys.exit()

def printTile(state, n):
    for i in range(n * n):
        print(state[i], end="\t")
        if (i + 1) % n == 0: print()

target_state = tuple(range(1,n*n)) + ('X',)
null_pos = n*n - 1
initial_state, null_pos = shuffle(target_state, null_pos, n)
print(initial_state)
printTile(initial_state, n)
print()
print(astar(initial_state, n))
# printTile(astar(initial_state, n), n)