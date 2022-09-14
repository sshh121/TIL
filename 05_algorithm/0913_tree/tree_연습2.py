'''
    1
 2     3
     4   5
------------
4
1 2 1 3 3 4 3 5
'''

def find_root(V):
    for i in range(1, V + 1):
        if par[i] == 0:  # 부모가 없으면 root
            return i

def preorder(n): # 전위 순회
    # global cnt
    global last
    if n: # n이 0이 아니면
        print(n) # visit(n)
        preorder(ch1[n])
        preorder(ch2[n])

def inorder(n): # 중위 순회
    if n:
        inorder(ch1[n])
        print(n) # visit(n)
        inorder(ch2[n])

def postorder(n): # 후위 순회
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(n)

def f(n):  # global cnt 없이 방문한 정점 수를 리턴하는 함수
    # L R V 각각의 리턴 값을 더해주면 됨..?
    # 자식이 없을 때는 0을 리턴
    if n == 0: # 서브트리가 비어있으면 (자식이 없으면)
        return 0
    else:
        L = f(ch1[n])
        R = f(ch2[n])
        return L + R + 1


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

root = find_root(V)
# print(f(root)) # 서브트리의 정점 수 5개
print(f(3)) # 서브트리의 정점 수 3개