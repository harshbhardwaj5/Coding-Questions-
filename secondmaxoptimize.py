arr=[]
arr=list(map(int,input().split()))
first=second=-2147483648
for i in range(len(arr)):
    if arr[i]>first:
        second=first 
        first=arr[i]
        
    elif arr[i]<first and arr[i]>second:    #---------->our target is smaller than first rember that toh second ko toh ab bigger se replace karoga acc to condition
        second=arr[i]

print(second)