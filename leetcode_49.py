#Idea is to build a dictionary which consists of a 
# key which is made of character counts in a word and 
# use a list of words as a value

#the key must be immutable (ex: tuple or a string)

#if a word mathes a key with counts 
# we will append a word to a list which is a value in a dictionary
#else we create a new key with a list that already contains that word

def build_key(s):
    dict = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,
            "g":0,"h":0,"i":0,"j":0,"k":0,"l":0,
            "m":0,"n":0,"o":0,"p":0,"q":0,"r":0,
            "s":0,"t":0,"u":0,"v":0,"w":0,"x":0,
            "y":0,"z":0,}
    for c in s:
        dict[c]+=1
    return f"a{dict['a']}b{dict['b']}c{dict['c']}d{dict['d']}e{dict['e']}f{dict['f']}g{dict['g']}h{dict['h']}i{dict['i']}j{dict['j']}k{dict['k']}l{dict['l']}m{dict['m']}n{dict['n']}o{dict['o']}p{dict['p']}q{dict['q']}r{dict['r']}s{dict['s']}t{dict['t']}u{dict['u']}v{dict['v']}w{dict['w']}x{dict['x']}y{dict['y']}z{dict['z']}"

strs = ["eat","tea","tan","ate","nat","bat"]
#strs = ["a"]

def group_anagrams(strs):
    groups = {} #key made of characters : [list containing words with that key]
    for s in strs:
        key = build_key(s)
        if key in groups:
            groups[key].append(s)
        else:
            groups[key] = [s]
    result = []
    for value in groups.values():
        result.append(value)
    return result

print(group_anagrams(strs))