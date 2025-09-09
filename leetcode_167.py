#The difference from two sum I is that now you need to use constant space
numbers = [2,3,4]
target = 6
'''
Brute force O(n^2)
def two_sum(numbers,target):
    for i in range(len(numbers)):
        diff = target - numbers[i]
        for j in range(i+1,len(numbers)):
            if numbers[j]==diff:
                return [i+1,j+1]
            
print(two_sum(numbers,target))
'''

#Key Idea have two opposite pointers left and rigth 
#everytime you add them you need to find a difference from a target
#if smaller than target need to get a bigger number so increment the left
#if larger then teget need to get smaller number so decrement the right

def two_sum(numbers,target):
    left = 0
    right = len(numbers)-1
    while left < right:
        if numbers[left]+numbers[right] == target:
            return [left+1,right+1]
        elif numbers[left]+numbers[right] < target:
            left+=1
        else:
            right-=1

print(two_sum(numbers,target))
