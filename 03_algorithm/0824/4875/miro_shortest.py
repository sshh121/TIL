# 최단경로를 찾기 위해서는 모든 경로를 돌아봐야 함
# 모든 가능한 경로의 수까지 확인 가능
# dfs(i, j, N)
'''
1
5
11111
12001
10101
13001
11111
'''

def dfs(i, j, s, N):
    global minV
    if maze[i][j] == 3:
        if minV > s + 1:
            minV = s + 1
        return
    else:
        visited[i][j] = 1
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if maze[ni][nj] != 1 and visited[ni][nj] == 0: # 벽으로 둘러쌓여있기 때문에 범위 검사 따로 X
                dfs(ni, nj, s+1, N)
        visited[i][j] = 0 # 지우고 return해야 다른 경로를 찾음
        return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    sti, stj = -1, -1
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sti, stj = i, j
                break
        if stj != -1:
            break
    answer = 0              # 경로의 수
    minV = N*N
    visited = [[0]*N for _ in range(N)]
    dfs(sti, stj, 0, N)
    if minV == N*N:
        minV = -1
    print(minV)