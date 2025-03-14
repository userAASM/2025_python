#함수정의
def get_radius(prompt):
    r = int(input(prompt))
    return r

def get_circle_area(int_r):
    msg_area = 3.14*int_r*int_r
    return msg_area

#분문
input_r = "넓이를 구하고자하는 원의 반지름을 입력하세요."
result = get_radius(input_r)
area = get_circle_area(result)
print("반지름 ", result , "인 원의 넓이 = 3.14 x " , result , " x " , result , " = " , area)
