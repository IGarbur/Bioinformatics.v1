def process_1(n):
    for i in range(n):
        print(f"Process 1: Stored {i}")
        yield i #saves the kinda like a state of a CPU 

def process_2(n):
    for i in range(n):
        print(f"Process 2: Stored {i}")
        yield i

x = process_1(5) #created an iterator object
y = process_2(5) #created an iterator object

#make sure that you don't go out of bounds aka StopIteration
#Think about this: if one iteration stops sooner than the other
#but what if you stop Iteration for one of processes will the other process be finished?
#you need to synchronize them (need a check)
while True:
    try:
        x.__next__() #you can write this as "next(x)"
    except:
        x = None #when you reach the end of object that is a process, you set the object to None
    try:
        y.__next__()
    except:
        y = None
    if x == None and y == None: #when both processes are finished
        break

