file_path = "C:\\Users\\elale\\Desktop\\writen\\text.txt"
with open(file_path,"r") as file:
    contents = file.read()
def get_format(contents):
    lines = contents[1:].split(">")
    form = {}
    for line in lines:
        two_parts = line.split("\n",1)
        key = two_parts[0]
        value = ""
        for c in two_parts[1]:
            if c!="\n":
                value+=c
        form[key]=value
    return form

def get_sequences(fasta):
    sequences = []
    for val in fasta.values():
        sequences.append(val)
    return sequences

def get_shortest(sequences):
    index_of_shortest = 0
    length_of_shortest = len(sequences[0])
    for i in range(len(sequences)):
        if len(sequences[i]) < length_of_shortest:
            index_of_shortest = i
            length_of_shortest = len(sequences[i])
    return sequences[index_of_shortest]

def common_motif(sequences,motif):
    for seq in sequences:
        if motif not in seq:
            return False
    return True
'''Binary Search and rolling hash
Key Idea - instead of generating every possible substring like in brute force
we generate all substrings of a given length, why is that better? well if you generate 
length using binary search then you can determine wether you need a longer string,
or a shorter string (reducing number of serches to log(n))'''

'''def sub_of_given_length(motif,length):
    substrings = set()
    for j in range(len(motif)-length+1):
        substrings.add(motif[j:j+length])
    return substrings
    
def match(sequences,length,substrings):
    common = substrings #does this save an order of a set?!, because you can't just call intersection directly on substrings
    for seq in sequences:
        subs_of_seq = sub_of_given_length(seq,length)
        common = common.intersection(subs_of_seq)
        #print(common)
        if len(common)==0:
            return [False,""] #no substring in both sets we can stop
    return [True,list(common)[0]]

    
        

def binary_serch_on_length(motif):
    sub = ""
    low = 1
    high = len(motif)
    while low <= high:
        middle = (low + high)//2
        substrings = sub_of_given_length(motif,middle)
        check = match(sequences,middle,substrings)
        #print(check)
        if check[0]:
            sub = check[1]
            low = middle + 1
        else:
            high = middle - 1
    return sub
        
motif = "ATACA"
how_long = binary_serch_on_length(motif)
print(how_long)'''

fasta = get_format(contents)
sequences = get_sequences(fasta)
motif = get_shortest(sequences)


'''#Brute Force 
def all_substrings(motif):
    substrings = [motif]
    for k in range(len(motif)-1,0,-1): #our current length
        length = k
        for j in range(len(motif)-length+1):# our range for each length is the length of our initial motif - current length, +1 idk why i did +1?
            substring=""
            for i in range(j,j+length): #like a sliding window of fixed length, we build our substring
                substring+=motif[i]
            substrings.append(substring)
    return substrings

def lc_substring(substrings,sequences):
    for substring in substrings:
        if common_motif(sequences,substring):
            return substring
'''
'''
substrings = all_substrings(motif)
lcs = lc_substring(substrings,sequences)
print(lcs)
'''
