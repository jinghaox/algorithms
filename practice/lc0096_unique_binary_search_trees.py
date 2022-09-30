def num_unique_bst(n):
    num_trees = [1]*(n+1)  
    # initialize it for number of nodes (from 0 to n)
    # num_trees[0]=1
    # num_trees[1]=1

    # then we can start iterate number of nodes from 2 to n
    for num_nodes in range(2, n+1):
        temp_num = 0
        for root_node_ix in range(1, num_nodes+1):   
            # here must be from 1 to num_nodes+1, i.e. 1, 2, ..., num_nodes
            num_left_nodes = root_node_ix - 1
            num_right_nodes = num_nodes - root_node_ix
            temp_num += num_trees[num_left_nodes]*num_trees[num_right_nodes]
        num_trees[num_nodes] = temp_num
        print(f"{num_nodes}, {num_trees}")
    return num_trees[n]

n = 4
ret = num_unique_bst(n)
print(ret)
