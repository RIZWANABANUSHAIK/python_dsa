import sys                           # without using buit in functions
arr=[12,34,556,11,90,13]
print("before:",arr)
for i in range(len(arr)):
    min_idx =i
    for j in range(i+1,len(arr)):
        if arr[min_idx]>arr[j]:
            min_idx=j
    arr[min_idx],arr[i]=arr[i],arr[min_idx]
print ("Sorted array")
for i in range(len(arr)):
    print("%d" %arr[i],end=" ")

# with using built in functions
# for i in range(len(arr)-1):
#     min_val=min(arr[i:])
#     index_min_val=arr.index(min_val,i)
#     arr[i],arr[index_min_val]=arr[index_min_val],arr[i]
# print("after:",arr)
