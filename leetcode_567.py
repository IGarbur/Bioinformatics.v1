s1 = "ab"
#s2 = "eidbaooo"
#s2 = "eidoooba"
s2="ba"
dict_1 = {}
state = False
for c in s1:
    if c in dict_1:
        dict_1[c]+=1
    else:
        dict_1[c]=1
#print(dict_1)
l = 0
r = len(s1)
dict_2 = {}
for i in range(l,r):
        if s2[i] in dict_2:
            dict_2[s2[i]]+=1
        else:
            dict_2[s2[i]]=1
#print(dict_2)

while r <= len(s2):
    print(dict_1)
    print(dict_2)
    print()
    if dict_1==dict_2:
        state = True
        break
    else:
        dict_2[s2[l]]-=1
        if dict_2[s2[l]]<=0:
            del dict_2[s2[l]]
        l+=1
        if s2[r] in dict_2:
            dict_2[s2[r]]+=1
        else:
            dict_2[s2[r]]=1
        r+=1

print(state)    