file_path = "C:\\Users\\elale\\Desktop\\writen\\text.txt"
with open(file_path,"r") as file:
    contents = file.read()
    arr = contents.split()
    strand1 = arr[0]
    strand2 = arr[1]
    mismatch_count = 0
    for i in range(len(strand1)):
        if strand1[i]!=strand2[i]:
            mismatch_count+=1
    print(mismatch_count)