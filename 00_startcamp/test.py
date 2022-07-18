#import hello
# 모듈 불러올 때 뒤에 확장자 .py 생략 가능

#print(hello.greeting)\

from hello import greeting, player
from hello import bot  #함수 불러올 때 소괄호 필요 없음 -> 소괄호 붙이는 것은 함수 실행한다는 의미



print(greeting)
print(player)

bot()
