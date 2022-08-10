
N = 3 # 행
M = 4 # 열
# N개의 원소를 갖는 0으로 초기화된 1차원 배열
arr1 = [0]*N

# 크기가 NxM이고 0으로 초기화된(비어있는) 2차원 배열
arr2 = [[0]*M for _ in range(N)]
print(arr2)

arr_ = [[0]*M]*N # 얕은복사
# 1차원 배열 하나만 만들어놓고, 그 배열을 가리키는 레퍼런스를 3개 만든 것
arr_[0][0] = 1
print(arr_)

arr3 = [[1], [2, 3], [3, 4, 5]]
print(arr3)


# 배열의 합
# 외부에서 읽을 때, 2차원 배열 원소의 합을 구하는 경우
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

s = 0
for i in range(N):
    for j in range(N):
        s += arr[i][j]
print(s)


# 각 행의 합과 그 중 최댓값 출력

#3
#1 2 3
#4 5 6
#7 8 9

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

maxV = 0 # 최댓값을 넣을 변수를 설정 (최대 행의 합)
for i in range(N): # 각 행에 접근
    rs = 0 # 행의 합 값을 초기화
    for j in range(N): # 각 i행의 j열에 접근
        rs += arr[i][j]
    if maxV < rs:
        maxV = rs
print(maxV)

