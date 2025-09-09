def format(file_path):
    with open(file_path,"r") as file:
        content = file.read()
        arr = content[1:].split(">")
        sequences = {}
        for id_seq in arr:
            two_parts = id_seq.split("\n",1)
            id = two_parts[0]
            seq = two_parts[1]
            clean_seq = ""
            for c in seq:
                if c!="\n":
                    clean_seq+=c
            sequences[id]=clean_seq
        return sequences
    
def gc_count(seq):
    counts = {"C":0,"G":0}
    for c in seq:
        if c in counts:
            counts[c]+=1
    return (counts["C"]+counts["G"])/len(seq)*100

def id_and_gc_count(sequences):
    id_and_count = {}
    for key,val in sequences.items():
        id_and_count[key]=gc_count(val)
    return id_and_count

def max_gc_count(id_and_count):
    max = 0
    max_id = None
    for key,val in id_and_count.items():
        if val > max:
            max = val
            max_id = key
    return [max_id,max]


file_path = "C:\\Users\\elale\\Desktop\\writen\\text.txt"
sequences = format(file_path)
id_and_count = id_and_gc_count(sequences)
highest_gc = max_gc_count(id_and_count)

with open("C:\\Users\\elale\\Desktop\\writen\\result.txt","a") as result:
    result.write(highest_gc[0]+"\n"+str(round(highest_gc[1],6)))

    
