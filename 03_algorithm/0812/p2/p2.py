def itoa(num): #int를 문자열로 바꾸는 함수
    # 넘겨받은 정수를 0이 되기 전까지 계속 반복
    negative = False
    if num < 0:
        negative = True
        num = -num
    if num == 0:
        return '0'

    result = ''
    while num:
        remainder = num % 10
        result = chr(ord('0') + remainder) + result # 순서에 주의
        num = num // 10

    if negative:
        return '-' + result
    else:
        return result

print(itoa(123)*3) # 문자열로 변환되어 123이 곱해지는 것이 아니라 반복됨
print(itoa(0))
print(itoa(-3))






'''
    result = ''

    while abs(num) > 0:
    # 일의 자리 수부터 끊어서 문자열로 변환
        char = chr(abs(num) % 10) - chr()
        num = abs(num) // 10
        result = char + result
    # atoi에서는 ord(char)-ord('0') 사용

    # 만약 처음 넘겨 받은 값이 음수였다면
    if num < 0:
        result = '-'+result
        return result
    else:
        return result
    # 문자열 앞에 '-' 붙여서 반환


    # num % 10
    pass

'''
