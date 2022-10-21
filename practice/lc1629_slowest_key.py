from typing import List
def slowestKey(releaseTimes: List[int], keysPressed: str) -> str:
    n = len(releaseTimes)
    duration = [releaseTimes[i] - releaseTimes[i-1] for i in range(1, n)]
    duration.insert(0, releaseTimes[0])
    max_dur = max(duration)
    candidate = [i for i in range(n) if duration[i] == max_dur]
    max_i = candidate[0] 
    for i in candidate:
        if keysPressed[i] > keysPressed[max_i]:
            max_i = i

    return keysPressed[max_i]

def slowest_key_one_loop(releaseTimes, keysPressed):
    slowest_key = ''  # initialize it to 'a'? what if 'a' is not in ?
    max_duration = 0
    n = len(releaseTimes)
    for i in range(n):
        pre_rt = releaseTimes[i-1] if i > 0 else 0 
        duration = releaseTimes[i] - pre_rt
        if duration > max_duration:
            max_duration = duration
            slowest_key = keysPressed[i]
        elif duration == max_duration:
            slowest_key = max(slowest_key, keysPressed[i])
    return slowest_key


# releaseTimes = [9, 29, 49, 50]
# keysPressed = 'cbcd'

releaseTimes = [12,23,36,46,62]
keysPressed = "spuda"
# ret = slowestKey(releaseTimes, keysPressed)
ret = slowest_key_one_loop(releaseTimes, keysPressed)
print(ret)