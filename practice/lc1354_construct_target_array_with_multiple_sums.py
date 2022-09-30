from heapq import heappop, heappush
def construct_target_array_with_multiple_sums(target):
    sums = sum(target)
    # sums can be used to calculate the sum of the rest elements
    # first sums contains all elements
    # after we take the first max, then sums is the sum of the rest (also need remainder, see below)
    heap = []
    for t in target:
        heappush(heap, -t)
    
    while sums > len(target):       # sum([1,...,1]) is actually len(target)
        max_t = -1*heappop(heap)    # max_heap
        rest_sum = sums - max_t     # sums=9+5+3=17, 17-9 = 8, actually is 5+3 
        if max_t < rest_sum:        # 如果为真，表示不可能用1 + rest_sum来构成max_t，所以是False
            return False
        if rest_sum == 0:           # corner case
            return False
        rmdr = max_t % rest_sum     # 现在检查max_t - n*rest_sum后，剩下多少，即求模，因为不管n是1还是100，都可以重复得到
                                    # e.g [89, 5, 3], where 89 = 10*(5+3) + 1, 所以它等同于 [9, 5, 3]
        if rmdr == 0:               # 如果可以整除，那么就检查rest_sum是否恰好为1，这个只有一种情况，即rest_sum已经只剩1的时候
                                    # 这时候任何数%1都是0，所以肯定是可以的
                                    # 如果是其它数，比如%2==0，那肯定是不可以的
            return rest_sum == 1
        # sums = sums - (max_t - rmdr)  # 实际上这就是rest_sum + prev，即 [max_t, a, b,...]，在减去max_t后，变成[a,b,..., rmdr]
                                        # 其更新的sums = sum(a,b,...) + rmdr = rest_sum + rmdr
        sums = rest_sum + rmdr
        heappush(heap, -rmdr)       # 这时再将rmdr加到heap里
    return True


target = [89,3,5]
ret = construct_target_array_with_multiple_sums(target)
print(ret)