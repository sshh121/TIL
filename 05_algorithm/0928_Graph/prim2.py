def prim2(r, V):
    MST = [0] * (V + 1)  # MST 포함 여부
    MST[r] = 1 # 시작 정점 표시
    s = 0
    for _ in range(V):  # V+1개의 정점 중 V개를 선택
        u = 0
        minV = 10000
        # MST에 포함된 정점 i와 인접 정점 j 중 MST에 포함될
        for i in range(V + 1):
            if MST[i]: # MST에 포함되어있다면
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