def insertionsort(arr):
    for i in range(len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
arr=[12,76,11,89,1]
insertionsort(arr)
print(arr)
