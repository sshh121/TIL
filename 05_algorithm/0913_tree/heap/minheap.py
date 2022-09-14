# N
N = 6
# data
data = [3, 6, 9, 1, 8, 2]
'''
       3
   6       9
 1   8   2
 
인덱스는 
        1
   2          3
4     5    6
'''

# 최소 힙 구성
# tree = 리스트로 표현
# 0번 idx는 사용하지 않는다.
tree = [0 for _ in range(N+1)]
# tree는 빈 리스트이고, last에 계속 값을 넣을 것임
last = 1 # last를 초기화

for i in range(len(data)):
    # 트리에 값이 아무것도 추가되지 않았다면
    if not tree[i]: # i번째 값이 0이면
        tree[last] = data[i]
    else:
        last += 1 # 내가 집어넣을 수 있는 위치
        child = last # 새로 추가된 정점을 자식으로 둘 꺼
        parent = child // 2 # 완전이진트리에서 부모는 항상 자식을 2로 나눈 몫

        tree[child] = data[i]
        print(tree, child, parent)

        # tree에 요소 추가하면서 최소힙 만듦듦
       # 부모가 있고, 부모가 자식보다 작아야 됨 (최소힙 조건)
        while parent >= 1 and tree[parent] > tree[child]:
            # 부모와 자식 위치 변경
            tree[parent], tree[child] = tree[child], tree[parent]
            child = parent
            parent = parent // 2
print(tree) # 최종 모양 [0, 1, 3, 2, 6, 8, 9]

