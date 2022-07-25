def sum_of_repeat_num(lst):
    result = 0
    for num in lst:
        if lst.count(num)==1:
            result += num
    return result

print(sum_of_repeat_num([4,4,7,8,10,4]))

