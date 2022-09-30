from re import I


def coin_change(coins, amount):
    # dp[target] = min(1 + dp[target-c1],
    #                  1 + dp[target-c2],
    #                  1 + dp[target-c3])
    # how to do it?
    # dp[target] = min(1 + dp[target-c1], dp[target])
    # assume 1+dp[target-c1] is a, dp[taget] is b
    # then min(a,b), if a<b, is a, ow, is b
    # then if a<b, min(1+dp[target-c2], a)
    # or if a>b, min(1+dp[target-c2], b)
    dp = (amount+1)*[float('inf')]
    dp[0] = 0
    for t in range(2, amount+1):
        for c in coins:
            if t-c >= 0:
                # dp[t]'s init value is 'inf', and we are taking min here, so it's ok
                dp[t] = min(1 + dp[t - c], dp[t])
    print(dp)
    return dp[-1]

coins = [1,2,5]
amount = 11
ret = coin_change(coins, 11)
print(ret)
