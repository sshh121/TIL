import sys
sys.stdin = open('input.txt')

def bfs(i, j, N):
    visited = [[0]*N for _ in range(N)]
    q = []
    q.append((i, j))
    visited[i][j] = 1       # 시작점 방문 표시
    while q:
        i, j = q.pop(0)
        # 정점에서 할 일? -> 도착지가 맞는가??
        if maze[i][j] == 3:
            return 1             # visited[i][j] : 거리 정보가 됨
        else:
            # 인접, 방문하지 않은 곳
            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]: # 오른쪽, 아래, 왼쪽, 위
                ni, nj = i+di, j+dj
                if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                    q.append((ni, nj))
                    visited[ni][nj] = visited[i][j] + 1
    return 0

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
    print(f'#{tc} {bfs(sti, stj, N)}')