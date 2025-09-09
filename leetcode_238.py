#nums = [1,2,3,4]
nums = [-1,1,0,-3,3]
pre = nums[:len(nums)-1]
post = nums[1:]
left = [1]
right = [1]
'''
index = 1
for i in range(len(pre)):
    left.append(left[index-1]*pre[index-1])
    index+=1
'''
for i in range(len(pre)):
    left.append(left[i]*pre[i])
#print(left)
for i in range(len(post)):
    right.append(right[i]*post[(len(post)-1)-i])
#print(right)

result = []
for i in range(len(left)): #or right same length
    result.append(left[i]*right[(len(right)-1)-i])
print(result)