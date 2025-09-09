heights = [2,1,5,6,2,3]
#heights = [6, 2, 5, 4, 5, 1, 6]
#heights = [2, 2, 6, 5, 4, 3, 2]

'''My original approach
max_area = 0
areas = []
for i in range(len(heights)):
    current = heights[i]
    j = i - 1 
    while j>=0 and heights[j]>=heights[i]:
        current+=heights[i]
        j-=1
    k = i + 1
    while k<len(heights) and heights[k]>=heights[i]:
        current+=heights[i]
        k+=1
    areas.append(current)
print(areas)
print(max(areas))'''