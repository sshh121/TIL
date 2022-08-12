def my_len(arr): # 배열을 입력받을 것, 배열의 개수를 세는 함수
    idx = 0
    # \0 문자를 만나기 전까지는 개수 세기
    # \0 문자를 만나면 종료
    while True:
        if arr[idx] == '\0':
            return idx
        idx += 1
    return idx

arr = ['짜', '장', '면', '\0']
print(my_len(arr))