
def index_diff(A,B):
    index_list = [] # keeps track of indices with diff values
    if len(A) == len(B): # checks if length of arrays are equal
        i = 0
        while i < len(A):
            j = i
            if A[i] != B[i]:
                sub_ind = []
                while j != len(A) and A[j] != B[j]:
                    sub_ind.append(j) # records indices with diff values
                    j += 1
                i = j
                index_list.append(sub_ind)
            else:
                i = j
                i += 1

    if index_list == []:
        return True
    for si in index_list:
        if si == []: # if index list is empty, means no differences
            return True
        elif len(si) == 1: # if only 1 difference, return False
            return False
        else:
            # index_list = [1,2,3]
            A = A[si[0]:si[-1] + 1]
            B = B[si[0]:si[-1] + 1]
            B = B[::-1]
            print("reverse B")
            print(B)

            index_diff(A, B) # pass through function again until no differences found (True) or only 1 difference found (False)

def index_diff_new(A,B):
    if len(A) != len(B):
        return False
    
    start_index = end_index = 0
    for i in range(len(A)):
        if A[i] != B[i]:
            start_index = i
            break
        
    for i in range(len(A)-1, -1, -1):
        if A[i] != B[i]:
            end_index = i
            break

    sub_array_b = B[start_index:end_index+1]
    sub_array_b = sub_array_b[::-1]
    sub_array_a = A[start_index:end_index+1]
    return sub_array_b == sub_array_a

A = [1,2,3,4,5,6,7,8,9]
B = [1,4,2,3,5,7,8,6,9]
ret = index_diff(A,B)#  ## #  #
print(ret)