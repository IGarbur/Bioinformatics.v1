prices = [7,1,5,3,6,4]
#prices = [7,6,4,3,1]
#lets do a brute force
#you are searching for the biggest net difference between two points i & j 
'''net = 0
for i in range(len(prices)):
    for j in range(i+1,len(prices)):
        if prices[j]-prices[i]>net:
            net = prices[j]-prices[i]
print(net)'''

#O(n)solution requires you keeping track of two variables
# min price we have seen so far
# net_change vs current difference between our current value and min_so_far

net = 0
min_so_far = prices[0]

for i in range(len(prices)):
    if prices[i]-min_so_far > net:
        net = prices[i]-min_so_far
    if prices[i] < min_so_far:
        min_so_far = prices[i]
print(net)