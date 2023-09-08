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

def exponentialsearch(arr,n,x):
    if arr[0] == x:
        return 0
    i = 1
    while i < n and arr[i] <= x:
        i = i * 2
    return binarysearch( arr, i // 2, min(i, n-1), x)

arr=[20,30,40,50,60]
x=20
n=len(arr)
ans=exponentialsearch(arr,n,x)
if ans!=-1:
    print(x,"is found at index",ans)
else:
    print("given key is not present")