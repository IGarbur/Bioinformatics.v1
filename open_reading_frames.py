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

def get_transcript(dna_seq):
    m_rna = ""
    for nuc in dna_seq:
        if nuc == "T":
            m_rna+="U"
        else:
            m_rna+=nuc
    return m_rna
def get_segments(m_rna):
    segments = []
    stop_codons = ["UAG","UAA","UGA"]
    for i in range(len(m_rna)-2):
        segment = ""
        start_codon = m_rna[i]+m_rna[i+1]+m_rna[i+2]
        if start_codon == "AUG":
            j = i
            #print(i)
            while (j < len(m_rna)-1):
                try:
                    stop_codon = m_rna[j]+m_rna[j+1]+m_rna[j+2]
                except:
                    break
                if stop_codon not in stop_codons:
                    segment+=stop_codon
                    j+=3
                else:
                    segment+=stop_codon
                    break
        if segment != "":
            segments.append(segment)

    verified = []
    for i in range(len(segments)):
        if segments[i][len(segments[i])-3:] in stop_codons: #This is an extremly important check: it checks if each mRNA ends with stop codon if it doesn't then its not a valid candidate for translation, logically there might be continuation of that segment cuz we never reached stop codon
            verified.append(segments[i])
    return verified

def translate(m_rna):
    current_codon = ""
    codon_length = 0
    protein = ""
    for i in range(len(m_rna)):
        current_codon+=m_rna[i]
        codon_length+=1
        if codon_length==3:
            if table[current_codon]!=None:
                protein+=table[current_codon]
                current_codon = ""
                codon_length = 0
            else:
                break
    return protein

def reverse_complement(dna_seq):
    complement = ""
    for nuc in dna_seq:
        if nuc == "A":
            complement+="T"
        elif nuc == "T":
            complement+="A"
        elif nuc == "C":
            complement+="G"
        elif nuc == "G":
            complement+="C"
    rev_comp = ""
    for i in range(len(complement)-1,-1,-1):
        rev_comp+=complement[i]
    return rev_comp

fasta = get_format(contents)
#print(fasta)
dna_seq = fasta["Rosalind_99"]
rev_comp = reverse_complement(dna_seq)
#print(f"Reverse complement: {rev_comp}")
#print(dna_seq)
m_rna = get_transcript(dna_seq)
m_rna2 = get_transcript(rev_comp)
#print(f"Original: {m_rna}")
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

m_rnas = get_segments(m_rna)
m_rnas2 = get_segments(m_rna2)
#print(m_rnas)
proteins = set()
for m_rna in m_rnas:
    proteins.add(translate(m_rna))
for m_rna2 in m_rnas2:
    proteins.add(translate(m_rna2))

with open("C:\\Users\\elale\\Desktop\\writen\\result.txt","w") as result:
    for protein in proteins:
        result.write(protein + "\n")