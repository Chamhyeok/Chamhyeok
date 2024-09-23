# 14 def

import time

#함수 정의(구현 or 기술)
def multiple_table(name, num):
    print('MASTER:', name)
    for k in range (1,10):
        print(f'{num} * {k} = {num*k}')

def tot(x, y):
    print('총점:',x+y)
    print('평균:',(x+y)/2)

#함수 호출
if __name__ == '__main__':
    multiple_table('찬돌', 7)
    print()
    kor = 90
    eng = 82
    tot(kor, eng)
    