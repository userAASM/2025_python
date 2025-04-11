def read_single_digit(num):
    if num == '0' :
        return '영'
    elif num <= '1' :
        return '일'
    elif num <= '2' :
        return '이'
    elif num <= '3' :
        return '삼'
    elif num <= '4' :
        return '시'
    elif num <= '5' :
        return '오'
    elif num <= '6' :
        return '육'
    elif num <= '7' :
        return '칠'
    elif num <= '8' :
        return '팔'
    else:
        return '구'


def read_number(n):
    number = str(input(n))
    num100 = read_single_digit(number[0])
    num10 = read_single_digit(number[1])
    num1 = read_single_digit(number[2])
    read_num = (f'{num100} {num10} {num1}')
    return read_num

n = read_number('세 자리 정수 입력: ')
print(n)
