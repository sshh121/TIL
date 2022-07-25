'''
word = 'python'
print(word)
print(id(word))  #메모리 주소 확인 3098148905328

word = 'test'
print(word)
print(id(word))  #메모리 주소 확인 3098148897840

# python를 변경한 것이 아니라 아예 새로운 단어로 덮어씌워진 것
# python 삭제되고 test가 생긴 것
# python는 기존 메모리 주소에 그대로 있음
# test는 다른 메모리 주소에 생긴 것

print('apple'.find('p')) #1:인덱스 1번
print('apple'.find('k')) #-1 :없음!
print('apple'.index('k')) #오류남
print('abc'.isalpha()) #True
print('ㄱㄴㄷ'.isalpha()) #True


print('a,b,c'.split(',')) #['a','b','c']
#ex
print('서울시 강남구 테헤란로'.split()[0])

msg = 'hI! Everyone, I\'m python'
print(msg)
print(msg.capitalize()) #Hi! everyone, i'm python
print(msg.title()) #Hi! Everyone, I'M python
print(msg.upper()) #HI! EVERYONE, I'M python
print(msg.lower()) #hi! everyone, i'm python

print('*'.join(['python', 'busan'])) #python*busan
print(' '.join(['3', '5'])) #3 5


#------리스트
cafe = ['starbucks', 'tomntoms', 'hollys']
print(id(cafe))
cafe.append('banapresso')
print(cafe)
print(id(cafe))

cafe.insert(0,'start')
print(cafe)
cafe.insert(100000, 'end') #에러 나지 않고, 맨끝에 들어감
print(cafe)

cafe.extend(['coffee'])
print(cafe)
cafe.extend('cup') #['start', 'starbucks', 'tomntoms', 'hollys', 'banapresso', 'end', 'coffee', 'c', 'u', 'p']
print(cafe)


numbers = [1, 2, 3, 'hi']
print(numbers)
word = numbers.pop()
print(word)
print(numbers)

numbers.clear()
print(numbers)

numbers = [3, 2, 5, 7]
result = numbers.sort() #None 반환
print(numbers, result)

# result = numbers.sorted() : 잘못된 표현식
result = sorted(numbers)
print(numbers, result)

#----------셋
a = {'사과', '바나나', '수박'}
print(type(a))
print(a)
a.add('딸기')
print(a)

a.update(['망고', '메론', '수박'])
print(a)
'''

# 얕은 복사
original_list = [1,2,3]
copy_list = original_list
print(original_list, copy_list)

copy_list[0] = 'hello'
print(original_list, copy_list)


#깊은 복사
import copy
a = [[1,2,3], [4,5,6],[7,8,9]]
b= copy.deepcopy(a)
print(a,b)

b[0][2] = 'hello'
print(a,b)