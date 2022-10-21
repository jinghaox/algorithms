def is_robot_bounded(movements: str) -> bool:
    x, y, dx, dy = 0, 0, 0, 1
    for move in movements:
        if move == 'G':
            x, y = x + dx, y + dy
        elif move == 'L':
            # Left means previous is 0, 1, then turn left is -1, 0
            #         (0,1)
            # 
            #  (-1,0)        (0,1)
            # 
            #        (0,-1)
            dx, dy = -dy, dx
        else: # this is move == 'R'
            dx, dy = dy, -dx
    print(x,y,dx,dy)
    return (x, y) == (0, 0) or (dx, dy) != (0, 1)

movements = 'GLRRLL'
ret = is_robot_bounded(movements) 
print(ret)