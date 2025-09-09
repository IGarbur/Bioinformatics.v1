file_path = "C:\\Users\\elale\\Desktop\\writen\\text.txt"
with open(file_path,"r") as file:
    contents = file.read()
    arr = contents.split()
    s = arr[0]
    t = arr[1]

motifs = []
for i in range(len(s)-len(t)+1):
    match_count = 0
    j = i
    k = 0
    while k < len(t) and s[j]==t[k]:
        #print(f"{s[j]}=={t[k]}, match_count={match_count}")
        match_count+=1
        if match_count==len(t):
            motifs.append(i+1)
        j+=1
        k+=1

with open("C:\\Users\\elale\\Desktop\\writen\\result.txt","a") as result:
    for motif in motifs:
        result.write(str(motif)+" ")


