import sys
sys.stdin = open('input.txt', encoding='utf-8') # 입력 데이터에 깨지는 현상이 발생할 수 있음

### 1. 함수 정의 - while문
def bruteForce(pattern, target):
    # 현재 조사 대상인 각 idx 초기화
    p_idx, t_idx = 0, 0
    # 패턴이 몇 번 나오느냐
    count = 0
    while t_idx < len(target):
        # 조사 대상을 변수에 담아서 사용
        t = target[t_idx]
        p = pattern[p_idx]

        # 두 값이 서로 다를 때
        if t != p:
            t_idx = t_idx - p_idx
            p_idx = -1

        t_idx += 1
        p_idx += 1

        # 만약 모든 패턴 조사가 다 끝났다면
        if p_idx == len(pattern):
            # 패턴이 한 번 일치한다
            count += 1
            p_idx = 0

    return count

for _ in range(10):
    tc = int(input())
    word = input()
    sentence = input()
    print(f'#{tc} {bruteForce(word, sentence)}')



#---------------------------------------------------
### 2. 함수 정의 - for문
def bruteForce(pattern, target):
    count = 0
    for i in range(len(target)- len(pattern) + 1):
        for j in range(len(pattern)):
            # 두 값이 다른 경우가 나올 때까지
            if pattern[j] != target[i+j]:
                break
        else: # break된 적 없이 for문이 다 돌아갔다면
            count += 1
    return count

for _ in range(10):
    tc = int(input())
    word = input()
    sentence = input()
    print(f'#{tc} {bruteForce(word, sentence)}')



#-----------------------------------------------------
### for문
for _ in range(10):
    tc = int(input())
    word = input()
    sentence = input()
    cnt = 0
    for i in range(len(sentence) - len(word) + 1):
        for j in range(len(word)):
            if sentence[i+j] != word[j]:
                break
        else: # for문 다 돌아가고 난 후 else문 실행
            cnt += 1

    print(f'#{tc} {cnt}')



#-------------------------------------------------
### 내 생각
for _ in range(10):
    tc = int(input())
    word = input()
    sentence = input()
    l_w = len(word)
    l_s = len(sentence)
    # 문장을 순회하면서 word를 찾아내야 함 <- idx 활용
    i = 0
    j = 0
    cnt = 0
    while i < l_s:
        f_i = i
        if sentence[i] == word[j]:
            i += 1
            j += 1
            if j == l_w:
                cnt += 1
                j = 0
        else:
            i = i - j # 단어의 길이만큼 되돌아가야됨
            i += 1
            j = 0

    print(f'#{tc} {cnt}')

