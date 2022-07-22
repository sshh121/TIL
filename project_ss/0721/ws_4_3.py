####미완 ㅠ

def remove_num(list):
    pass
    #return
    for idx, num in enumerate(list):
        if list[idx+1] == num:
            list.pop(idx+1)  #pop은 인덱스로 값 삭제 후 삭제한 값 반환
    return list


numbers = [1,1,3,3,0,1,1]
print(remove_num(numbers))
