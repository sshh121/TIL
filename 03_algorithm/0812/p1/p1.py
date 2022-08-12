import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    word = input()
    # 슬라이싱
    print(f'#{tc} {word[::-1]}')

    # reversed 내장 함수
    result = list(reversed(word))
    # list-> 문자열
    print(f'#{tc} {"".join(result)}')

    # 뒤에서부터 더해나가면 배열을 뒤집는 것과 동일
    result = ''
    for idx in range(len(word)-1, -1, -1):
        result += word[idx]
    print(f'#{tc} {result}')