
def binary_search(nums,target):
    l = 0
    r = len(nums)-1
    while l<=r: #to avoid overflow in other languages L + half_of_list -> (r-l)//2
        mid = (l+r)//2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            l = mid + 1
        else:
            r = mid - 1
    return -1

nums = [-1,0,3,5,9,12]
target = 31
print(binary_search(nums,target))