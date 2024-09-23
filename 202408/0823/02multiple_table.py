# 02 multiple_table

import time
    
num = int(input('원하는 단 입력: '))
for x in range(1, 10, 1) :
    # print(num, '*', x, '=',(num * x))
    print(f'{num}*{x}={num*x}')
    time.sleep(0.5)