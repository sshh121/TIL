orders = ['아이스아메리카노','카라멜마키야또','에스프레소','아메리카노','아메리카노','아이스라떼','핫초코','아이스아메리카노','아메리카노','아이스카라멜마키야또','아이스라떼','라떼마키야또','카푸치노','라떼마키야또']

# 1.
count = 0
for i in orders:   #포함되면 True 출력
    if '아이스' in i:
        count += 1
print(f'아이스 음료 주문 : {count}개')

# 2. 
orders_list = sorted(list(set(orders)))  #중복 없는 메뉴

for i in orders_list:
    print(f'{i} : {orders.count(i)}개')

