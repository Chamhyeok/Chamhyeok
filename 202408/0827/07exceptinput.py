# 07exceptinput
# 문제 1. dan 입력 키보드 input(), 형변환
# 문제 2. dan 입력 범위 정수 1이상

import time

dan = 0
try :
    dan = int(input('원하는 단 입력: '))
    if dan < 2 or dan > 9 :
        print('2~9 사이의 숫자를 입력하세요.')
    elif 10 > dan > 1 :
        for k in range(1,10) :
            print(f'{dan}*{k}={dan*k}')
            time.sleep(0.3)
except :
    print('2~9 사이의 숫자를 입력하세요.')

    

print()
# time.sleep(0.5)
# print('포인트 7점 획득')
# print('포인트 5점 이상이면 vip 혜택 부여')