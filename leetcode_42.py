height = [4,2,0,3,2,5]
#build a list of maximums to the left of currrent number
left = []
max_left = 0
for i in range(len(height)):
    left.append(max_left)
    if height[i]>max_left:
        max_left = height[i]
#print(left)
#build a list of maximums to the right of currrent number
right = []
max_right = 0
for i in range(len(height)-1,-1,-1):
    right.append(max_right)
    if height[i]>max_right:
        max_right = height[i]
#print(right)

#print(height)
#min(left[i],right[len(right)-1-i])-height[i] <-----if result > 0 add to the list
water = []
for i in range(len(height)):
    result = min(left[i],right[len(right)-1-i])-height[i]
    if result > 0:
        water.append(result)
#print(water)

sum = 0
for i in range(len(water)):
    sum+=water[i]
print(sum)