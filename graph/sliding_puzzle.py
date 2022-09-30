from collections import deque
from typing import List
from pprint import pprint as pp

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
def num_steps(init_pos, target):
    # possible change is still [1,0,-1,0] for row and [0,1,0,-1] for col
    # but we use condition to limit its move
    init_pos = tuple(tuple(line) for line in init_pos)
    if init_pos == target:
        return 0
    moves_map = {init_pos: 0}
    moves_queue = deque([init_pos])
    while moves_queue:
        top = moves_queue.popleft()
        row, col = 0, 0
        # need to find the position of element "0"
        # can we remember this?
        for i, line in enumerate(top):
            for j, entry in enumerate(line):
                if entry == 0:
                    row, col = i, j
        print(f"zero location {row}, {col}")
        for delta_row, delta_col in directions:
            new_row, new_col = row + delta_row, col + delta_col
            if new_row >= 0 and new_row < 2 and new_col >= 0 and new_col < 3:
                new_state = list(list(line) for line in top)
                new_state[new_row][new_col], new_state[row][col] = new_state[row][col], new_state[new_row][new_col]
                new_tuples = tuple(tuple(line) for line in new_state)
                if new_tuples not in moves_map:
                    moves_map[new_tuples] = moves_map[top] + 1
                    moves_queue.append(new_tuples)
                    if new_tuples == target:
                        return moves_map[new_tuples]
    return -1

def num_steps_new(init_pos, target):
    delta_row = [0, 1, 0, -1]
    delta_col = [1, 0, -1, 0]
    init_pos = tuple(tuple(line) for line in init_pos)
    if init_pos == target:
        return 0

    moves_steps = 0
    moves = {init_pos:0}
    moves_queue = deque([init_pos])
    while moves_queue:
        q_len = len(moves_queue)
        for _ in range(q_len):   # DO NOT use for _ in moves_queue, since moves_queue is mutated
            top = moves_queue.popleft()
            row, col = 0, 0
            for i, line in enumerate(top):
                for j, entry in enumerate(line):
                    if entry == 0:
                        row, col = i, j
            print(f"zero location {row}, {col}")
            for i in range(len(delta_row)):
                new_row = row + delta_row[i]
                new_col = col + delta_col[i]
                if 0<= new_row < 2 and 0<= new_col < 3:
                    new_state = list(list(line) for line in top)
                    new_state[new_row][new_col], new_state[row][col] = new_state[row][col], new_state[new_row][new_col]
                    new_tuples = tuple(tuple(line) for line in new_state)
                    if new_tuples not in moves:
                        moves[new_tuples] = moves[top] + 1
                        moves_queue.append(new_tuples)
                        if new_tuples == target:
                            return moves[new_tuples]
    return -1
        

target = ((1, 2, 3), (4, 5, 0))
init_pos = ((4,1,3), (2,0,5))
ret = num_steps_new(init_pos, target)
print(ret)