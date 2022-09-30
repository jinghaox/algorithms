class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def build_list(arr):
    if arr:
        val = arr.pop(0)
    else:
        # when arr is empty, return None
        return None
    nxt = build_list(arr)
    return Node(val, nxt)

def print_list(head):
    while head:
        print(f"{head.val}", end="->")
        head = head.next
    print("")
    
def middle_of_linked_list(head):
    slow = head
    fast = head
    # for odd length, fast is good, fast.next is None
    # for even length, previous fast is the next of the tail, so fast is None, there's no fast.next
    while fast and fast.next:
        fast = fast.next
        fast = fast.next
        slow = slow.next

    return slow.val

arr = [1,2,3,4,5, 6]
lnk_lst = build_list(arr)
print_list(lnk_lst)

ret = middle_of_linked_list(lnk_lst)
print(ret)


