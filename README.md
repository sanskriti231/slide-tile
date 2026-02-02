# Sliding Tile Puzzle

### Problem description:

- For an $n * n$ puzzle, the board consists of numbers 1 through $n^2$ - 1, and one empty tile represented by X.
- A move consists of moving the empty tile 'X' across the 4 directions.
- The objective is to reach the target state: number sorted accross the board


## Sliding tile puzzle solver - Version 1

- Version 1 is an implementation of 8-Puzzle problem using BFS - Breadth First Search algorithm.
- The goal of the puzzle is to rearrange tiles on a 3×3 board to reach the target configuration by sliding tiles into the empty space (X).
- BFS guarantees the minimum number of moves.

#### Approach used:

- Each board configuration is treated as a state.
- BFS explores all states level by level, ensuring the shortest solution path.
- States are stored as tuples (immutable and hashable) so they can be safely used in a set for tracking visited states.

#### Why we shuffled a solved board:

Instead of generating a completely random board, we shuffle an already solved puzzle to create the initial state.
- Not all 8-Puzzle configurations are solvable.
- Randomly generating states can easily lead to unsolvable puzzles.
- By applying valid moves to a solved board, we guarantee: the generated puzzle is always solvable.

This approach ensures version 1 is simple and reliable.

#### State representation
- The state is stored as tuple of length 9.
- This makes: state comparisons fast and storage in a set efficient.

#### Version 1 limitations

- BFS can be memory-intensive for deeper states.
