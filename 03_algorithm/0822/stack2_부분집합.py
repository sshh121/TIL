def f(i, N): # i번 인덱스
    global answer
    global cnt
    cnt += 1
    if i == N: # 인덱스와 원소의 개수가 같아지면 출력
        s = 0 # 부분집합의 합 구하기 위함
        for i in range(N):
            if bit[i]: # 해당 비트가 1이면
                # print(A[i], end = ' ') # 각 부분집합에 들어가는 원소를 출력
                s += A[i]
        # print()
        if s == 10: # 합이 10이 되는 경우
            answer += 1 # 부분집합의 합이 10인 경우의 수
    else:
        candidate = [0, 1]
        for x in candidate:
            bit[i] = x
            f(i+1, N)
        # bit[i] = 1 # A[i]가 부분집합에 포함
        # f(i+1, N) # 다음으로 가서 비교
        # bit[i] = 0
        # f(i+1, N)

A = list(range(1, 11))
bit = [0] * 10
answer = 0
cnt = 0
f(0, 10)
print(answer, cnt)