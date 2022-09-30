from http.client import PRECONDITION_REQUIRED


def course_schedule(numCourses, prerequisites):
    adj_list = {i:[] for i in range(numCourses)}
    for c, preq in prerequisites:
        adj_list[c].append(preq)

    # a course has 3 possible sttes
    # visited
    # visiting
    # unvisited
    output = []
    visit = set()
    cycle = set()

    def dfs(crs):  # crs is the current course visiting
        if crs in cycle:
            return False
        if crs in visit:
            return True

        cycle.add(crs)
        for pre in adj_list[crs]:
            if dfs(pre) == False:
                return False
        cycle.remove(crs)
        visit.add(crs)
        output.append(crs)
        return True

    def dfs_207(crs):  
        # this is using the algorithm in 207, no need of "visit", here cycle is "visit_set" in 207
        # but clear the prerequisite adjacent list if this course's pres have all been visited
        # note: if crs not in output ... this change is essential (do not use necessary, since it means can be done without) 
        if crs in cycle:
            return False
        if adj_list[crs] == []:
            if crs not in output:
                output.append(crs)
            return True

        cycle.add(crs)
        for pre in adj_list[crs]:
            if dfs(pre) == False:
                return False
        cycle.remove(crs)
        output.append(crs)
        adj_list[crs] = []   
        return True
    
    for c in range(numCourses):
        if dfs(c) == False:
            return []
    
    return output
            

prerequisites = [[0,1],[0,2],[1,3],[3,2],[4,0],[5,0]]
numCourses = 6
# prerequisites = [[0,1], [0,2], [1,3], [1,4], [3, 4]]
# numCourses = 5
ret = course_schedule(numCourses, prerequisites)
print(ret)
