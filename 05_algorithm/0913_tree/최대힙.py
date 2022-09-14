'''
2 5 7 3 4 6
'''
# 삽입
def enq(n):
    global last
    last += 1 # 완전 이진 트리에서 마지막 정점 추가
    heap[last] = n # 마지막 정점에 key 추가
    # 부모가 있고, 부모 < 자식인 경우 자리 교환
    # 즉, 부모가 없거나 부모 > 자식 조건을 만족할 때까지
    c = last
    p = c // 2 # 완전 이진 트리에서 부모 정점 번호
    while p and heap[p] < heap[c]: # 고유한 값이기 때문에 =은 고려 X
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2

# 삭제
def deq():
    global last
    tmp = heap[1] # 루트 백업 (버리는 것이 아니라 리턴값으로)
    heap[1] = heap[last] # 삭제할 노드의 키를 루트에 복사
    last -= 1 # 마지막 노드 삭제
    p = 1 # 루트에 옮긴 값을 자식과 비교
    c = 2*p # 왼쪽 자식부터 계산
    while c <= last: # 자식이 하나라도 있으면
        if c + 1 <= last and heap[c] < heap[c+1]: # 오른쪽 자식도 있고, 오른쪽 자식이 더 크면
            c += 1 # 비교 대상을 오른쪽 자식으로 정함
        if heap[p] < heap[c]: # 부모보다 자식이 더 크면 최대힙 규칙에 어긋남
            heap[p], heap[c] = heap[c], heap[p]
            # 교환했다면 밑의 자식과 또 비교할 필요가 있으므로
            p = c # 자식을 새로운 부모로 잡고
            c = p * 2 # 왼쪽 자식으로 설정
        else: # 그렇지 않다면
            break # 비교를 중단
    return tmp


# 최대힙
heap = [0] * 100 # 최대 크기는 100
last = 0 # 현재 노드가 하나도 없는 상태

enq(2)
enq(5)
enq(7)
enq(3)
enq(4)
enq(6)
while last:
    print(deq()) # 내림차순으로 꺼내짐