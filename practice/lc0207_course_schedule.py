def course_schedule(num_courses, prereq):
    # using dfs, O(n+p) need to visit every node and edge
    # pre_map
    # course   preq
    # 0       [1, 2]
    # 1       [3, 4]
    # 2       []
    # 3       [4]
    # 4       []

    # visit_set is used to detect cycle
    # if a node is already in the visitSet, then there's a loop

    pre_map = {i:[] for i in range(num_courses)}
    # for p in prereq:
    #     pre_map[p[0]].append(p[1])
    # this is better
    for c, p in prereq:
        pre_map[c].append(p)

    visit_set = set()

    def dfs(crs):  # we need current course as the arg, so for next recur call, we know which course to call
        if crs in visit_set:
            # this is the: if a node is already in the visitSet, then there's a loop
            return False
        if pre_map[crs] == []:
            return True  # means it can be completed

        visit_set.add(crs)
        for pre in pre_map[crs]:
            if not dfs(pre):  # return False immediately
                return False
        # only when all pre of this crs have been handled, and no one returns False, then we know this crs can be finished, it should return True
        # 在返回True之前，先做下面的
        # now we can remove this course from the visit_set, and set its pre_map to be []
        visit_set.remove(crs)
        pre_map[crs] = []
        # 注意这里也要return True，表明当前节点已经都访问过了
        return True

    for c in range(num_courses):  # 这里要用loop，是为了对付isolated graph，否则的话，call dfs(0)足够了
                                  # 在这个时候，所有pre_map应该已经全部为空了
        if not dfs(c):
            return False

    return True
            

num_courses = 5
prereq = [[0,1], [0,2], [1,3], [1,4], [3, 4]]
ret = course_schedule(num_courses, prereq)
print(ret)

