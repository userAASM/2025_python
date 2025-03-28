#함수정의
def get_fixed_price(discount_price):
    fixed_price = discount_price/((100-discount_rate)/100)
    return fixed_price

def input_price():
    discount_price = int(input("A 상품의 할인된 가격은? "))
    fixed_price_A = get_fixed_price(discount_price) #get_fixed_price 호출 1회
    discount_price = int(input("B 상품의 할인된 가격은? "))
    fixed_price_B = get_fixed_price(discount_price) #get_fixed_price 호출 2회
    print("A 상품의 정가는 ", fixed_price_A, " 원")
    print("B 상품의 정가는 ", fixed_price_B, " 원")

#본문
discount_rate = int(input("할인율은? "))
input_price()
