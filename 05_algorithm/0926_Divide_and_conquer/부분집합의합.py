def f1(i, k, t):
    global cnt
    cnt += 1
    if i == k:
        s = 0
        for j in range(10):
            if bit[j]:
                s += A[j]
        if s == t: # t: 목표 합
            for j in range(10):
                if bit[j]:
                    print(A[j], end=' ')
    else:
        bit[i] = 0
        f1(i+1, k, t)
        bit[i] = 1
        f1(i+1, k, t)

def f2(i, k, t, s, rs): # rs는 남은 애들의 합
    global cnt
    cnt += 1
    if i ==k:
        if t == s:
            for j in range(10):
                if bit[j]:
                    print(A[j], end=' ')
            print()
    elif t <= s: # 가지치기 가능 <- 값에 따라 효과가 다르긴 함
        return
    elif t > s + rs: # 추가적인 가지치기, 남은 애들의 합 + 현재의 합이 목표보다 작다면
        return # 중단
    else:
        bit[i] = 0
        f2(i + 1, k, t, s, rs-A[i])
        bit[i] = 1
        f2(i + 1, k, t, s+A[i], rs-A[i])

A = [i for i in range(1, 11)]
bit = [0] * 10
cnt = 0
# f1(0, 10, 5) # 합이 5인경우를 구합
f2(0, 10, 55, 0, sum(A))
print(cnt)