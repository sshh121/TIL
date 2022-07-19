score = {'python':80, 'django':89, 'web':83}

# 1. algorithm 90점 추가
score['algorithm'] = 90
print(score)

# 2. python 85점으로 수정
score['python'] = 85
print(score)

# 3. 전체 과목 평균 점수 출력
print(sum(score.values()) / len(score.values()))

