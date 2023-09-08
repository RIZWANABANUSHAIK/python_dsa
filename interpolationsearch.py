def interpolation_search(arr,lo,hi,x):
    if (lo<=hi and x>=arr[lo] and x<=arr[hi]):
        pos = lo + ((hi - lo) // (arr[hi] - arr[lo]) *(x - arr[lo]))
        if arr[pos] == x:
            return pos
        elif arr[pos]<x:
            return interpolation_search(arr,pos+1,hi,x)
        else:
            return interpolation_search(arr,lo,pos-1,x)

    return -1
arr = [10, 12, 13, 16, 18, 19, 20,21, 22, 23, 24, 33, 35, 42, 47]
n = len(arr)
x = 18
index = interpolation_search(arr, 0, n - 1, x)
if index!= -1:
    print(x, "is found at index",index)
else:
    print("key is not found")