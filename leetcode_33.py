
#this is a combination of binary serach and finding min in rotated array
#lets start with a binary search
#what if you find a minimum element l = index_of_min, r = index_of_min-1
#and then just do binary search

def bsearch(nums,target):
    l = 0
    r = len(nums)-1
    while l<=r:
        mid = (l+r)//2
        if nums[mid]==target:
            return mid                  
        elif nums[l]<=target<nums[mid]:  
            r = mid - 1                 
        else:
            l = mid + 1
    return -1 

def main():
    nums = [4,5,6,7,0,1,2]
    target = 0
    found = bsearch(nums,target)
    print(found)
main()