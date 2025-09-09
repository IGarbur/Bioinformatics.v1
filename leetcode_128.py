#The idea is very simple given a random number 
#How do you tell if its a beggining of a sequence?
#if the previus number (num-1) is present in set  then it's not a start of a sequence
#therefore we don't need to interate num+1 until we reach some number that doesn't match
nums = [100,4,200,1,3,2]
myset = set()

for i in range(len(nums)):
    myset.add(nums[i])
print(myset)

max_count = 0
for i in range(len(nums)):
    if (nums[i]-1) in myset:
        pass
    else:
        count = 1
        num = nums[i]
        while num+1 in myset:
            count+=1
            num+=1
        #print(f"count:{count}")
        if count > max_count:
            max_count = count
print(f"max_count: {max_count}")

'''AI generated clean version 
for num in nums:
    if (num - 1) not in myset:
        count = 1
        while num + 1 in myset:
            num += 1
            count += 1
        max_count = max(max_count, count)
'''
