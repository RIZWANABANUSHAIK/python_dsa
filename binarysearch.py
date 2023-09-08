def binarysearch(arr,l,h,x):
    if h>=l:
        mid=l+(h-l)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return binarysearch(arr,l,mid-1,x)
        else:
            return binarysearch(arr,mid+1,h,x)
    else:
        return -1

arr=[20,30,40,50,60]
x=100
ans=binarysearch(arr,0,len(arr)-1,x)
if ans!=-1:
    print(x,"is found at index",ans)
else:
    print("given key is not present")
