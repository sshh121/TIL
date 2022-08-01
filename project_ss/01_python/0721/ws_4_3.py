####미완 ㅠ
'''
def remove_num(list):
    pass
    #return
    for idx, num in enumerate(list):
        if list[idx+1] == num:
            list.pop(idx+1)  #pop은 인덱스로 값 삭제 후 삭제한 값 반환, pop안에 인자 안넣으면 마지막값 반환 후 삭제 ==> '추출'의 의미로 쓰일 수 있음
    return list
'''
def remove_num(list):
    pass
    #return
    for idx, num in enumerate(list):
        if list[idx+1] == num:
            del list[idx+1]  #del로 해당 값 삭제 
    return list

numbers = [1,1,3,3,0,1,1]
print(remove_num(numbers))
