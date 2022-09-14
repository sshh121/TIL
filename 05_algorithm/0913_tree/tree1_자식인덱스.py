'''
정점 번호 V : 1~(E+1)
간선 수 : E
부모 - 자식 순으로 연결 정보
4
1 2 1 3 3 4 3 5

4
2 1 2 3 1 4 1 5
'''
def find_root(V):
    for i in range(1, V + 1):
        if par[i] == 0:  # 부모가 없으면 root
            return i

E = int(input())
arr = list(map(int, input().split()))
V = E + 1
# root = 1 # 루트가 1번인지 알고있다고 가정
ch1 = [0]*(V+1)
ch2 = [0]*(V+1)
# 자식을 인덱스로 부모 번호 저장
par = [0]*(V+1)

for i in range(E):
    p, c = arr[i*2], arr[i*2 + 1]
    if ch1[p] == 0: # 아직 자식이 없으면
        ch1[p] = c # 자식 1로 저장
    else:
        ch2[p] = c # 자식 2로 저장
    par[c] = p
# print(par) # [0, 2, 0, 2, 1, 1]
# 1, 3번 자식의 부모는 2번 & 4, 5번 자식의 부모는 1번
root = find_root(V)
print(root)
