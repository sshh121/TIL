def f(i, k):
    if i == k:      # i번 인덱스가 원소의 개수와 같아지면 (완성되면)
        global minV
        if i == k:  # 인덱스 i == 원소의 개수
            s = 0   # 모든 j행에서 p[j]열을 골랐을 때 sum(합)
            for j in range(k):
                s += arr[j][p[j]]
            if minV > s:
                minV = s
    else:
        for j in range(i, k):
            p[i], p[j] = p[j], p[i]
            f(i+1, k)
            p[i], p[j] = p[j], p[i]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    p = [_ for _ in range(N)] # p[i]는 i행에서 선택한 열 번호가 들어있음
    minV = N*9
    f(0, N)
    print(f'#{tc} {minV}')