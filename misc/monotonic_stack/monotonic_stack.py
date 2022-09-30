def monotonic_stack(insert_entries):
    stack = []
    for x in insert_entries:
        while stack and x > stack[-1]:
            stack.pop()
        stack.append(x)
    return stack

insert_entries = [3,1,6,2,5,4]
ret = monotonic_stack(insert_entries)
print(ret)
