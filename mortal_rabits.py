# for each generation 
#total rabbits -> total number of rabbits alive this generation (Adults and Small)
#small rabits -> newly born rabits aren't mature yet
#new offspring will come from mature rabbits meaning -> total rabbits - small rabbits = mature rabits
# [total number of rabbits, small rabits which are offspring of previous generation] 
#death = now to find these rabbits that will die 
# we need to subtract from our current generation n from total number of rabbits the offspring that were born m months ago (n-m)
#make sure that n - m isn't negative
#next_total = current_total + newborns - deaths
gen = 97
arr =[[1,1],[1,0]]
age_of_death = 20

for i in range(2,gen):
    if i>=age_of_death:
        deaths = arr[i-age_of_death][1]
    else:
        deaths = 0
    newborns = arr[i-1][0]-arr[i-1][1]
    current_total = arr[i-1][0]

    next_total = current_total + newborns - deaths
    arr.append([next_total,newborns])

with open("C:\\Users\\elale\\Desktop\\writen\\result.txt","a") as file:
    file.write(str(arr[-1][0]))





#I actully programmed it first using OOP and it was easier to implement
'''class Litter:
    def __init__(self):
        self.rabbits = []
        self.count = 0
    def add(self,rabbit):
        self.rabbits.append(rabbit)
        self.count+=1
    def remove(self,rabbit):
        self.rabbits.remove(rabbit)
        if self.count > 0:
            self.count-=1
        else:
            print("There are no rabbits in the litter")

class Rabbit:
    def __init__(self):
        self.months_old = 0

    def reproduce(self,litter):
        if self.months_old > 0:
            litter.add(Rabbit())
        self.months_old+=1
        
    def die(self,litter,age_of_death):
        if self.months_old >= age_of_death:
            litter.remove(self)

gen = 1
final_gen = 6
age_of_death = 3
r1 = Rabbit()
l1 = Litter()
l1.add(r1)
while gen!=final_gen:
    for rabbit in l1.rabbits[:]:
        rabbit.reproduce(l1)
        rabbit.die(l1,age_of_death)
    #print(l1)
    gen+=1
print(l1.count)'''


