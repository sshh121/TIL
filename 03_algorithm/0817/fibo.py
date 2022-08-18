# 재귀
def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
for i in range(21):
    print(i, fibo(i))


# memoization -> 실행 속도 빨라짐
def fibo(n):
    if memo[n] == -1:
        memo[n] = fibo(n-1) + fibo(n-2)   # 계산된 적 없으면 새로 계산해야 함
    return memo[n]
memo = [-1]*101
memo[0] = 0
memo[1] = 1
for i in range(101):
    print(i, fibo(i))


# memoization_webex
# def fibo(n):
#     if n >= 2 and len(memo) <= n:
#         memo.append(fibo(n-1) + fibo(n-2))
#     return memo[n]
#
# memo = [0, 1]
# print(fibo(8))
# print(memo)