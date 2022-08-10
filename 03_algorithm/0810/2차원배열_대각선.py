'''

# 대각선
# 오른쪽 아래로 내려가는 대각선 (0, 0) (1, 1) (2, 2) (3, 3)
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

s = 0
for i in range(N):
    s += arr[i][i]
print(s)

# 왼쪽 아래로 내려가는 대각선
s = 0
for i in range(N):
    s += arr[i][N-1-i]
print(s)

# X자 형태로 두 대각선의 합 구하고 홀수일 때 중간에 중복되는 값 한 번 빼주기
s = 0
for i in range(N):
    s += arr[i][i]
for j in range(N):
    s += arr[j][N-1-j]
if N % 2: # 크기가 홀수일 때
    s -= arr[N//2][N//2]
print(s)


# 대각선을 기준으로 오른쪽 상단, 왼쪽 하단의 합을 각각 구해서 비교
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

pink = black = 0
for i in range(N):
    for j in range(N):
        if i < j:
            pink += arr[i][j] # 우상단
        elif i > j:
            black += arr[i][j] # 좌하단
print(pink, black)

## 두번째 방법
pink = black = 0
for i in range(N):
    for j in range(i+1, N):
        pink += arr[i][j] # 행 기준으로 더해짐
        black += arr[j][i] # 열 기준으로 더해짐
print(pink, black)
'''


# 사선의 합
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

s = [0]*(2*N-1) #각 사선의 합을 더해줄 리스트 생성
for i in range(N):
    for j in range(N):
        s[i+j] += arr[i][j]

print(s)

