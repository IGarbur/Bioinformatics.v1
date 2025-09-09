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

def profile(form):
    prof = {"A":[],"C":[],"G":[],"T":[]}

    matrix = []
    for value in form.values():
        matrix.append(value)

    for j in range(len(matrix[0])):
        column = []
        for i in range(len(matrix)):
            column.append(matrix[i][j])
        counts = {"A":0,"C":0,"G":0,"T":0}
        for c in column:
            counts[c]+=1
        for key,value in counts.items():
            prof[key].append(value)
    return prof

def consensus(prof):
    most_common = ""
    for i in range(len(prof["A"])):
        arr = []
        for value in prof.values():
            arr.append(value[i])
        maximum = max(arr)
        if maximum == arr[0]:
            most_common+="A"
        elif maximum == arr[1]:
            most_common+="C"
        elif maximum == arr[2]:
            most_common+="G"
        else:
            most_common+="T"
    return most_common
    

form = format(contents)
prof = profile(form)
most_common = consensus(prof)

with open("C:\\Users\\elale\\Desktop\\writen\\result.txt","a") as result:
    result.write(most_common)