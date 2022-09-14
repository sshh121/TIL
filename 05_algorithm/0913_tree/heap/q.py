import heapq # 우선순위 큐 만들 수 있음

data = [3, 6, 9, 1, 8, 2]

heapq.heapify(data)
print(data) # [1, 3, 2, 6, 8, 9]

heapq.heappop(data)
print(data) # [2, 3, 9, 6, 8]

heapq.heappop(data)
print(data) # [3, 6, 9, 8]