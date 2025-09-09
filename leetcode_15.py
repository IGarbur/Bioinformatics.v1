arr = [-4,-1,-1,0,1,2]
result = []
for i in range(len(arr)):
    if i > 0 and arr[i] == arr[i-1]: #skip duplicates for i
        continue
    
    j = i+1
    k = len(arr)-1
    while j<k:
        if arr[j]+arr[k]+arr[i]==0:
            result.append([arr[i],arr[j],arr[k]])
            j+=1
            k-=1
            # after finding a sequence you need to make sure that the next j isn't a duplicate
            while j<k and arr[j]==arr[j-1]:
                j+=1
            # after finding a sequence you need to make sure that the next k isn't a duplicate
            while j<k and arr[k]==arr[k+1]:
                k-=1
        elif arr[j]+arr[k]+arr[i]<0:
            j+=1
        else:
            k-=1
print(result)