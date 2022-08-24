p = 1 # 처음 줄 설 사람 번호
q = []

N = 20 # 초기 마이쮸
m = 0  # 나눠준 개수
v = 0

while m < N:
    input()
    q.append((p, 1, 0))  # 처음 줄 서는 사람, 몇 개 받아가는지, 나눠 줄 사탕 수
    print(q)
    v, c, my = q.pop(0)
    print(f'큐에 있는 사람 수 {len(q)+1}, 받아갈 사탕 수 {c}, 나눠준 사탕 수 {m}')
    m += c
    q.append((v, c+1, my+c))
    p += 1
print(f'마지막 받은 사람 : {v}')