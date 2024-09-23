# 08Exception

x, y = 0, 0

hap, kop, mok, nmg = 0,0,0,0

try:
    x = int(input('x값 정수 입력: '))
    y = int(input('y값 정수 입력: '))

    hap = x+y
    kop = x*y
    mok = x/y
    nmg = x%y
    print(f'{x} + {y} = {hap}')     #연산되는 것이 아니라 변수 선언한 값만 나옴
    print(f'{x} / {y} = {mok}')
    print(f'{x} % {y} = {nmg}')
    print(f'{x} * {y} = {kop}')

except Exception as ex:
    print('원인: ', ex)

# print(f'{x} + {y} = {hap}')     #연산되는 것이 아니라 변수 선언한 값만 나옴
# print(f'{x} / {y} = {mok}')
# print(f'{x} % {y} = {nmg}')
# print(f'{x} * {y} = {kop}')

# print('%d정수' %(데이터))
#  