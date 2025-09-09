#nums = [1,1,1,2,2,3]
#k = 2
'''
def frequent(nums,k):
    #k cannot be greater than number of elements in a list
    dict = {} # number:count, what if two different numbers have same count which to return?
    for i in range(len(nums)):
        if nums[i] in dict:
            dict[nums[i]]+=1
        else:
            dict[nums[i]]=1
    #print(dict)
    #idea remove the element with highest count from the dict
    #repeat this k times
    result = []
    
    for i in range(k):
        max = 0
        key_max = None
        for key, value in dict.items():
            if value > max:
                max = value
                key_max = key
        #print(key_max)
        #print(max)
        result.append(key_max)
        dict.pop(key_max)
        #print(result)
        #print(dict)
    return result

k_elements = frequent(nums,k)
print(k_elements)
'''
def count(nums):
    dict_count = {} 
    for i in range(len(nums)):
        if nums[i] in dict_count:
            dict_count[nums[i]]+=1
        else:
            dict_count[nums[i]]=1
    return dict_count

def create_2D_list(nums):
    list_2D = []
    for i in range(len(nums)+1):
        list_2D.append([])
    return list_2D

def count_to_num(counts,list2,k):
    for num, count in counts.items():
        list2[count] = num
    #print(list2)
    
    result = []
    for i in range(len(list2)-1,0,-1):
        if list2[i]!=[]:
            result.append(list2[i])
        if len(result)==k:
            return result


def main():
    nums = [1,1,1,2,2,100,100,100,100]
    k = 3
    counts = count(nums)
    #print(counts)
    list2 = create_2D_list(nums)
    #print(list2)
    result = count_to_num(counts,list2,k)
    print(result)
main()