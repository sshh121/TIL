arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(3):
    for j in range(3):
        print(i,j)
print('='*30)
# [1,4,7]
# [2,5,8]
# [3,6,9]로 만들고 싶다면?
# 전치행렬 -> [i][j] 와 [j][i]를 바꿔주면 됨
for i in range(3):
    print(*arr[i])

for i in range(3):
    for j in range(i+1, 3):
        # 대각선 기준으로 대칭인 값들을 서로 바꿔줌
        arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
print('='*30)
for i in range(3):
    print(*arr[i])

print('='*30)
# 전치행렬 만들기 -> 파이썬에서만 가능한 방식
# zip
arr = ['123', '456', '789']
arr = list(zip(*arr))
for i in range(3):
    print(*arr[i])