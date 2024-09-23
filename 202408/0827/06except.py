# 06except

x = 8
y = 0

hap, kop, mok, nmg = 0,0,0,0

try:
    pass

    hap = x+y
    kop = x*y
    mok = x/y
    nmg = x%y

except:
    pass
    print('연산 처리가 잘못되었습니다.')

print(f'{x} + {y} = {hap}')     #연산되는 것이 아니라 변수 선언한 값만 나옴
print(f'{x} / {y} = {mok}')
print(f'{x} % {y} = {nmg}')
print(f'{x} * {y} = {kop}')

# print('%d정수' %(데이터))
#  