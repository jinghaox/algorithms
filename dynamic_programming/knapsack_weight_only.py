# def generate_sums(weights, res, sums, i):
#     # res is a set, so repeating values will be removed
#     if i == len(weights):
#         res.add(sums)
#         return
# 
#     # choosing the current item, i.e. weights[n-1], also get the res, and number of remaining is n-1
#     generate_sums(weights, res, sums + weights[i], i+1)
# 
#     generate_sums(weights, res, sums, i+1)
# 
# def knapsack_weight_only(weights):
#     res = set()
#     # n = len(weights)
#     generate_sums(weights, res, 0, 0)
#     return list(res)


# def generate_sums(weights, res, sums, i, memo):
#     # here memo is 2d, depth/level of the node, and node's value (weights sum by considering items from 0 to i)
#     if memo[i][sums]:
#         # if memo is True, means we already have this value summed, so just return
#         return
# 
#     if i == len(weights):
#         res.add(sums)
#         return
# 
#     generate_sums(weights, res, sums + weights[i], i + 1, memo)
#     generate_sums(weights, res, sums, i + 1, memo)
# 
# def knapsack_weight_only(weights):
# 
#     res = set()
# 
#     n = len(weights)
#     # find total sum of weights
#     total_sum = 0
#     for weight in weights:
#         total_sum += weight
#     memo = [[False for x in range(total_sum + 1)] for y in range(n + 1)] 
#     # memo is 2d, row is n+1 (including 0), colum is total_sum+1 
# 
#     generate_sums(weights, res, 0, 0, memo)
#     return list(res)

# # top-down with memoization
# def generate_sums(weights, sums, sum, n, memo):
#   if memo[n][sum]:
#     return
#   if n == 0:
#     sums.add(sum)
#     return
#   generate_sums(weights, sums, sum, n - 1, memo)
#   generate_sums(weights, sums, sum + weights[n - 1], n - 1, memo)
# def knapsack_weight_only(weights):
#   sums = set()
#   n = len(weights)
#   total_sum = 0
#   for weight in weights:
#     total_sum += weight
#   memo = [[False for x in range(total_sum + 1)] for y in range(n + 1)] 
#   generate_sums(weights, sums, 0, n, memo)
#   ans = []
#   for sum in sums:
#     ans.append(sum)
#   return ans

# bottom-up dp
def knapsack_weight_only(weights):
    n = len(weights)
    total_sum = sum(weights)
    dp = [[False for x in range(total_sum + 1)] for y in range(n + 1)] 
    # also create 2d array dp (same as memo)

    dp[0][0] = True

    for i in range(1, n + 1):
        for w in range(0, total_sum + 1):
            if i == 4 and w == 7:
                w = 7
            # vertical blue arrow in the above slides
            # why using dp[i][w]???
            # dp[i][w] = dp[i][w] or dp[i - 1][w]

            # using dp[i-1][w] seems working too
            dp[i][w] = dp[i-1][w]

            # diagonal blue arrow in the above slides
            if w - weights[i - 1] >= 0: # make sure the current item's weight is smaller than the target weight w
                # the reason we need dp[i][w] on the right is, dp[i][w] may be set to True in two lines before
                dp[i][w] = dp[i][w] or dp[i - 1][w - weights[i - 1]]
    ans = []
    # check the last row for all possible answers
    for w in range(0, total_sum + 1):
        if dp[n][w]:
            ans.append(w)

    return ans

def knapsack_weight_only_combination(weights):
    res = []
    # for combination, no need to use used array, since we can use index to control it
    def dfs(index, path, res, n):
        if len(path) == n:
            sums = sum(path)
            if sums not in res:
                res.append(sums)
            return
        
        for i in range(index, len(weights)):
            path.append(weights[i])
            dfs(i+1, path, res, n)
            path.pop()
    
    for n in range(1, len(weights)+1):
        dfs(0, [], res, n)
    return res
    

weights = [1,3,3,5]
# ret = knapsack_weight_only(weights)
ret = knapsack_weight_only_combination(weights)
print(ret)
