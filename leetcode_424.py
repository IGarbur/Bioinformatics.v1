'''s = "ABAB"
k = 2

l = 0
r = 0
counts = {}
longest = 0

while r < len(s):
    while ((r-l)+1) - (max(counts.values()) if counts else 0)> k:
        counts[s[l]]-=1
        l+=1
    if s[r] in counts:
        counts[s[r]]+=1
    else:
        counts[s[r]]=1
    r+=1
    if (r-l) > longest:
        longest = (r-l)
print(longest) '''

s = "ABAB"
k = 2

l = 0
r = 0
counts = {}
longest = 0
length_so_far = 0
while r < len(s):
    while ((r-l)+1) - (max(counts.values())if counts else 0) > k: #the reason for if counts else 0 is cuz initially dictionary is empty, you can also add a random lowercase character with value of zero and it will work
        counts[s[l]]-=1
        length_so_far-=1
        l+=1
    if s[r] in counts:
        counts[s[r]]+=1
    else:
        counts[s[r]]=1
    length_so_far+=1
    r+=1
    if length_so_far > longest:
        longest = length_so_far
print(longest) 