'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
# 주어진 트리를 root부터 순회하는 경우 마지막 정점은? last
# 서브 트리의 노드 개수는? cnt

def find_root(V):
    for i in range(1, V + 1):
        if par[i] == 0:  # 부모가 없으면 root
            return i

def preorder(n): # 전위 순회
    # global cnt
    global last
    if n: # n이 0이 아니면
        # print(n) # visit(n)
        # cnt += 1 # 서브트리의 정점 개수를 알고 싶다면
        last = n
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

V = int(input())
arr = list(map(int, input().split()))
# root = 1 # 루트가 1번인지 알고있다고 가정
ch1 = [0]*(V+1)
ch2 = [0]*(V+1)
# 자식을 인덱스로 부모 번호 저장
par = [0]*(V+1)

for i in range(V-1):
    p, c = arr[i*2], arr[i*2 + 1]
    if ch1[p] == 0: # 아직 자식이 없으면
        ch1[p] = c # 자식 1로 저장
    else:
        ch2[p] = c # 자식 2로 저장
    par[c] = p

root = find_root(V)
cnt = 0
last = 0
preorder(3)
# print(cnt)
print(last)