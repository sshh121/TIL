# ## 버블 정렬 => N^2
# lst = [55, 7, 78, 12, 42]
# N = 5
# for phase in range(N-1, 0, -1): # N번 반복
#     for st in range(0, phase): # 0~N-1 -> N번 반복
#         if lst[st] > lst[st+1]:
#             lst[st], lst[st+1] = lst[st+1], lst[st]



# # 1단계 => idx 4(N-1)가 결정됨
# '''
# idx 0, 1 : 7 55 78 12 42
# idx 1, 2 : 7 55 78 12 42
# idx 2, 3 : 7 55 12 78 42
# idx 3, 4 : 7 55 12 42 78
# '''
# for st in range(0, 4): # 0 ~ N-1
#     if lst[st] > lst[st+1]:
#         lst[st], lst[st+1] = lst[st+1], lst[st]


# # 2단계 => idx 3이 결정
# # 7 55 12 42 비교 [78]
# '''
# idx 0, 1 : 7 55 12 42
# idx 1, 2 : 7 12 55 42
# idx 2, 3 : 7 12 42 55
# '''
# for st in range(0, 3): # 0 ~ N-2
#     if lst[st] > lst[st+1]:
#         lst[st], lst[st+1] = lst[st+1], lst[st]

# # 3단계 => idx 2가 결정
# # 7 12 42 비교 [55 78]
# '''
# idx 0, 1 : 7 12 42
# idx 1, 2 : 7 12 42
# '''

# # 4단계 => idx 1이 결정
# # 7 12 비교 [42 55 78]

#-------
# 카운팅 정렬
K = 9 #나올 수 있는 자연수의 최댓값
N = 8 #
#num은 0에서 9까지 발생할 수 있다
lst = [0, 4, 1, 3, 1, 2, 4, 1]
cnt = [0]*(K+1)

for num in lst:
    cnt[num] += 1
print(cnt) 

for idx in range(1, K+1):
    cnt[idx] = cnt[idx] + cnt[idx-1]
print(cnt)
'''
cnt[1] = cnt[0] + cnt[1]
cnt[2] = cnt[1] + cnt[2]
...
cnt[9] = cnt[8] + cnt[9]
'''

temp = [-1]*N # -1이면 비어있는 상태 -> 초기화는 원하는 거 아무거나 해도 됨
for num in lst[::-1]:
    pos = cnt[num] - 1
    temp[pos] = num
    cnt[num] -= 1

# for idx in range(10):
#     num = lst[idx]
#     cnt[num] += 1
#     # cnt[lst[idx]] += 1


#----1206_view

