#couple of key ideas
#Idea #1 instead of checking each time if two dictionaries are equal
#you can have two variable like     NEED vs HAVE 
#depending on thier relationship you perform actions

#NEED is constracted from t
#HAVE is constructed as we go:
#things that influence HAVE are charcters that appear in NEED
#that is as long as that character count is <= that character count in have dictionary

#another thing that influences HAVE is when we remove (-1) character 
# that is NEED dictionary

#things that don't influence count are characters that are not in
# NEED dictionary
# or characters that go above the count in NEED dictionary

#other things to keep in mind is l & r pointers which need to be updated
# we need to keep track of current_length which is (r-l) or (r-l)+1 (will have to double check)
# that length will need to be compared to minimum_length variable 
# 
# The function is supposed to return character from s starting from 
# index l and ending at index r aka (s[s:r+1])   

s = "ADOBECODEBANC"
t = "ABC"
#lets start with building two dictionaries
dict_t = {}
dict_s = {}

for i in range(len(t)):
    if t[i] in dict_t:
        dict_t[t[i]]+=1
    else:
        dict_t[t[i]]=1
#print(dict_t)
for i in range(len(t)):
    if t[i] in dict_t:
        dict_s[t[i]]=0
#print(dict_s)
#two variable to track dictionaries instead of comparing
have = 0
need = len(t)
#two pointers
l = 0
r = 0

#lets start with thinking how to add a single character @ r -> s[r]
#we need to check if that character in dict_t 
# and if value id dict_s @ s[r] < value in dict_t @s[r]
#if that is the case we increment value at dict_s[s[r]] and inc have