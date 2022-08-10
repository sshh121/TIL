# N = int(input())
# arr =[list(map(int, input())) for _ in range(N)]
# print(arr)

# 개별 원소 접근 원할 시
# for i in range(N):
#     for j in range(N):
#         print(arr[i][j], end=' ')

## delta
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
arr = [[1, 2, 3, 4], [4, 5, 6, 7]]
N = 2
M = 4
for i in range(N):
    for j in range(M):
        for k in range(4): #방향이 4개
            ni = i+di[k]
            nj = j+dj[k]
            if 0 <= ni < N and 0 <= nj < M:
                print(ni, nj)

# 두 개씩
for i in range(N):
    for j in range(M):
        for d in range(1,3): #거리가 2
            for k in range(4): #방향이 4개
                ni = i + di[k]*d
                nj = j + dj[k]*d
                if 0 <= ni < N and 0 <= nj < M:
                    print(ni, nj)