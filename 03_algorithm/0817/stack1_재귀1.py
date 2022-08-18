# i : 현재 단계, N : 목표치
# i를 N이 될때까지 계속 더해줌, N은 그대로
def f(i, N):
 if i == N:
     print(i)
     return
 else:
     print(i)
     f(i+1, N)      # 재귀호출
f(0, 1000)          # 재귀 호출 깊이가 생각보다 깊지 않기 때문에
                    # 1000번 이하로 하는 것이 좋은 듯