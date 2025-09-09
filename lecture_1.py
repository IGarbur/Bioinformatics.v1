
def mf_k_mer(genome,length):
    k_mers = {}
    for i in range(len(genome)-length+1):
        if genome[i:i+length] in k_mers:
            k_mers[genome[i:i+length]]+=1
        else:
            k_mers[genome[i:i+length]]=1
    #print(k_mers)
    max_v = 0
    for v in k_mers.values():
        if v > max_v:
            max_v = v
    #print(max_v)
    
    frequent = []
    for k,v in k_mers.items():
        if v==max_v:
            frequent.append(k)
    return frequent

genome = ""

most_frequent = mf_k_mer(genome,3)
print(most_frequent)