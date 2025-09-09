'''This implementation uses binary serch technique and sets (intersection)
    The idea that differs from brute force where we generate all possible substrings
    here we use binary serch to generate a length of which we want to generate substrings
    effectively reducing generation to log(n)
    
    O(m * n log n) is the time complexity of this algorithm
    it's not the best as suffix tree aproach is O (n log n) 
    but for now this will do'''

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

def sub_of_given_length(motif,length):
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
fasta = get_format(contents)
sequences = get_sequences(fasta)
motif = get_shortest(sequences)     
lcs = binary_serch_on_length(motif)
with open("C:\\Users\\elale\\Desktop\\writen\\result.txt","a") as result:
    result.write(lcs)