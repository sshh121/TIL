
salt = []
saltwater_all = []

i = 0
while i <= 5:
    i+=1
    x = input(f'{i}.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: ')

    if x == 'Done':
        break
    else:
        per, saltwater = x.split()
        per = int(per[:-1]) #농도
        saltwater = int(saltwater[:-1]) #소금물의 양

        salt.append(round(per*saltwater/100,2)) #소금의 양
        saltwater_all.append(saltwater) #소금물

saltwater_total = sum(saltwater_all)
per_total = sum(salt)*100/saltwater_total
        
print('{:.2f}% {}g'.format(per_total, saltwater_total))


