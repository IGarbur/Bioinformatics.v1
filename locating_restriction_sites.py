file_path = "C:\\Users\\elale\\Desktop\\writen\\text.txt"
with open(file_path,"r") as file:
    contents = file.read()
def format(contents):
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

def reverse_complement(seq):
    complement = ""
    for nuc in seq:
        if nuc == "T":
            complement+="A"
        elif nuc == "A":
            complement+="T"
        elif nuc == "C":
            complement+="G"
        elif nuc == "G":
            complement+="C"

    rev_complement = ""
    for i in range(len(complement)-1,-1,-1):
        rev_complement+=complement[i]
    return rev_complement

def get_restriction_sites(seq,rev_comp):
    #{start:length}
    restriction_sites = {}
    for i in range(len(seq)):
        new_palindrome = True
        length = 0
        k = i
        original = i
        j = 0
        match = ""
        while k < len(seq) and j < len(rev_comp):
            print(f"{match}     strats at: {i+1}      length: {length}")
            if seq[k]==rev_comp[j]:
                length+=1
                new_palindrome = False
                #if length > 3 and length < 13:
                    #restriction_sites[original+1]=length
                match+=rev_comp[j]
                k+=1
                j+=1
            elif seq[k]!=rev_comp[j] and new_palindrome:
                j+=1
            elif seq[k]!=rev_comp[j] and not new_palindrome:
                if length > 3 and length < 13:
                    restriction_sites[original+1]=length
                match = ""
                k = i
                j-=length - 1
                new_palindrome = True
                original = k
                length = 0
    print(restriction_sites)


seq = format(contents)["Rosalind_24"]
print(seq)
rev_comp = reverse_complement(seq)
print(rev_comp)
get_restriction_sites(seq,rev_comp)
