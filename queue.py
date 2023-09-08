queue=[]
def enqueue(queue,item):
	queue.append(item)
	print("added item ",item)
def dequeue(queue):
	if not queue:
		print("queue is empty")
	else:
		e=queue.pop(0)
		print("removed item is ",e)

enqueue(queue,10)
enqueue(queue,20)
enqueue(queue,30)
enqueue(queue,40)
dequeue(queue)
dequeue(queue)
dequeue(queue)
dequeue(queue)
dequeue(queue)
print(queue)
