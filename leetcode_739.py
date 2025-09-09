temperatures = [73,74,75,71,69,72,76,73]
#temperatures = [30,40,50,60]
#temperatures = [30,60,90]
'''Brute Force
days = []
for i in range(len(temperatures)):
    j = i + 1
    while j < len(temperatures) and temperatures[j] < temperatures[i]:
        j+=1
    if j >= len(temperatures):
        days.append(0)
    else:
        days.append(j-i)

print(days)'''
#I did a horrible job implementing solution to this question 
days = []
for t in temperatures:
    days.append(0)
#print(days)
stack = []
i = 0
while i < len(temperatures):
    if stack == [] or temperatures[i] < stack[-1][0]:
        stack.append((temperatures[i],i))
    else:
        while stack!=[] and temperatures[i] > stack[-1][0]:
            days[stack[-1][1]] = (i-stack[-1][1])
            stack.pop()
        stack.append((temperatures[i],i))
    i+=1
print(days)