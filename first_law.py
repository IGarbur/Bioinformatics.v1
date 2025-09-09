#Mendel's first law
'''Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k
 individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected 
mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype).
 Assume that any two organisms can mate.'''



def prob_of_dominant(k,m,n):
    # 1-probability of recessive offspring
    # irrelivant crossings
    # AA x AA
    # AA x Aa, Aa x AA
    # AA x aa, aa x AA
    z =k+m+n
    #Aa x Aa
    het_het = (m/z)*((m-1)/(z-1))*(1/4)
    #aa x Aa and Aa x aa thus 2*
    rec_het_and_het_rec = ((n/z)*(m/(z-1))*(2/4))*2
    #aa x aa
    rec_rec = (n/z)*((n-1)/(z-1)) #*4/4
    prob_rec = het_het + rec_het_and_het_rec + rec_rec
    return 1 - prob_rec

k = 17
m = 21
n = 25
print(prob_of_dominant(k,m,n))
