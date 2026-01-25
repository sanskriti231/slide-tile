from queue import *
import random

def shuffle(state, null_pos, n):
    variation_size = random.randint(30, 200)
    while variation_size > 0:
        dirs = [(0,-1),(-1,0),(0,1),(1,0)]
        ran_action = random.randint(0, 3)
        new_x = dirs[ran_action][0] + null_pos[0]
        new_y = dirs[ran_action][1] + null_pos[1]
        while new_x < 0 or new_x >= n or new_y < 0 or new_y >= n:
            ran_action = random.randint(0, 3)
            new_x = dirs[ran_action][0] + null_pos[0]
            new_y = dirs[ran_action][1] + null_pos[1]
        
        x, y = null_pos
        state[x][y], state[new_x][new_y] = state[new_x][new_y], state[x][y]
        null_pos = [new_x, new_y]
        variation_size -= 1
    return state

def printTile(state):
    for row in state:
        for char in row:
            print(char, end = " ")
        print()


# n = 3
# null_pos = [2,2]
# target_state = [[1,2,3],[4,5,6],[7,8,'X']]

n = 4
null_pos = [3,3]
target_state = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,'X']]
initial_state = shuffle(target_state, null_pos, n)
printTile(initial_state)

# def bfs(state, npos):
#     if state == target_state: return state
#     q = Queue()
#     q.enqueue([state, npos])
#     dirs = [[-1, 0], [0, -1], [0, 1], [1, 0]]
#     while 
