#dict of codons into AAs

table = {"UUU":"F","CUU":"L","AUU":"I","GUU":"V",
         "UUC":"F","CUC":"L","AUC":"I","GUC":"V",
         "UUA":"L","CUA":"L","AUA":"I","GUA":"V",
         "UUG":"L","CUG":"L","AUG":"M","GUG":"V",
         "UCU":"S","CCU":"P","ACU":"T","GCU":"A",
         "UCC":"S","CCC":"P","ACC":"T","GCC":"A",
         "UCA":"S","CCA":"P","ACA":"T","GCA":"A",
         "UCG":"S","CCG":"P","ACG":"T","GCG":"A",
         "UAU":"Y","CAU":"H","AAU":"N","GAU":"D",
         "UAC":"Y","CAC":"H","AAC":"N","GAC":"D",
         "UAA":None,"CAA":"Q","AAA":"K","GAA":"E",
         "UAG":None,"CAG":"Q","AAG":"K","GAG":"E",
         "UGU":"C","CGU":"R","AGU":"S","GGU":"G",
         "UGC":"C","CGC":"R","AGC":"S","GGC":"G",
         "UGA":None,"CGA":"R","AGA":"R","GGA":"G",
         "UGG":"W","CGG":"R","AGG":"R","GGG":"G",}

file_path = "C:\\Users\\elale\\Desktop\\writen\\text.txt"
with open(file_path,"r") as file:
    sample = file.read()
current_codon = ""
codon_length = 0
protein = ""
for i in range(len(sample)):
    current_codon+=sample[i]
    codon_length+=1
    if codon_length==3:
        if table[current_codon]!=None:
            protein+=table[current_codon]
            current_codon = ""
            codon_length = 0
        else:
            break

with open("C:\\Users\\elale\\Desktop\\writen\\result.txt","a") as result:
    result.write(protein)