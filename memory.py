def create_var(var_name,obj,idx,stack,heap):
    if isinstance(obj,str) and obj in stack: #you have to be caraeful not to pass list as a key, cuz list isn't hashible
        #if statement is when you try to reasign pointer that already was referncing something in a heap
        if var_name in stack:
            del_var(var_name, stack, heap) #you can't just straight up delete something in a heap cuz other pointer might be pointing to that object
            
        stack[var_name]=stack[obj]
        arr = heap[stack[obj]]
        arr[1]+=1
        return idx
        
    if var_name in stack:
        heap[stack[var_name]]=[obj,1]
        return idx
    else:
        stack[var_name]=idx
        heap[idx]=[obj,1]
        idx+=1
        return idx
        

def del_var(var_name,stack,heap):
    if var_name in stack:
        idx = stack[var_name]
        arr = heap[idx]
        arr[1]-=1
        if arr[1]<=0:
            del heap[idx]
        del stack[var_name]
    else:
        print("The pointer you are trying to delete doesn't exist")
def display(stack,heap):
    print(stack)
    print(heap)
    print("-"*30)
    
def main():
    stack = {} #x:id                "x":0
    heap = {} #id:[[1,2,3],count]   0:[[1,2,3],1]
    idx = 0
    display(stack,heap)
    
    idx = create_var("x",[1,2,3],idx,stack,heap)
    display(stack,heap)
    
    idx = create_var("y",[4,5,6],idx,stack,heap)
    display(stack,heap)
    
    #interesting case where you change the reference but value in heap that is associated with that id,, remains
    idx = create_var("y","x",idx,stack,heap)
    display(stack,heap)
    
    idx = create_var("c","x",idx,stack,heap)
    display(stack,heap)
    
    del_var("x",stack,heap)
    display(stack,heap)
    
    del_var("y",stack,heap)
    display(stack,heap)
    
    del_var("c",stack,heap)
    display(stack,heap)
    
main()