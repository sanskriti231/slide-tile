import random

def shuffle(state, null_pos, n):
    variation_size = random.randint(30, 200)
    state = list(state)
    dirs = (n, -n, 1, -1)
    while variation_size > 0:
        ran_action = random.randint(0, 3)
        x = null_pos
        new_x = x + dirs[ran_action]
        while new_x < 0 or new_x >= n * n or (new_x % n == 0 and x - 1 == new_x) or (x % n == 0 and new_x == x + 1):
            ran_action = random.randint(0, 3)
            new_x = x + dirs[ran_action]

        state[x], state[new_x] = state[new_x], state[x]
        null_pos = new_x
        variation_size -= 1
    return tuple(state), null_pos