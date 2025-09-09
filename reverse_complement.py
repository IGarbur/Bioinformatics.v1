def colored(seq):
    bcolors = {
        "A":"\033[92m",
        "C":"\033[94m",
        "G":"\033[93m",
        "T":"\033[91m",
        "U":"\033[91m",
        "reset":"\033[0;0m",
    }
    tmpStr = ""
    for nuc in seq:
        if nuc in bcolors:
            tmpStr += bcolors[nuc]+nuc
        else:
            tmpStr += bcolors["reset"]+nuc
    return tmpStr + "\033[0;0m"
def complement(seq):
    match = {"A":"T","T":"A","C":"G","G":"C"}
    comp = ""
    for base in seq:
        comp+=match[base]
    return comp

def reverse_complement(seq):
    reverse = ""
    for i in range(len(seq)-1,-1,-1):
        reverse+=seq[i]
    reverce_comp = complement(reverse)
    return reverce_comp

def display(strand1,strand2):
    connector = "|"*len(strand1)
    new_seq = f"5'->{strand1}->3'\n    {connector}\n3'<-{strand2}<-5'"
    print(colored(new_seq))

strand1 = "AAAACCCGGT"
strand2 = reverse_complement(strand1)
display(strand1,strand2)