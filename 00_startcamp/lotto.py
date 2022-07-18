# 1.   lotto api로 부터 데이터 받아오기
# 2. 지난주 당첨 번호 알아내기 (1등만)
# 3. random module 이 가지고 있는 sample이라는 함수를 사용하여 1부터 45중에 무작위 6개 뽑는다.
# 4. 그 번호가 내 당첨번호와 일치하는지 확인한다.
# (5.) 1000번 이상 새로운 로또 번호를 생성하여 매번 당첨이 되었는지 확인해보는 로직 작성
# (6.) 1등부터 2등을 포함한 (보너스번호까지) 4등까지의 각 당첨 횟수 출력하기
# 여러줄 한 번에 주석처리 할 때 ctrl+/

import requests

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1024'
response = requests.get(url).json()

lotto = {response['drwtNo1'], response['drwtNo2'], response['drwtNo3'], response['drwtNo4'], response['drwtNo5'], response['drwtNo6']}
lotto_bnus = {response['bnusNo']}
No = response['drwNo']
print('당첨번호 : ' + str(lotto)) 
print('보너스번호 : ' + str(lotto_bnus))
print('\n')


from random import sample

first, second, third, fourth, fifth = 0, 0, 0, 0, 0

for i in range(1000000):
    my_num = set(sample(range(1,46),6))
    res = len(lotto & my_num)

    if res == 6:
        first += 1
    elif res == 5:
        if len(my_num & lotto_bnus) == 1:
            second += 1
        else:
            third += 1
    elif res == 4:
        fourth += 1
    elif res == 3:
        fifth += 1

print( str(No) + '회 당첨횟수')
print('1등 : ' + str(first) + '\n2등 : ' + str(second) + '\n3등 : ' + str(third) + '\n4등 : ' + str(fourth) + '\n5등 : ' + str(fifth))

