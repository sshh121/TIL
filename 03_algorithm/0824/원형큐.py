N = 3
q = [0] * N
front, rear = 0, 0

rear = (rear+1) % N # enqueue(10)
q[rear] = 10

rear = (rear+1) % N # enqueue(20)
q[rear] = 20

rear = (rear+1) % N # enqueue(30)
q[rear] = 30

rear = (rear+1) % N # enqueue(40)
q[rear] = 40
# 크기보다 넘치게 원소를 추가할 수는 있지만, 이전의 원소가 덮어씌워짐

front = (front + 1) % N # dequeue()
print(q[front]) # 원소를 지우는 것이 아니라, 값 자체가 무시되는 것

front = (front + 1) % N # dequeue()
print(q[front])

front = (front + 1) % N # dequeue()
print(q[front])