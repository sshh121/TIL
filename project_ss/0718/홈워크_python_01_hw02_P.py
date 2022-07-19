s = input('숫자를 입력해주세요 : ')
s = list(s)
s_len = len(s)

sum = 0
for i in s:
    sum += int(i)
print(sum)