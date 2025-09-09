import math
def generate_counters(n):
    current = []
    for i in range(n-1):
        current.append(0)
    increment = [1]
    for i in range(n-2):
        increment.append(0)
    mods = []
    for i in range(n,1,-1):
        mods.append(i)

    counters = []

    for j in range(math.factorial(n)):
        carry = 0
        for i in range(len(current)):
            sum = current[i]+increment[i]+carry
            carry = sum//mods[i]
            current[i] = sum % mods[i]
            counter = ""
            for num in current:
                counter+=str(num)
        counters.append(counter)
        #print(counter)
    #print(counters)
    return counters

original_order = [1,2,3]
counters = generate_counters(len(original_order))
permutations = []
#Note: reduce number of swaps by storing new_orders in hash map, then look up these orders when calculating in a new digit
for counter in counters:
    new_order = original_order[:]
    for i in range(len(counter)):
        temp = new_order[i]
        j = int(counter[i])
        new_order[i] = new_order[i+j]
        new_order[i+j] = temp
    permutations.append(new_order)

permutations_strs = []
for i in range(len(permutations)):
    permutation = ""
    for element in permutations[i]:
        permutation+=str(element)+" "
    permutations_strs.append(permutation)
#print(permutations_strs)

with open("C:\\Users\\elale\\Desktop\\writen\\result.txt","w") as result:
    result.write(str(math.factorial(len(original_order)))+"\n")
    for permutation in permutations_strs:
        result.write(permutation + "\n")
    
