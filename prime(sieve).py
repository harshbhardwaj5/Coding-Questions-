ls=list(map(int,input().split()))
prime=[]

for i in range(0,len(ls)):
    prime.append(1)
prime[0]=0
prime[1]=0
for i in range(2,len(ls)):
    if prime[i]==1:
        for j in range(2,len(ls)):
            if i*j>=len(ls):
                break 
            else:
                prime[i*j]=0

c=1
for i in range(1,len(prime)):
    c+=1 
    if prime[i]==1:
        print(ls[c]) 


