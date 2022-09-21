def f(i, k):
    if i == k:      # i번 인덱스가 원소의 개수와 같아지면 (완성되면)
        print(p)
    else:
        for j in range(i, k): # 옆으로 가면서 자리 바꾸기
            p[i], p[j] = p[j], p[i]
            f(i+1, k)
            p[i], p[j] = p[j], p[i] # 원상복구 하고 다시 순열

p = [1, 2, 3, 4, 5]
f(0, 5) # 0번부터 시작하고 워소의 개수는 3개(5개)
