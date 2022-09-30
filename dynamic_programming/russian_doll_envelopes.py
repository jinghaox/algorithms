from math import inf
def max_layers_mine(envelopes):
    def compare_env(env1, env2):
        if env1[0] < env2[0] and env1[1] < env2[1]:
            return True
        return False

    # remember the min of the previous
    dp = [1] * len(envelopes)
    min_env = [inf, inf]
    for i in range(len(envelopes)):
        for j in range(i):
            if compare_env(envelopes[i], min_env):
                dp[i] = max(dp[j]+1, dp[i])
                min_env = envelopes[i]
    print(dp)
    return dp[-1]

def max_layers(envelopes):
    # it first sorts the envelopes by width+length 
    # [[2,3],[5,4],[6,4],[6,7]]
    # if an envelope A can fit into B, then A's sum < B's sum, e.g. (5,4) can fit into (6,5), so 9<11
    # but if A's sum < B's sum, doesn't mean A can fit into B, e.g (5,4) can't be in (6,4)

    envelopes.sort(key=lambda line: line[0] + line[1])
    max_layers_until_envelope = []
    for i, envelope in enumerate(envelopes):
        max_previous_layers = 0
        for j in range(i):
            # because we have sorted them by sum of width+length
            # so now as long as we check both width and length are smaller, then we know this 
            # evelope can fit into current envelope
            if envelopes[j][0] < envelope[0] and envelopes[j][1] < envelope[1]:
                max_previous_layers = max(max_previous_layers, max_layers_until_envelope[j])
        max_layers_until_envelope.append(max_previous_layers + 1)
    return max(max_layers_until_envelope)

envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
ret = max_layers(envelopes)
print(ret)


