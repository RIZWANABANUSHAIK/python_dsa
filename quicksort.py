def partitions(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<=pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1

def quicksort(arr,low,high):
    if low<high:
        pi=partitions(arr,low,high)
        quicksort(arr,low,pi-1)        #left pivot
        quicksort(arr,pi+1,high)  
                                          #right pivot

arr=[14,56,8,11,1,56]
quicksort(arr,0,len(arr)-1)
print(f'Sorted array: {arr}')
