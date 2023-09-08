# stack can be implemented using  list (LIFO)
#and also by using modules
#by using append and pop method using list
# for push ----> append
# for pop------>pop
stack=[]
# stack.append(10)
# stack.append(20)
# stack.append(30)
# stack.append(40)
# stack.append(60)
# print(stack)
# stack.pop()
# print(stack)
# stack.pop()
# print(stack)
# stack.pop()
# print(stack)
# stack.pop()
# print(stack)
# stack.pop()
# print(stack)

# # for check empty
# if len(stack)==0:
#     print("true")

# # for accesing last element
# stack[-1]
def push():
    element= int(input("enter element:"))
    stack.append(element)
    print(stack)

def pop():
    if len(stack)!=0:
        ele= stack.pop()
        print("removed element is ",ele)
        print(stack)
    else:
        print("we cant remove the element from empty stack")
while True:
    choice= int(input("enter which operation you have to perform 1.push   2.pop  3.quit"))
    if choice==1:
        push()
    elif choice ==2:
        pop()
    elif choice ==3:
        break
    else:
        print("enter the correct operator")
