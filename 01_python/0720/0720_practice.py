'''
#--- 조건문 실습
num = int(input())  # input은 문자역 'str'으로 출력됨
if num%2==0:
    print('짝수')
else:
    print('홀수')
'''

#---삼항연산자
num=2
result = '홀수' if num%2 else '짝수'
#나머지가 1이면 truthy => 참, 나머지가 0이면 falsy => 거짓
print(result)


num = -5
if num >= 0 :
    value = num
else:
    value = 0
print(value)