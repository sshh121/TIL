def f(i, k, r):
    if i == r: # i == k 팩토리얼 시
        print(p)
    else:
        for j in range(k):
            if used[j] == 0: # a[j]가 아직 사용되지 ㅇㄶ았으면
                used[j] = 1  # a[j]가 사용됨을 표시
                p[i] = a[j]  # p[i]는 a[j]로 결정
                f(i+1, k, r)    # p[i+1] 값을 결정하러 이동
                used[j] = 0  # a[j]를 다른 자리에서 쓸 수 있도록 해제

# 위에는 팩토리얼 형태이고, 순열을 사용하고 싶다면??
N = 5
R = 3
a = [_ for _ in range(1, N+1)]
used = [0] * N
p = [0] * R # 실제 저장할 공간
f(0, N, R) # N개 중에 R개만 고르겠다!
