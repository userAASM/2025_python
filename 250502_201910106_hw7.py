shopping_bag = {}
print('[구입]')
while True:
    item = input('상품명? ')    
    if item.isalpha() :
        shopping_bag[item] = input('수량은? ')
        print(f'장바구니에 {item}가(이) 담겼습니다.\n')
    else:
        break

print(f'\n>>>장바구니 보기: {shopping_bag}\n')

print('[검색]')
while True:
    item = input('장바구니에서 확인하고자 하는 상품은? ')
        
    if item in shopping_bag :
        count = shopping_bag.get(item)
        print(f'{item}은(는) {count}개가 담겼습니다.')
        
    else:
        print('검색한 물건은 장바구니에 없습니다. 검색을 종료합니다.')
        break
