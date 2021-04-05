arr=[5,34,6,2,5]
minn=arr[0]
for i in range(len(arr)):
    minn=i
    for j in range(i+1,len(arr)):
        if arr[j]<arr[minn]:
            minn=j 
    arr[minn],arr[i]=arr[i],arr[minn] 
print(arr)