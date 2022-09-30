from typing import List

def festival_game(target: List[int]) -> int:
    dp = [[0]* len(target) for _ in range(len(target))]
    def f(left, right):
        if dp[left][right] != 0:
            return dp[left][right]
        for i in range(left, right + 1):

            if i == left:
                left_interval = 0
            else:
                left_interval = f(left, i - 1)

            if i == right:
                right_interval = 0
            else: 
                right_interval = f(i + 1, right)

            if left == 0:
                left_t = 1
            else:
                left_t = target[left-1]

            if right == len(target)-1:
                right_t = 1
            else:
                right_t = target[right+1]

            val = left_t * target[i] * right_t

            dp[left][right] = max(dp[left][right], left_interval + right_interval + val)

        return dp[left][right]
    return f(0, len(target) - 1)

target = [1,5,4]
ret = festival_game(target)
print(ret)