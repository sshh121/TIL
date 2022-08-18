def f(n):           # 팩토리얼 1! = 1
    if n <= 1:
        return 1
    else:
        return n * f(n-1)

for i in range(21):
    print(i, f(i))