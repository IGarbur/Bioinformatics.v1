#Am i supposed to make a bunch of linked lists?
#make a dictionary of suffixes
#make a dictionary of prefixes

file_path = "C:\\Users\\elale\\Desktop\\writen\\text.txt"
with open(file_path,"r") as file:
    contents = file.read()
def parse_fasta(contents):
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

def get_prefixes(form):
    prefixes = {}
    for key,val in form.items():
        prefix = val[:3]
        if prefix in prefixes:
            prefixes[prefix].append(key)
        else:
            prefixes[prefix]=[key]
    return prefixes

def get_sufixes(form):
    sufixes = {}
    for key,val in form.items():
        sufix = val[len(val)-3:]
        if sufix in sufixes:
            sufixes[sufix].append(key)
        else:
            sufixes[sufix]=[key]
    return sufixes
def match(prefixes,sufixes):
    link = {}
    for sufix in sufixes.keys():
        if sufix in prefixes.keys():
            link[sufix]=[sufixes[sufix]]
            if sufix in link:
                link[sufix].append(prefixes[sufix])
            else:
                link[sufix]=prefixes[sufix]
    #print(link)
    return link

def display(link):
    result = []
    for arr_2d in link.values():
        for x in arr_2d[0]:
            for y in arr_2d[1]:
                if y!=x:
                    result.append([x,y])
    with open("C:\\Users\\elale\\Desktop\\writen\\result.txt","a") as file:
        for arr in result:
            file.write(arr[0]+" "+arr[1]+"\n")

    
    
form = parse_fasta(contents)
prefixes = get_prefixes(form)
sufixes = get_sufixes(form)
link = match(prefixes,sufixes)
display(link)



