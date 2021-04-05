
#timecomplexity=log(n)

def binarySearch(arr,low,high,x):
    if high>=low:
        mid = low + (high - low) // 2

        if arr[mid]==x:
            return mid
        elif arr[mid] > x:
    
           return binarySearch(arr,low,mid-1,x)
        else:
            return binarySearch(arr,mid+1,high,x) 

    else:
         return -1


arr = [ 2, 3, 4, 10, 40 ]
x = 10
result = binarySearch(arr, 0, len(arr)-1, x)
  
if result != -1:
    print ("Element is present at index % d" % result)
else:
    print ("Element is not present in array")



    
#--------------------------------------------------------------iterative--------------------------------------------------------------
def binarysearchiter(arr,l,h,x):
    while(l>=h):
        if arr[mid]==x:
            return mid 
        elif arr[mid]>x:
            h=mid-1 
        else:
            h=mid+1 
    return -1  
print(binarySearch([1,2,3,4],0,3,5))