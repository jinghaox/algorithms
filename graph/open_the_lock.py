from typing import List
from collections import deque

def num_steps(target_combo: str, trapped_combos: List[str]) -> int:
    # auto generate "0":"1" to "8":"9", then add "9":"0" manually
    next_digit = {**{str(i): str(i + 1) for i in range(9)}, "9": "0"}
    # prev_digit just reverts the key&val in next_digit
    # this is a smart way to reverse a dictionary
    prev_digit = {e: n for n, e in next_digit.items()}
    
    trapped_set = set(trapped_combos)
    # initialize step
    steps = {"0000":0}
    q = deque(["0000"])
    while q:
        curr_comb = q.popleft()
        for i in range(4):    # looping from start or end, it's different, depends on the target
            # e.g. "0000" is changed to  "" + "1" + "000"
            next_comb = curr_comb[:i] + next_digit[curr_comb[i]] + curr_comb[i+1:]
            if next_comb not in trapped_set and next_comb not in steps:
                # add next_comb to queue
                q.append(next_comb)
                # update the number of steps by 1 on top of current comb's step counts
                steps[next_comb] = steps[curr_comb] + 1
                if next_comb == target_combo:
                    print(len(steps))
                    return steps[next_comb]
            next_comb = curr_comb[:i] + prev_digit[curr_comb[i]] + curr_comb[i+1:]
            if next_comb not in trapped_set and next_comb not in steps:
                q.append(next_comb)
                steps[next_comb] = steps[curr_comb] + 1
                if next_comb == target_combo:
                    return steps[next_comb]
    return -1

def num_steps_new(target_combo: str, trapped_combos: List[str]) -> int: 
    def get_neighbours(combo): 
        for i in range(4): 
            yield combo[0:i] + str((int(combo[i]) + 1) % 10) + combo[i+1:] 
            yield combo[0:i] + str((int(combo[i]) - 1) % 10) + combo[i+1:]

    seed = "0000"

    visited = set(trapped_combos)
    visited.add(seed)
    q = deque([seed])
    steps = 0
    steps = {"0000":0}

    while len(q) > 0:
        # two ways to do this:
        # 1. using for _ in range(len(q)) to control the q's level, after each level iteration, steps+=1
        # 2. don't use level control, but control the level in the steps{"prev_level_key":value}, steps{"new_level": prev_level.value+1}
        # for _ in range(len(q)):
        combo = q.popleft()
        if combo == target_combo:
            return steps[combo]
        
        for n in get_neighbours(combo):
            if n in visited:
                continue
            steps[n] = steps[combo] + 1
                
            visited.add(n)
            q.append(n)
        
        # steps += 1
    return -1 

target_combo = "0002"
trapped_combos = ["0201","0101","0102","1212","2002"]

ret = num_steps_new(target_combo, trapped_combos)
print(ret)