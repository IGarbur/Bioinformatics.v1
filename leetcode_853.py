#This question requires positions to be sorted, also notice that
#positions are unique

#based on these ideas above to sort positions and not love its corresponding 
#speeds i will use a dict position:speed
target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]

corresponding = {}
for i in range(len(position)):
    corresponding[position[i]]=speed[i]
#print(corresponding)

stack = []
#sort position array
start = sorted(position)
#print(start)
for i in range(len(start)-1,-1,-1):
    time = (target-start[i])/corresponding[start[i]]
    #print(time)
    if stack!=[] and time <= stack[-1]:
        #stack.pop()
        continue
    else:
        stack.append(time)
    #print(stack)
print(len(stack))
