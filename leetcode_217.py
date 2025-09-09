#Leetcode 217
#GIVEN AN INTEGER ARRAY nums , RETURN true IF ANY VALUE APPEARS AT LEAST TWICE IN AN ARRAY, AND RETURN false if every element is distinct
nums = [1,4,4,5,4]

def duplicate(list):
    dict = {}
    for i in range(len(list)):
        if list[i] not in dict:
            dict[list[i]]=1
        else:
            return True
    return False 

result = duplicate(nums)
print(result)

'''NeetCode solution:
He used a set data structure which I forgot existed (shame)

hashset = set()

for n in nums:
    if n in hashset:
        return True
    hashset.add(n)
return False

So otherwise code and the idea is the same'''