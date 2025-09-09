import math
#piles = [3,6,7,11]
#h = 8
piles = [30,11,23,4,20]
h = 5

l =  1
r = max(piles)
def calc_current_hours(piles,mid):
    sum = 0
    for num in piles:
        sum += math.ceil(num/mid)
    return sum

while l <= r:
    mid = (l+r)//2
    c = calc_current_hours(piles,mid)
    if c <= h:
        r = mid - 1
    else:
        l = mid + 1
print(l)