'''ADVICE use the r istead of l when comparing to mid'''
'''There is a problem when you compare l and mid and try to increment 
    you would then need to check if it already sorted, 
    its kinda dumb but makes sense if array was rotated len(n) times'''
nums = [3,4,5,1,2]
l = 0
r = len(nums)-1
while l<r:
    mid = (l+r)//2
    if nums[mid] > nums[r]:
        l = mid + 1
    else:
        r = mid
print(nums[l])
'''key take away you can use binary search to find
 a minimum value or a maximum value in an array where there are two
  climbs '''