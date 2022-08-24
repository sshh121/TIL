N = 3
q = [0] * N
front, rear = -1, -1

rear += 1 # enqueue(10)
q[rear] = 10

rear += 1 # enqueue(20)
q[rear] = 20

rear += 1 # enqueue(30)
q[rear] = 30

# rear += 1 # enqueue(40)
# q[rear] = 40 => 지정해놓은 크기보다 많은 원소가 들어가려 함

front += 1 # dequeue()
print(q[front]) # 원소를 지우는 것이 아니라, 값 자체가 무시되는 것

front += 1 # dequeue()
print(q[front])

front += 1 # dequeue()
print(q[front])