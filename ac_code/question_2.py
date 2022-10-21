# Company has multiple delievery centers from which products are sent.
# In one such delivery center, parcels are placed in a sequence where the ith parcel has a weight of weight[i].
# A shipment is consituted of a contiguous segment of parcels. The shipment imbalance of a shipment is defined as the 
# difference between the maximum and minimum weights within a shipment.
# Given the arrangement of parcels, find the sum of shipment imbalance of all the shipments that can be formed from the given sequence of parcels.
# 
# Example:
# weights = [1,2,3]
# The shipment imbalance is calculated as
# 1, imbalance = 0
# 2, imbalance = 0
# 3, imbalance = 0
# 1,2, imbalance = 1 
# 2,3, imbalance = 1 
# 1,2,3, imbalance = 2 

def sum_of_shipment_imbalance(weights):
    n = len(weights)
    imb_sum = 0
    for i in range(1,n):
        for j in range(0,n-i):
            max_s = max(weights[j:j+i+1])
            min_s = min(weights[j:j+i+1])
            imb = max_s - min_s
            imb_sum += imb
    return  imb_sum

weights = [1,2,3,4,5,6,7]
ret = sum_of_shipment_imbalance(weights)
print(ret)