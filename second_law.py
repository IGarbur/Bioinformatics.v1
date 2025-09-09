#first number is k = number of generations
#second number is (at least x) individuals of genotype AaBb

#The question is asking for 
#probability of at least x individuals of type AaBb after k generations

#This is a Binomial Probability distribution
#why?
#1) fixed number of trials (k generations)
#2) 2 possible outcomes of each trial:
#       - success: AaBb -> 0.25 
#       - failure: all other genotypes: 0.75
#3) Probability of success is constant: 0.25
#4) Each trial is independent (Independent Segregation of Allelles)

# Formula:
#Combinations: (n!/((n-i)!*i!)) total arremgements/ (arrangement of failures * arrengemnts of success)
#p^i -> p = probability of success, and i = number of successes
#(1-p)^(n-1) -> 1-p probability of failure, and n-i = number of failures
# n = 2^k 
def get_n(k):
    return 2**k

def factorial(n):
    if n == 0:
        return 1
    fact = n
    for i in range(n-1,0,-1):
        fact *= i
    return fact

def combinations(n,i):
    return factorial(n)/((factorial(n-i))*factorial(i))

def prob_of_specific_success(p,n,x):
    #print(f"{combinations(n,x)}*{(p)**x}*{(1-p)**(n-x)}={combinations(n,x) * ((p)**x) * ((1-p)**(n-x))}")
    return combinations(n,x) * ((p)**x) * ((1-p)**(n-x))

def prob_of_at_least_x_successes(p,n,x):
    sum = 0
    for i in range(n-x+1):
        sum+=prob_of_specific_success(p,n,x+i)
    return sum

with open("C:\\Users\\elale\\Desktop\\writen\\text.txt","r") as file:
    contents = file.read()
    arr = contents.split()
k = int(arr[0])
x = int(arr[1])

p = 0.25
n = get_n(k)

with open("C:\\Users\\elale\\Desktop\\writen\\result.txt","a") as result:
    result.write(str(prob_of_at_least_x_successes(p,n,x)))