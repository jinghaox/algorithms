def decode_ways_mine(digits):
    # 'A' is 1, not 0
    # since we need to find all ways, not just one way, so we shouldn't return True/False now
    # can't set memo's value to True/False, but numbers
    memo = {}
    words = [chr(ord('a') + i) for i in range(26)]

    def dfs(index, res):
        if index == len(digits):
            return 1

        if index in memo:
            return memo[index]
        
        ways = 0
        for c in words:
            # this one can only find one solution, not more solutions
            # because digits[index:] is '235'
            # '235' can start with '23', or '2', corresponds to 'w', or 'c'
            # but we can't tell it's 'cdf' or 'xf' if we have to convert it form digits to chars, 
            # so we can't check if it starts with 'c' or 'x'
            # that's why we use digits, not chars

            # unless we check all possibles of digits[index:]
            # in this test, we only need to check up to index+2

            # chr_to_check = chr(ord('a') + int(digits[index:index+len(c)]))

            if index == 4:
                index = 4
            possible = []
            if index+1 <= len(digits):
                chr_to_check = chr(ord('a') + int(digits[index:index+1]))
                possible = [chr_to_check]

            if index+2 <= len(digits):
                chr_to_check = chr(ord('a') + int(digits[index:index+2]))
                possible.append(chr_to_check)
            
            # if chr_to_check == c:
            if c in possible:
                if index + ord(c) - ord('a') <= len(digits):
                    ret = dfs(index + ord(c)-ord('a'), res)
                    ways += ret
                    if ret == 1:
                        res.append(c)
                    # simplified, just append c is fine, since chr_to_check == c when this happens
                    # res.append(c)
                    # memo[index] = ways
        memo[index] = ways
        return ways 
    res = []
    ret = dfs(0, res)
    print(res)
    print(memo)
    return ret

def decode_ways(digits):
    prefixes = [str(i) for i in range(1, 27)]
    def dfs(start_index, memo, res):
        if start_index in memo:
            return memo[start_index]
        if start_index == len(digits):
            memo[start_index] = 1
            return 1
        ways = 0
        remaining = digits[start_index:]
        for prefix in prefixes:
            # remaining '235', can start with '23'
            if remaining.startswith(prefix):
                ret = dfs(start_index + len(prefix), memo, res)
                ways += ret
                if ret>=1:
                    res.append(chr(ord('a') + int(prefix)))
        memo[start_index] = ways
        return ways
    memo = {}
    res = []
    ret = dfs(0, memo, res)
    print(f"memo = {memo}")
    print(res)
    return ret

def decode_ways_without_memo(digits):
    # without memo, we can get all results
    # but with memo, see the function below, it's not working
    prefixes = [str(i) for i in range(1, 27)]
    def dfs(start_index, path, res):
        # now return nothing
        if start_index == len(digits):
            res.append(path[:])
            return
        remaining = digits[start_index:]
        for prefix in prefixes:
            # print(prefix, end= " ")
            if remaining.startswith(prefix):
                path.append(chr(ord('a') + int(prefix)))
                dfs(start_index + len(prefix), path, res)
                path.pop()
    path = []
    res = []
    dfs(0, path, res)
    return res

def decode_ways_with_memo_and_res(digits):
    # now the problem is, when we have memo, the pop() doesn't work correctly
    # don't figure out the solution yet
    prefixes = [str(i) for i in range(1, 27)]
    def dfs(start_index, memo, res, path):

        if start_index == len(digits):
            res.append(path[:])
            memo[start_index] = 1
            return 1

        # if comment this out, then res is correct and ways is also correct
        # 这里的问题是，可以用memo来返回个数，但是无法返回具体的组合
        # 除非改变memo的结构和实现方法
        # memo = {5:[""], 4:["3"], 3:[["2", "3"], ["23"]], 2:[["2", "2", "3"], ["22", 3], ["2", "23"], ...]}
        if start_index in memo:
            # path.append(digits[start_index])
            res.append(path[:])
            return memo[start_index]

        ways = 0
        remaining = digits[start_index:]
        for prefix in prefixes:
            # remaining '235', can start with '23'
            if remaining.startswith(prefix):
                path.append(prefix)
                ways += dfs(start_index + len(prefix), memo, res, path)
                path.pop()
        memo[start_index] = ways
        return ways

    memo = {}
    res = []
    path = []
    ret = dfs(0, memo, res, path)
    print(f"res = {res}")
    print(memo)
    return ret

def decode_ways_with_new_memo(digits):
    prefixes = [str(i) for i in range(1, 27)]
    def dfs(start_index, memo, res, path):

        if start_index == len(digits):
            res.append(path[:])
            memo[start_index] = [[""]]
            return 1

        if len(memo[start_index]) != 0:
            # path.append(digits[start_index])
            res.append(path[:])
            return len(memo[start_index])


        ways = 0
        remaining = digits[start_index:]
        for prefix in prefixes:
            if remaining.startswith(prefix):
                path.append(prefix)
                ways += dfs(start_index + len(prefix), memo, res, path)
                path.pop()
        
        if start_index == 2:
            start_index = 2
        for i in range(start_index+1, start_index+2):
            # memo = {5:[[""]], 4:[["3"]], 3:[["2", "3"], ["23"]], 2:[["2", "2", "3"], ["22", 3], ["2", "23"], ...]}
            for y in memo[i]:
                for x in y:
                    if x == '':
                        new_s = [digits[start_index]]
                    else:
                        new_s = [[digits[start_index], x]]
                        if (digits[start_index]  + x) in prefixes:
                            new_s.append([digits[start_index]+x])
                    memo[start_index].append(new_s)

        return ways

    memo = {}
    for i in range(len(digits)+1):
        memo[i] = []

    res = []
    path = []
    ret = dfs(0, memo, res, path)
    print(f"res = {res}")
    print(memo)
    return ret

# ret = decode_ways_mine('235')
# print(ret)
# ret = decode_ways('235')
# print(ret)
# ret = decode_ways_without_memo('235')  # [2,3,5] [23, 5]
# print(ret)
# ret = decode_ways('11223')
# print(ret)
# ret = decode_ways_without_memo('11223')
# print(ret)
# ret = decode_ways_with_memo_and_res('11223')
# print(ret)
ret = decode_ways_with_new_memo('11223')
print(ret)