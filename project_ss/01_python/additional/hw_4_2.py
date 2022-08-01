#끝말잇기 단어 리스트 -> 탈락 하는 사람 몇번쨰?
# 끝말잇기 틀리거나, 이전에 등장했던 단어 사용하는 경우 탈락
#done을 입력할때까지 끝말잇기 시행


words = ["round", "dream", "magnet", "tweet", "trick","kiwi", "apple"]

for i in range(len(words)):
    if words[i+1] == "done":
        break
    else:          
        if words[i][-1] != words[i+1][0]:
            print(f'{i+2}번째 사람이 탈락!')
            break
        elif words[i] in words[:i]:
            print(f'{i+1}번째 사람이 탈락!!')
            break
