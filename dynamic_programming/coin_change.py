# given coins of different values and an amount, find the minimum number of coins to make up the amount
# [1,2,5] --> 11
# solution: 3  (1,5,5)
from typing import List
from math import inf

def coin_change(coins, amount):
    """ Dynamic programming

    dp[target] = min(1 + dp[target-c1],
                     1 + dp[target-c2],
                     1 + dp[target-c3])
    how to do it?
    dp[target] = min(1 + dp[target-c1], dp[target])
    assume 1+dp[target-c1] is a, dp[taget] is b
    then min(a,b), if a<b, is a, ow, is b
    then if a<b, min(1+dp[target-c2], a)
    or if a>b, min(1+dp[target-c2], b)

    init dp[t] to inf, where t is from 0 to amount
    for each t
        loop thru all coins
            dpt[t] = min(1 + dp[t-c], dp[t])

    """
    dp = (amount+1)*[float('inf')]
    dp[0] = 0
    for t in range(1, amount+1):  # we used 2 before, but we can start from 1
        for c in coins:
            if t-c >= 0:
                # dp[t]'s init value is 'inf', and we are taking min here, so it's ok
                dp[t] = min(1 + dp[t - c], dp[t])
    print(dp)
    return dp[-1]

def coin_change_dfs(coins, amount):
    def dfs(sum):
        if sum == amount:
            return 0
        if sum > amount:
            return float('inf')
        res = float('inf')
        for c in coins:
            ret = dfs(sum+c)
            if ret != float('inf'):
                res = min(res, ret+1)

        return res
    
    return dfs(0)

def coin_change_dfs_mine(coins, amount):
    # my code passes res (list) as the argument
    # so no need to set res=float('inf') in each call
    def dfs(sum, res):
        if sum == amount:
            return 0
        if sum > amount:
            return -1  #float('inf')
        for c in coins:
            ret = dfs(sum+c, res)
            if ret != -1: #float('inf'):
                res[0] = ret+1   # here don't use min()

        return res[0]
    
    res = [-1] #[float('inf')]
    return dfs(0, res)

def coin_change_dfs_mine_memo(coins, amount):
    # my code passes res (list) as the argument
    # so no need to set res=float('inf') in each call
    # here memo saves the min value of each dfs return
    # which means the minimum coins it needs to reach the amount
    # e.g. sum==0, memo[sum]=3, means it needs minimum 3 coins (1,2,5) to get 11
    def dfs(sum, res, memo):
        if sum == amount:
            # this means it needs 0 coin to reach amount since sum==amount
            return 0
        if sum > amount:
            return -1  #float('inf')
        if memo[sum] != -1:
            return memo[sum]

        for c in coins:
            ret = dfs(sum+c, res, memo)
            if ret != -1: #float('inf'):
                # for current coin c, it needs one more coin + the return of dfs(sum+c)
                # that's why it's ret+1
                res[0] = ret + 1   
            print(f"c={c}, memo={memo}")

        memo[sum] = res[0]
        return res[0]
    
    res = [-1] 
    memo = [-1]*(amount+1)
    ret = dfs(0, res, memo)
    return ret

def min_coins(coins, amount, sum, memo):
  if sum == amount:
    return 0

  if sum > amount:
    return inf

  if (memo[sum] != -1):
    return memo[sum]

  ans = inf
  for coin in coins:
    result = min_coins(coins, amount, sum + coin, memo)
    if result == inf:
      continue
    ans = min(ans, result + 1)
  
  memo[sum] = ans
  print(memo)
  return ans

def coin_change_algo(coins: List[int], amount: int) -> int:
  memo = [-1] * (amount + 1)
  result = min_coins(coins, amount, 0, memo)
  return result if result != inf else -1

# the following is for get all coin combinations to reach the amount
def coin_comb(coins, amount):
    def dfs(start_index, path, res, remaining):
        if remaining == 0:
            res.append(path[:])
            return
        for i in range(start_index, len(coins)):
            coin = coins[i]
            if remaining < coin:
                continue
            path.append(coin)
            # to remove dup, here must call dfs(i), not dfs(start_index)
            dfs(i, path, res, remaining - coin)
            path.pop()
    res = []
    path = []
    dfs(0, path, res, amount)
    return res 




coins = [1,2,5]
amount = 11
# coins = [2]
# amount = 3
# ret = coin_change(coins, 11)
# ret = coin_change_dfs_mine_memo(coins, amount)
ret = coin_change_dfs_mine_memo(coins, amount)
print(ret)
ret = coin_comb(coins, amount)
print(len(ret))
all_lens = [len(r) for r in ret]
print(min(all_lens))
print(ret)
print([r for r in ret if len(r) == min(all_lens)])

