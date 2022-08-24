# 1219. 길찾기 -> BFS로 풀어보기
def bfs(v, N, t):                        # v 시작, N 마지막 정점 번호, t 찾는 정점
    visited = [0] * (N+1)
    q = []
    q.append(v)
    visited[v] = 1
    while q:
        v = q.pop()                     # v를 반환하고
        if v == t:                      # 탐색에서 할 일을 적어줌!
            return 1                    # 목표 발견
            # 만약 return visited[99]이면 99번 정점까지 몇 단계를 거쳐왔는지 확인 가능
        for w in adjList[v]:            # v에 인접하고 방문안한 w 인큐, 표시
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[v] + 1

    return 0                            # 목표를 발견하지 못한다면

T = 1
for _ in range(T):
    tc, E = map(int, input().split())
    arr = list(map(int, input().split()))

    adjList = [[] for _ in range(100)]
    for i in range(E):
        a, b = arr[i*2], arr[i*2 + 1]
        adjList[a].append(b)            # 단방향임에 주의!!

    print(bfs(0, 99, 99))               # 시작 정점, 마지막 정점, 타겟 정점
