#s = "abcabcbb"
#s = "bbbbb"
#s = "pwwkew"
'''
The following was my attempt at solving the question 
but it fails when you try s = "dvdf"

counts = []
myset = set()
for c in s:
    if c not in myset:
        myset.add(c)
        #print(myset)
    else:
        counts.append(len(myset))
        myset.clear()
        myset.add(c)
counts.append(len(myset))
#print(counts)
print(max(counts))'''

#remember the example where you had to calculate sum of 5 numbers
#but instead of calculating sum each time 
#you removed the number behind and added the number in front of window

#same concept applies here when you find a duplicate s[r] in set, you 
# remove the "last" character from the set s[l] and increment the left pointer l+=1
#update length - 1
# then you ask again is  s[r] in set? if s[r] in set you again remove s[l] from the set
# else you add s[r] to set and increment r+=1, length + 1
#you also need to ask if your current length is greater than max lengt, 
# in which caase you need to update max length

s = "dvdf"
l = 0
r = 0
max_length = 0
current_length = 0
myset = set()
while r < len(s):
    print(myset)
    while s[r] in myset:
        myset.remove(s[l])
        print(myset)
        l+=1
        current_length-=1
    myset.add(s[r])
    print(myset)
    r+=1
    current_length+=1
    print(f"current length: {current_length}")
    print(f"max length: {max_length}")
    if current_length > max_length:
        max_length = current_length
print(max_length)