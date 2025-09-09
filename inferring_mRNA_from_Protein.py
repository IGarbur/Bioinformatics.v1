def aa_counts(table):
    #{"AA":count}
    counts = {}
    for aa in table.values():
        if aa in counts:
            counts[aa]+=1
        else:
            counts[aa]=1
    return counts

def protein_to_mrna_count(aa_seq,nums):
    num_of_rna_strings = 1
    for aa in aa_seq:
        num_of_rna_strings*=nums[aa]
    return (num_of_rna_strings*3)% 1000000

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
         "CAA":"Q","AAA":"K","GAA":"E",
         "CAG":"Q","AAG":"K","GAG":"E",
         "UGU":"C","CGU":"R","AGU":"S","GGU":"G",
         "UGC":"C","CGC":"R","AGC":"S","GGC":"G",
         "CGA":"R","AGA":"R","GGA":"G",
         "UGG":"W","CGG":"R","AGG":"R","GGG":"G",}

nums = aa_counts(table)
with open("C:\\Users\\elale\\Desktop\\writen\\text.txt","r") as file:
    aa_seq = file.read()
num_of_rna = protein_to_mrna_count(aa_seq,nums)
with open("C:\\Users\\elale\\Desktop\\writen\\result.txt","a") as result:
    result.write(str(num_of_rna))
