def new_fruit(old):
    old = old.split(',')
    # print(old)
    # new = []
    # for i in old:
    #     new.append(i.lower())
    # print(new)

    for i in range(len(old)):
        old[i] = old[i].lower().replace('rotten', '')
    return old

    

print(new_fruit('apple,rottenBanana,apple,RoTTenorange,Orange'))