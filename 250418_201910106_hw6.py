#개념확인문제
'''
단 입력 없이 2~5단이 4열에 걸쳐 나온 후, 한 줄 띄고 아래에 6~9단
'''

def display_1st_table(n):
    row =''
    for i in range(2, 6) :
        row_ele = f'{i} x {n} = {i * n:2d}\t'
        row += row_ele
    print(row)

def display_2nd_table(n):
    row =''
    for i in range(6, 10) :
        row_ele = f'{i} x {n} = {i * n:2d}\t'
        row += row_ele
    print(row)
    

for a in range(1, 10):
    display_1st_table(a)
print()
for a in range(1, 10):
    display_2nd_table(a)
