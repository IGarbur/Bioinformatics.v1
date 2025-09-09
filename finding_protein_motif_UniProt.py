import requests
def fetch_uniProt_fasta(accession_number):
    url = f"https://rest.uniprot.org/uniprotkb/{accession_number}.fasta"
    response = requests.get(url)
    if response.status_code==200:
        return response.text
    else:
        print(f"Unable to fetch the data for: {accession_number}")
        return None
def parse_fasta(fasta):
    #arr = fasta.split("\n",1)
    #seq = arr[1]
    #return seq
    lines = fasta.strip().split("\n")
    seq = "".join(lines[1:])
    return seq

    
def matches_glycosylation_motif(seq):
    matches = []
    for i in range(len(seq)-3):
        #print(f"{seq[i:i+4]}")
        if (seq[i]=="N") and (seq[i+1]!="P") and (seq[i+2]=="S" or seq[i+2]=="T") and (seq[i+3]!="P"):
            matches.append(i+1)
    return matches

with open("C:\\Users\\elale\\Desktop\\writen\\text.txt","r") as file:
    contents = file.read()

ids = contents.split()
accession_numbers = []
for id in ids:
    accession_numbers.append(id.split("_",1)[0])

id_and_match = {}
for i in range(len(accession_numbers)):
    fasta = fetch_uniProt_fasta(accession_numbers[i])
    seq = parse_fasta(fasta)
    matches = matches_glycosylation_motif(seq)
    str_matches = []
    for match in matches:
        str_matches.append(str(match))
    id_and_match[ids[i]]=str_matches

with open("C:\\Users\\elale\\Desktop\\writen\\result.txt","a") as result:
    for id,match in id_and_match.items():
        if match:
            m = " ".join(match)
            line = f"{id}\n{m}\n"
            result.write(line)