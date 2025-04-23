#사용자 정의 함수부

def rep_chr(c, n):
    return(c*n)

def welcome(name):
    msg1 = f'Hello {name}, '
    msg2 = 'Welcome to Seoul.'
    if len(msg1) > len(msg2):
        box = rep_chr('-', len(msg1)+2)
    else:
        box = rep_chr('-', len(msg2)+2)
    print(f'{box}\n {msg1}\n {msg2}\n{box}')


#주 프로그램부
name = welcome(input('Input name: '))
