# sx=1,sy=1
# tx=3, ty=5
# (1+1, 1) -> (2,1) -> (2, 1+2) -> (2,3) -> (2+3, 3)
# (x, y) -> if x< y: (x+y, y) 谁大，就把大的加到小的数上
#           if x> y: (x, x+y)

# (1,9)  -> (100, 9)  use 100%9=1

def reaching_points(sx,sy,tx,ty):

    while tx>=sx and ty>=sy:
        if tx > ty:
            if tx%ty == sx:    
                # 对这个例子而言，这是算法work，(1,9) -> (100, 9)    100%9 ==1
                # 但是，对(3,3) -> (3,9)而言，9%3 == 0, 看似不work了，但实际上它是可以的
                # 这时，要用到下面的算法 (9-3)%3 = 0, ty=3 == sy=3
                return True
            elif (tx-sx) % ty == 0 and ty == sy:          
                # (3,2) -> (11,2),    (11-3)%2 == 8%2==0, ty=2 == sy=2
                # 这个表示11-3后，剩下的数可以用另一个数的倍数来得到
                # (100-9)%1 == 0, and ty=1 == sy=1
                return True
            else:
                # tx = tx - tx//ty * ty
                # 这个就是模
                tx %= ty
        else:
            if (ty-sy) % tx == 0 and tx == sx:
                return True
            # ty = ty - ty//tx * tx
            ty %= tx
    return False

sx, sy = 1,9
tx, ty = 102,9
ret = reaching_points(sx, sy, tx, ty)
print(ret)

        