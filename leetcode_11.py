height = [1,8,6,2,5,4,8,3,7]
max = 0
l = 0
r = len(height)-1
while l < r:
    area = min(height[l],height[r])*(r-l)
    if area > max:
        max = area
    
    if height[l] > height[r]:
        r-=1
    else:
        l+=1
print(max)

#My idea, what if you were given a max in the height already?
#
#Then you can do "while (max*length)<= current_max" as a stoping condition
#when theoretical max 
#ex: (8*8)>((1,7)*8)  64>0
#ex: (8*7)>((8,7)*7)  56==56 theoretical max == current
#ex: (8*6)<((8,3)*6)    48 theoretical max < 49 current max  we can stop searching