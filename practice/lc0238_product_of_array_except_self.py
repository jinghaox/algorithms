def product_except_self(nums):
    n = len(nums)

    res = [1]*n
    pre_prod = [1]*n
    post_prod = [1]*n

    prefix = 1
    # for me, I will use this, but better way is next
    # for i in range(1, n):
    #     prefix *= nums[i-1]
    #     pre_prod[i] = prefix

    for i in range(n):
        pre_prod[i] = prefix
        prefix *= nums[i]
    
    postfix = 1
    for i in range(n-1, -1, -1):
        post_prod[i] = postfix
        postfix *= nums[i]
    
    for i in range(n):
        res[i] = pre_prod[i] * post_prod[i]
    # print(pre_prod)
    # print(post_prod)
    return res

def product_except_self_less_space(nums):
    n = len(nums)
    res = [1]*n
    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]
    
    postfix = 1
    for i in range(n-1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    return res

def product_except_self_same(nums):
    res = [1]

    for i in range(1, len(nums)):            
        res.append(res[i-1]*nums[i-1])

    right = 1
    for i in range(len(nums)-1, -1, -1):
        res[i] = res[i]*right
        right = right*nums[i]
    return res

# ret = product_except_self([1,2,3,4])
# ret = product_except_self_less_space([1,2,3,4])
ret = product_except_self_same([1,2,3,4])
print(ret)