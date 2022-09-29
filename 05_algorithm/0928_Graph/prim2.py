# MST에 포함되는 모든 정점과 연결된 간선 중 가장 작은 값 선택
# 노드 수가 많아지면 느려지는 것처럼 보이는 단점..
def prim2(r, V):
    MST = [0] * (V + 1)  # MST 포함 여부
    MST[r] = 1 # 시작 정점 표시
    s = 0 # MST 간선의 가중치 합
    for _ in range(V):  # V+1개의 정점 중 V개를 선택 (V번 반복)
        u = 0
        minV = 10000
        # MST에 포함된 정점 i와 인접 정점 j 중 MST에 포함될
        for i in range(V + 1): # 0 ~ V번 노드를 순회하면서
            if MST[i]: # MST에 포함되어 있는 정점이면
                for j in range(V+1):
                    if adjM[i][j] > 0 and MST[j]==0 and minV>adjM[i][j]:
                        u = j
                        minV = adjM[i][j]
        s += minV
        MST[u] = 1
    return s


V, E = map(int, input().split())
adjM = [[0] * (V + 1) for _ in range(V + 1)]
adjL = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    adjM[u][v] = w
    adjM[v][u] = w  # 가중치가 있는 무방향 그래프

print(prim2(0, V))