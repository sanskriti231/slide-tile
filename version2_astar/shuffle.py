import random

def shuffle(state, null_pos, n):
    variation_size = n * random.randint(30, 200)
    state = list(state)
    while variation_size > 0:
        moves = []
        row, col = divmod(null_pos, n)

        if row > 0: moves.append(-n) #up
        if row < n - 1: moves.append(n) #down
        if col > 0: moves.append(-1) #left
        if col < n - 1: moves.append(1) #right
        ran_action = random.randint(0, len(moves) - 1)
        x = null_pos
        new_x = x + moves[ran_action]

        state[x], state[new_x] = state[new_x], state[x]
        null_pos = new_x
        variation_size -= 1
    return tuple(state), null_pos