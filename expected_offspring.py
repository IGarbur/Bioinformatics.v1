def expected_offspring(values):
    arr = values.split()
    for i in range(len(arr)):
        arr[i]=int(arr[i])
    #order: AA-AA,AA-Aa,AA-aa,Aa-Aa,Aa-aa,aa-aa (order obviously matters)
    #probbabilities of ofspring having dominant phenotype (at least 1 A) 
    probabilities = [1,1,1,0.75,0.5,0]
    e = 0
    num_offspring = 2
    #(number of couples of given genotype)*(probaility of that couple having domint phenotype) * number of offsprings
    for i in range(len(arr)):
        e+=(arr[i]*probabilities[i])*num_offspring
    return e

with open("C:\\Users\\elale\\Desktop\\writen\\text.txt","r") as file:
    contents = file.read()

e = expected_offspring(contents)
with open("C:\\Users\\elale\\Desktop\\writen\\result.txt","a") as result:
    result.write(str(e))


    