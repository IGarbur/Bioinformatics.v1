#LeetCode 1 Two sum


'''My brute force solution'''
'''
def two_sum(list,target):
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if list[i]+list[j]==target:
                return [i,j]
nums = [2,1,5,3]
target = 4
print(two_sum(nums,target))
'''

#Key IDEA, imagine your current element is equal to 1 and your target is 4
#if you have a hasmap of all elements which you can lookup which number would you look for?
#how long would it take you to look up that number?

'''My Second attempt
def two_sum(nums,target):
    dict = {} #I decided to use number as key and index as value
    for i in range(len(nums)):
        dict[nums[i]]=i
    #print(dict)
    for i in range(len(nums)):
        if (target-nums[i]) in dict: #so this will result in a problem because it will find 4-2=2 which will be itself, and we would need to check index of our current 2 with index of 2 in a dictionary
            return [i,dict[target-nums[i]]]

nums = [2,1,5,3]
target = 4
print(two_sum(nums,target))
'''

#Key IDEA_2 we would like to pass through a list once, and every time we check for that difference if it's not there we just add our element to a dictionary and move forward 

#Here is my final working solution
def two_sum(nums,target):
    dict = {}
    for i in range(len(nums)):
        if (target-nums[i]) in dict:
            return [dict[target-nums[i]],i] #had to switch an order
        else:
            dict[nums[i]]=i

nums = [2,7,11,15]
target = 9
print(two_sum(nums,target))
'''
NeetCode's fancy solution (same thing btw)
prevMap = {}
for i, n in enumerate(nums):
    diff = target - n
    if diff in prevMap:
        return [prevMap[diff],i]
    prevMap[n] = i
return


'''