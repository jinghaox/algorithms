# Company is hosting a team hackathon.
# 1. Each team will have exactly teamSize developers
# 2. A developer's skill level is denoted by skill[i]
# 3. The diff between the max and min skill levels within a team can't exceed maxDiff
# Determine the max num of teams that can be formed from the contestants.
# It doesn't say it get all developers' skills used
# For example, if skill = [1,3,3,4,6,7], then output will be 1, i.e.[1,3,3], since [4,6,7] doesn't work

# Example:
# skill = [3,4,3,1,6,5]
# teamSize = 3
# maxDiff = 2

def num_of_teams(skill, team_size, max_diff):
    # two pointers

    # first sort
    skill.sort()

    # then use two pointers to go thru the skill set
    i = 0
    j = i+1
    temp_size = 1
    num_teams = 0
    while j < len(skill):
        if skill[j] - skill[i] <= max_diff:
            temp_size += 1
            if temp_size == team_size:
                print(skill[i:j+1])
                i = j+1
                j = i   # here set j to i, since after this, we will do j+=1
                num_teams += 1
                temp_size = 1
        else:
            temp_size = 1
            i = j
        j += 1
    
    return  num_teams

skill = [3,4,3,1,6,7,5,8,8]
team_size = 3
max_diff = 2
ret = num_of_teams(skill, team_size, max_diff)
print(ret)