import random

def shuffle(state, null_pos, n):
    variation_size = random.randint(30, 200)
    dirs = [(0,-1),(-1,0),(0,1),(1,0)]
    while variation_size > 0:
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
    return state, null_pos