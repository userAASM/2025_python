def buy(shopping_bag):
    print('[구입]')
    item = input('상품명? ')    

    if item.isalpha() :
        shopping_bag[item] = input('수량은? ')
        count = shopping_bag.get(item)    
        print(f'장바구니에 {item} {count}개 가 담겼습니다.\n')
        
    else:
        return False


def show(shopping_bag):
    print(f'\n>>>장바구니 보기: {shopping_bag}\n')

def find(shopping_bag):
    while True:
        print('[검색]')
        item = input('장바구니에서 확인하고자 하는 상품은? ')
                
        if item in shopping_bag :
            count = shopping_bag.get(item)
            print(f'{item}은(는) {count}개 담겨 있습니다.')
        else:
            print(f'장바구니에 {item}은(는) 없습니다.')
            break

#주 프로그램부

shopping_bag = {}
while True:
    if buy(shopping_bag) == False:
        break

show(shopping_bag)
find(shopping_bag)
