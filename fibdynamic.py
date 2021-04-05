def dynamicfib():
    n=int(input())
    fib=[0]*n
    fib[0]=0 
    fib[1]=1 
    for i in range(2,n):
        fib[i]=fib[i-1]+fib[i-2]

    print(fib[n-1])

def recursionfib(n): 
    if n<0:
        print("Invalid Output")
    elif n==0 or n==1:
        return n 
    else:
        return recursionfib(n-1)+recursionfib(n-2)





def simplefib(n):
    first=0 
    second=1 
    for i in range(2,n+1):
        temp=first+second 
        first=second 
        second=temp
    return second



n=int(input())
print(simplefib(n))
# for i in range(n):
#     print(recursionfib(i)) 





