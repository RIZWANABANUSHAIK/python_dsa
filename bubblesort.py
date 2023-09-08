def bubblesort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                print(arr)
            else:
                print(arr)
        print()

arr = [64, 34, 25, 12, 22, 11, 90]
 
ans=bubblesort(arr)
print(arr)