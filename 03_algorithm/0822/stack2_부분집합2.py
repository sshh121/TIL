def f(i, N, s, t):               # 이전까지 합인 s와 내가 찾고자 하는 값 t
    global answer
    global cnt
    cnt += 1
    if i == N:                   # 모든 원소가 고려된 경우
        if s == t:               # 지금까지 구한 부분집합의 합이 t이면
            answer += 1
        return
    elif s > t:                  # 지금까지 더한 합이 목표값보다 크다면
        return                   # 되돌아감 -> 목표값이 작을 경우는 가지치기로 경로를 많이 줄일 수 있음
    else:
        f(i+1, N, s+A[i], t)     # A[i]가 포함된 경우
        f(i+1, N, s, t)          # A[i]가 포함되지 않는 경우의 합을 넘겨주는 것


A = list(range(1, 11))
bit = [0] * 10
answer = 0
cnt = 0
f(0, 10, 0, 10)
print(answer, cnt)