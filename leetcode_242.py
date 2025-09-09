#LeetCode 242
#Given two strings s and t, return true if t is an anagram of s, and false otherwise
#anagram is a word that contains same letters

#key note: dictionary.get(keyname, value) will return a value associated with a key, or a value if the key is not found 

#s = "anagram"
#t = "nagaram"

'''a = "rat"
b = "car"'''

def is_anagram(s,t):
    dict_s = {}
    dict_t = {}
    for i in range(len(s)):
        if s[i] not in dict_s:
            dict_s[s[i]]=1
        else:
            dict_s[s[i]]+=1
    for i in range(len(t)):
        if t[i] not in dict_t:
            dict_t[t[i]]=1
        else:
            dict_t[t[i]]+=1
    
    for i in range(len(s)):
        if dict_s[s[i]]!=dict_t.get(s[i],0):
            return False
    return True
    
#print(is_anagram(s,t))

'''This code below

for i in range(len(s)):
        if s[i] not in dict_s:
            dict_s[s[i]]=1
        else:
            dict_s[s[i]]+=1
            
    can be written as

    for char in s:
        dict_s[char] = dict_s.get(char, 0) + 1
        
    it's the same thing 
    if you can pull up a key add 1 to value
    if the key doesn't exist you get 0 and add 1 
    which is the same thing as directly setting it to 1
'''

'''
My initial attempt had a flowed logic 

def is_anagram(s,t):
    dict = {}
    for i in range(len(s)):
        dict[s[i]]=1
    for j in range(len(t)):
        if t[j] in dict:
            dict.pop(t[j])
    if len(dict)==0:
        print("it's an Annagram")
        return True
    else:
        print("it's not an Annagram")
        return False

It was obviously not traking how many times each character appered
so if lets say character a appeared 3 times it would remain dict[a]=1 
and not be incremented 
so if you try to run code with 
s = "angrm"
t = "nagaram"
it would say that it's an Annagram which is obviously wrong
'''

'''
NeetCode Solution:

def anagram(s,t):
    if len(s)!=len(t):
        return False

    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = countS.get(s[i],0) + 1
        countT[t[i]] = countT.get(t[i],0) + 1
    for c in countS:
        if countS[c] != countT.get(c,0):
            return False
    return True

'''
