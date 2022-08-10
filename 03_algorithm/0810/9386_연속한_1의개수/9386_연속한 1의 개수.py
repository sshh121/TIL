import sys
sys.stdin = open('input.txt')

T = int(input())
# 방법 1
# arr은 연속한 개수에 대한 점수를 넣은 배열
# arr[i] = arr[i-1] * arr[i] + arr[i]

# 방법 2
# 카운트배열 cnt에 대해서 1을 만날 때 마다 +1을 해줌
# 0을 만나면 0으로 초기화
# arr[i] == 1 일 때 cnt += 1 (max를 갱신하며 최댓값과 비교하는 방법)


for tc in range(1, T+1):
    N = int(input())
    numbers = input()
    cnt = 0
    max_cnt = 0
    for idx in range(N):
        if numbers[idx] == '1':
            cnt += 1
            if cnt > max_cnt:
                max_cnt = cnt
        else:
            cnt = 0

    print(f'#{tc} {max_cnt}')


