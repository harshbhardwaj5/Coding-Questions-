# count freq using dict
def countfreq():
    ls=[2,4,6,67,7,7,7,1]
    dic={}
    for i in range(len(ls)):
        dic[ls[i]]=dic.get(i,0)+1 
    print(dic)
    for i in dic:
        print(i,dic[i],dic.get(i,0))

def coutsort(arr,n):
    l=[0]*n                       # give this range not 100 or 10 equal to size of array
    coun=[0]*100


    for i in range(len(arr)):
        coun[arr[i]]+=1 
    


    for i in range(1,100):
        coun[i]+=coun[i-1]
    j=len(arr)-1  



    while j>=0:
        l[coun[arr[j]]-1]=arr[j]
        coun[arr[j]]-=1                   # very very imp step dont fuckit
        j-=1 




    for i in range(0, n):
        arr[i] = l[i]
    print(arr)
     
ls=[65,9,8,7,55]
coutsort(ls,len(ls))



