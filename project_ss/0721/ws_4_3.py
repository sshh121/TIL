'''
'''
####미완 ㅠ
numbers = list(input())
len_num = len(numbers)
for num in range(len_num-1):
    if numbers[num] == numbers[num+1] :
        numbers.pop(num+1)
        len_num -=1
        
print(numbers)
