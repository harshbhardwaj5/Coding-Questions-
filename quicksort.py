def partition(ls,low,high):
    i=(low-1) 
    pivot=ls[high]
    for j in range(low,high):
        if ls[j]<pivot :
            i+=1
            ls[i],ls[j]=ls[j],ls[i] 
    ls[i+1],ls[high]=ls[high],ls[i+1]  
    return i+1

    
        
def quick(arr,low,high) :
    if low<=high:
         pi=partition(ls,low,high)
         quick(ls,low,pi-1)  
         quick(ls,pi+1,high)  
ls= [10, 7, 8, 9, 1, 5]
n = len(ls)
quick(ls, 0, n-1)
print("Sorted array is:")
print(ls)
  
ls=[1,3,4,5,6,39,9]
