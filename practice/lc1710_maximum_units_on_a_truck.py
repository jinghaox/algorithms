def maximum_units_on_a_truck(boxTypes, truckSize):
    box_left = truckSize
    total = 0
    for box, units in sorted(boxTypes, key = lambda x: x[1], reverse =True):
        box = min(box, box_left)
        total += box*units
        box_left -= box
        if box_left < 0:
            break
    return total

boxTypes = [[5,10],[2,5],[4,7],[3,9]]
truckSize = 10
ret = maximum_units_on_a_truck(boxTypes, truckSize)
print(ret)