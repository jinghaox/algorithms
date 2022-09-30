class UnionFind:
    def __init__(self):
        # maps the node to its set ID
        # here set ID means the parent of each set
        self.id = {}
    
    def find(self, x):
        # get the value associated with key x, if not, set it to x itself
        y = self.id.get(x, x)

        # check if the current node is a Set ID node
        if y != x:
            # set the value to Set ID node of node y
            y = self.find(y)

        # if y == x, means x has no Set ID(parent)
        # then return y (x), means set a node's parent to itself
        return y
    
    def union(self, x, y):
        # union find
        # if x is single node, 
        # self.find(x) is x
        # so self.id[x] = self.find(y), set y's Set ID to x's Set ID
        # if y is single node, then x:y, other wise: x: y's Set ID

        # if x is not a single node, has Set ID already
        # self.find(x) is its Set ID, then we set its Set ID's Set_ID to be y's Set_ID
        self.id[self.find(x)] = self.find(y)

class AmortizedUnionFind:
    # initialize the data structure that maps the node to its set ID
    def __init__(self):
        self.id = {}

    # find the Set ID of Node x
    def find(self, x):
        y = self.id.get(x, x)
        # check if the current node is a Set ID node
        if y != x:
            # set the value to Set ID node of node y, and change the hash value of node x to Set ID value of node y
            self.id[x] = y = self.find(y)
            # the reason we assign it to y as well is because we want to return y
            # because when y==x, we also want to return y
            # otherwise, we need to add a 'return self.id[x]' here
        return y

    # union two different sets setting one Set's parent to the other parent
    def union(self, x, y):
        self.id[self.find(x)] = self.find(y)

class RankUnionFind:
    def __init__(self):
        self.id = {}
        self.rank = {}

    # find the Set ID of Node x
    def find(self, x):
      # Get the value associated with key x, if it's not in the map return x
      y = self.id.get(x, x)
      # check if the current node is a Set ID node
      if y != x:
          # change the hash value of node x to Set ID value of node y
          self.id[x] = y = self.find(y)
      return y


    # union two different sets setting one Set's parent to the other parent
    def union(self, x, y):
        # check if keys exist in our rank map; if not, add them
        if self.find(x) not in self.rank:
            self.rank[self.find(x)] = 0
        if self.find(y) not in self.rank:
            self.rank[self.find(y)] = 0
        if self.rank[self.find(x)] < self.rank[self.find(y)]:
            self.id[self.find(x)] = self.find(y)
        else:
            self.id[self.find(y)] = self.find(x)
            # if rank is the same then we update x rank and increment by 1
            # we make y's parent equal to x's parent, so x has increased depth
            if self.rank[self.find(x)] == self.rank[self.find(y)]:
                self.rank[self.find(x)] = self.rank[self.find(x)] + 1

class SetCounter:
    def __init__(self) -> None:
        self.dsu = UnionFind()
        self.sizes = {}

    def merge(self, x: int, y: int) -> None:
        # get the sum of the size of x and y, set it to new_size
        new_size = self.count(x) + self.count(y)
        # merge x&y
        self.dsu.union(x, y)
        # let x's Set_ID's size to be the new_size
        self.sizes[self.dsu.find(x)] = new_size

    def count(self, x: int) -> int:
        # return x's Set_ID's size
        return self.sizes.get(self.dsu.find(x), 1)

def umbristan(n, breaks):
    # initialize data structures
    dsu = UnionFind()
    # the reason we need to reverse here is
    # for repeated (1,2),(1,2), the results of with and w/o reverse, are different
    breaks.reverse()
    ret = []
    # loop through the reverse list and merge the edges if they are not of the same list
    for a, b in breaks:
        print(f"a, b = {a}, {b}")
        ret.append(n)
        print(ret)
        # merging 2 connected components means total number of connected components decreases by 1
        # for the example, when breaks is [2,3], dsu.find(2) == dsu.find(3), so nothing to do
        if dsu.find(a) != dsu.find(b):
            dsu.union(a, b)
            n -= 1
    # remember that our answers are in reverse since we started from the end
    ret.reverse()
    return ret

def merge_accounts(accounts):
    union_find = UnionFind()
    all_user_emails = set()
    for one_account in accounts:
        username = one_account[0]
        email_parent = None
        for email in one_account[1:]:
            user_email_pair = (username, email)
            all_user_emails.add(user_email_pair)
            if email_parent is None:
                email_parent = user_email_pair
            else:
                union_find.union(email_parent, user_email_pair)
    account_associations = {}
    for user_email_pair in all_user_emails:
        ancestor = union_find.find(user_email_pair)
        if ancestor not in account_associations:
            account_associations[ancestor] = []
        account_associations[ancestor].append(user_email_pair)
    return_res = []
    for user in account_associations:
        one_user = [user[0]]
        for email in sorted(account_associations[user]):
            one_user.append(email[1])
        return_res.append(one_user)
    return sorted(return_res, key = lambda a: (a[0], a[1]))

def number_of_connected_components(n, connections):
    # very similar to umbristan
    # 区别在于：umbristan中，当第一个breaks被连接在一起后，clusters 仍旧是还没连接在一起的数目
    # 因为我们是反向着做的，本来它是最后一个breaks，当它执行后，clusters数目自然要加1
    # 而在此题中，我们是在连接，不是在breaks，所以一旦第一个连接被执行后，clusters就减1了
    res = []
    connected_components = n
    dsu = UnionFind()
    for a, b in connections:
        if dsu.find(a) != dsu.find(b):
            dsu.union(a,b)
            connected_components -= 1
        res.append(connected_components)

    return res

# uf = UnionFind()
# uf.union(3,4)
# uf.union(4,5)
# uf.union(2,6)
# uf.union(3,2)
# print(uf.id)
# 
# auf = AmortizedUnionFind()
# auf.union(3,4)
# auf.union(4,5)
# auf.union(5,6)
# auf.find(3)
# print(auf.id)

# ruf = RankUnionFind()
# ruf.union(3,4)
# ruf.union(4,5)
# ruf.union(5,6)
# print(ruf.id)
# print(ruf.rank)

# sc = SetCounter()
# sc.merge(1,2)
# sc.merge(2,3)
# ret = sc.count(3)
# print(ret)
# ret = sc.count(4)
# print(ret)

# # n = 4
# # breaks = [[1, 2], [2, 3], [3, 4], [1, 4], [2, 4]]
# n = 6
# breaks = [[1, 2], [1, 2], [1, 2], [3, 4], [4, 5], [3,5]]
# ret = umbristan(n, breaks)
# print(ret)

# accounts = [
#   ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
#   ["John", "johnsmith@mail.com", "john_work@mail.com"],
#   ["Mary", "mary@mail.com"],
#   # if Mary shares the same email such as john_work@mail.com with "John", still thinks they are different accounts
#   ["John", "johnny@mail.com"]
# ]
# ret = merge_accounts(accounts)
# print(ret)

n = 5
connections = [[1, 2], [2, 3], [1, 3], [0, 4], [0, 4]]
ret = number_of_connected_components(n, connections)
print(ret)