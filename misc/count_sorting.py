
# Python program for counting sort
 
# The main function that sort the given string arr[] in
# alphabetical order
def countSort(arr):
 
    # The output character array that will have sorted arr
    output = [0 for i in range(len(arr))]
 
    # Create a count array to store count of individual
    # characters and initialize count array as 0
    count = [0 for i in range(10)]
 
    # For storing the resulting answer since the
    # string is immutable
    ans = [0 for _ in arr]
 
    # Store count of each character
    for i in arr:
        count[i] += 1
 
    # Change count[i] so that count[i] now contains actual
    # position of this character in output array
    for i in range(10):
        count[i] += count[i-1]
    # 这时，count[i]表示arr中，小于等于i的元素的个数
    # count = [0,2,4,4,5,6,6,7,7,7]
    # <=0 的，有0个，<=1的, 有2个，<=2的，有4个，<=3的，还是4个...
 
    # Build the output character array
    for i in range(len(arr)):
        output[count[arr[i]]-1] = arr[i]
        count[arr[i]] -= 1
    # i=0, arr[0] = 1, count[arr[0]] = count[1] = 2, output[2-1] = output[1] = arr[0] = 1
    # 这个表示对第一个元素arr[0]，小于并等于它的，有2个 (即count[1]=2)，那么我们把第一个放到output[2-1](因为index从0开始)
    # 然后将其count - 1，因为我们已经用掉了一个元素了
    # i=1, arr[1] = 4, count[arr[1]] = count[4] = 5, output[5-1] = output[4] = 4 
    # 第二个元素是4，其count是5，所以将其放到第四个位置上，然后count-1=4
    # i=2, arr[2] = 1, count[arr[2]] = count[1] = 1, output[1-1] = output[0] = 1 

    # 当array遍历完之后，count = [0,0,2,4,4,5,6,6,7,7] 相当于以前的count arrary右移了一位
    # why?

    # output = [1,1,2,2,4,5,7]
 
    # Copy the output array to arr, so that arr now
    # contains sorted characters
    for i in range(len(arr)):
        ans[i] = output[i]
    return ans
def count_sort(arr):
    max_element = max(arr)
    min_element = min(arr)
    range_of_elements = max_element - min_element + 1
    # Create a count array to store count of individual
    # elements and initialize count array as 0
    count_arr = [0 for _ in range(range_of_elements)]
    output_arr = [0 for _ in range(len(arr))]
 
    # Store count of each character
    for i in range(0, len(arr)):
        count_arr[arr[i]-min_element] += 1
 
    # Change count_arr[i] so that count_arr[i] now contains actual
    # position of this element in output array
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]
 
    # Build the output character array
    # for i in range(len(arr)-1, -1, -1):
    for i in range(len(arr)):
        output_arr[count_arr[arr[i] - min_element] - 1] = arr[i]
        count_arr[arr[i] - min_element] -= 1
 
    # Copy the output array to arr, so that arr now
    # contains sorted characters
    for i in range(0, len(arr)):
        arr[i] = output_arr[i]
 
    return arr

# arr = [1,4,1,2,7,5,2]
arr = [-5, -10, 0, -3, 8, 5, -1, 10]
# ret = countSort(arr)
ret = count_sort(arr)
print(ret)