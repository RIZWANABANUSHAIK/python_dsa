def search(arr,x):
    for index,value in enumerate(arr):
        if value == x:
            return index
    return None

arr=[10,20,3,4,5]
x=10
ans = search(arr,x)
if ans!= None:
    print(x,"is found at the position",ans)
else:
    print("key is not found")